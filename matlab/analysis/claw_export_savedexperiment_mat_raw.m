function rawExport = claw_export_savedexperiment_mat_raw(dataPath)
%CLAW_EXPORT_SAVEDEXPERIMENT_MAT_RAW Export a saved Scan .mat without analysis.
%
% This helper is for agent-visible raw exports. It serializes the saved
% MATLAB variables into JSON-friendly values and generates a raw-readout plot.
% It intentionally does not compute signal summaries, fit metrics, readout
% statistics, normalized contrasts, verdicts, or hidden-derived-field flags.

rawExport = struct( ...
    'ok', false, ...
    'source', 'savedexperiment_mat_raw_export', ...
    'data_path', '', ...
    'mat_variables', {{}}, ...
    'scan', struct(), ...
    'extra_variables', struct(), ...
    'diagnostic_figures', struct(), ...
    'warnings', {{}}, ...
    'error_code', '', ...
    'error_message', '');

try
    if nargin < 1
        error('NVClaw:MissingDataPath', 'A savedexperiment .mat path is required.');
    end

    dataPath = char(string(dataPath));
    if exist(dataPath, 'file') ~= 2
        error('NVClaw:MissingDataPath', 'Savedexperiment file not found: %s', dataPath);
    end

    loaded = load(dataPath);
    if ~isfield(loaded, 'Scan')
        error('NVClaw:MissingScan', 'Savedexperiment file did not contain a Scan variable.');
    end

    rawExport.ok = true;
    rawExport.data_path = dataPath;
    rawExport.mat_variables = local_mat_variable_list(dataPath);
    rawExport.scan = local_jsonable(loaded.Scan, 0);
    rawExport.extra_variables = local_extra_variable_export(loaded, {'Scan'});
    rawExport.diagnostic_figures = local_raw_readout_figures(dataPath, loaded.Scan);
    rawExport.warnings = local_concat_cell(rawExport.warnings, ...
        local_struct_field(rawExport.diagnostic_figures, 'warnings', {}));
catch ex
    rawExport.ok = false;
    rawExport.error_code = local_text_or(ex.identifier, 'NVClaw:SavedExperimentRawExportFailed');
    rawExport.error_message = local_text_or(ex.message, 'Failed to export the savedexperiment .mat file.');
end
end

function extra = local_extra_variable_export(loaded, skipNames)
extra = struct();
if ~isstruct(loaded)
    return;
end
names = fieldnames(loaded);
for idx = 1:numel(names)
    name = names{idx};
    if any(strcmp(name, skipNames))
        continue;
    end
    extra.(name) = local_jsonable(loaded.(name), 0);
end
end

function variables = local_mat_variable_list(dataPath)
variables = {};
try
    info = whos('-file', dataPath);
    for idx = 1:numel(info)
        item = struct();
        item.name = info(idx).name;
        item.class = info(idx).class;
        item.size = double(info(idx).size);
        variables{end + 1} = item; %#ok<AGROW>
    end
catch
end
end

function diagnostics = local_raw_readout_figures(dataPath, scan)
diagnostics = struct( ...
    'available', false, ...
    'png_path', '', ...
    'png_path_wsl', '', ...
    'contents', {{}}, ...
    'warnings', {{}});

try
    experimentData = local_object_property(scan, 'ExperimentData', {});
    scanIndex = local_first_nonempty_scan(experimentData);
    if isempty(scanIndex)
        diagnostics.warnings = {'Raw-readout PNG was not generated because ExperimentData was unavailable.'};
        return;
    end

    combinedReadouts = local_numeric_readout_values(experimentData{scanIndex});
    if isempty(combinedReadouts)
        diagnostics.warnings = {'Raw-readout PNG was not generated because combined readouts were empty.'};
        return;
    end

    outputDir = local_diagnostic_output_dir(dataPath);
    if isempty(outputDir)
        diagnostics.warnings = {'Raw-readout PNG was not generated because no writable output directory was available.'};
        return;
    end

    stem = local_safe_file_stem(dataPath);
    pathHash = local_path_hash(dataPath);
    pngPath = fullfile(outputDir, [stem '__' pathHash '__raw_readouts.png']);

    fig = figure('Visible', 'off', 'Color', 'w', 'Position', [100 100 1200 700]);
    cleanupFig = onCleanup(@() local_close_figure(fig)); %#ok<NASGU>

    xValues = local_scan_x_values(scan);
    sequenceName = local_text_or(local_object_property(scan, 'SequenceName', ''), '');
    dateTime = local_text_or(local_object_property(scan, 'DateTime', ''), '');
    averageEntries = local_average_entries_for_scan(scan, scanIndex);

    subplot(2, 1, 1);
    local_plot_combined_raw_readouts(gca, xValues, combinedReadouts);
    title(sprintf('Combined raw readouts | %s | %s', sequenceName, dateTime), 'Interpreter', 'none');

    subplot(2, 1, 2);
    local_plot_per_average_raw_overlay(gca, xValues, averageEntries, combinedReadouts);
    title('Per-average raw readout overlay', 'Interpreter', 'none');

    set(fig, 'PaperPositionMode', 'auto');
    print(fig, pngPath, '-dpng', '-r160');

    diagnostics.available = exist(pngPath, 'file') == 2;
    diagnostics.png_path = pngPath;
    diagnostics.png_path_wsl = local_to_wsl_path(pngPath);
    diagnostics.contents = {'combined raw readouts', 'per-average raw readout overlay'};
    if ~diagnostics.available
        diagnostics.warnings = {'Raw-readout PNG print completed but the output file was not found.'};
    end
catch ex
    diagnostics.available = false;
    diagnostics.warnings = {['Raw-readout PNG generation failed: ' local_text_or(ex.message, 'unknown error')]};
end
end

function local_plot_combined_raw_readouts(ax, xValues, combinedReadouts)
axes(ax); %#ok<LAXES>
hold(ax, 'on');
colors = lines(max(1, numel(combinedReadouts)));
labels = {};
for idx = 1:numel(combinedReadouts)
    y = combinedReadouts{idx};
    if ~isnumeric(y) || isempty(y)
        continue;
    end
    x = local_x_for_y(xValues, y);
    plot(ax, x, y, 'LineWidth', 1.4, 'Color', colors(idx, :));
    labels{end + 1} = sprintf('readout %d', idx); %#ok<AGROW>
end
grid(ax, 'on');
xlabel(ax, 'scan value');
ylabel(ax, 'raw readout');
if ~isempty(labels)
    legend(ax, labels, 'Location', 'best', 'Interpreter', 'none');
end
hold(ax, 'off');
end

function local_plot_per_average_raw_overlay(ax, xValues, averageEntries, combinedReadouts)
axes(ax); %#ok<LAXES>
hold(ax, 'on');
readoutCount = max(1, numel(combinedReadouts));
colors = lines(readoutCount);
plottedAny = false;
if iscell(averageEntries)
    for avgIdx = 1:numel(averageEntries)
        readouts = local_numeric_readout_values(averageEntries{avgIdx});
        for ridx = 1:min(numel(readouts), readoutCount)
            y = readouts{ridx};
            if ~isnumeric(y) || isempty(y)
                continue;
            end
            x = local_x_for_y(xValues, y);
            plot(ax, x, y, 'LineWidth', 0.45, 'Color', local_light_color(colors(ridx, :)));
            plottedAny = true;
        end
    end
end

labels = {};
for ridx = 1:numel(combinedReadouts)
    y = combinedReadouts{ridx};
    if ~isnumeric(y) || isempty(y)
        continue;
    end
    x = local_x_for_y(xValues, y);
    plot(ax, x, y, 'LineWidth', 1.7, 'Color', colors(ridx, :));
    labels{end + 1} = sprintf('combined readout %d', ridx); %#ok<AGROW>
    plottedAny = true;
end
if ~plottedAny
    text(ax, 0.5, 0.5, 'No per-average raw readouts available', 'Units', 'normalized', ...
        'HorizontalAlignment', 'center');
end
grid(ax, 'on');
xlabel(ax, 'scan value');
ylabel(ax, 'raw readout');
if ~isempty(labels)
    legend(ax, labels, 'Location', 'best', 'Interpreter', 'none');
end
hold(ax, 'off');
end

function averageEntries = local_average_entries_for_scan(scan, scanIndex)
averageEntries = {};
experimentDataEachAvg = local_object_property(scan, 'ExperimentDataEachAvg', {});
if iscell(experimentDataEachAvg) && numel(experimentDataEachAvg) >= scanIndex && ...
        iscell(experimentDataEachAvg{scanIndex})
    averageEntries = experimentDataEachAvg{scanIndex};
end
end

function scanIndex = local_first_nonempty_scan(experimentData)
scanIndex = [];
if ~iscell(experimentData)
    return;
end
for idx = 1:numel(experimentData)
    if iscell(experimentData{idx}) && ~isempty(experimentData{idx})
        scanIndex = idx;
        return;
    end
end
end

function values = local_numeric_readout_values(avgEntry)
values = {};
if ~iscell(avgEntry)
    return;
end
for idx = 1:numel(avgEntry)
    readout = avgEntry{idx};
    if isnumeric(readout) && ~isempty(readout)
        values{end + 1} = double(reshape(readout, 1, [])); %#ok<AGROW>
    end
end
end

function x = local_x_for_y(xValues, y)
if isnumeric(xValues) && numel(xValues) == numel(y)
    x = reshape(double(xValues), 1, []);
else
    x = 1:numel(y);
end
end

function color = local_light_color(color)
color = 0.72 + 0.28 .* color;
color = min(max(color, 0), 1);
end

function xValues = local_scan_x_values(scan)
xValues = [];
varyBegin = local_object_property(scan, 'vary_begin', []);
varyEnd = local_object_property(scan, 'vary_end', []);
varyPoints = local_object_property(scan, 'vary_points', []);

if isnumeric(varyBegin) && isnumeric(varyEnd) && isnumeric(varyPoints) && ...
        isscalar(varyBegin) && isscalar(varyEnd) && isscalar(varyPoints) && varyPoints > 0
    xValues = linspace(double(varyBegin), double(varyEnd), double(varyPoints));
end
end

function outputDir = local_diagnostic_output_dir(dataPath)
outputDir = '';
envDir = local_text_or(getenv('OPENCLAW_SAVEDEXPERIMENT_FIGURE_DIR'), '');
candidates = {};
if ~isempty(envDir)
    candidates{end + 1} = envDir; %#ok<AGROW>
end
if ~isempty(dataPath)
    candidates{end + 1} = fullfile(fileparts(dataPath), 'openclaw_diagnostic_figures'); %#ok<AGROW>
end

for idx = 1:numel(candidates)
    candidate = candidates{idx};
    if isempty(candidate)
        continue;
    end
    try
        if exist(candidate, 'dir') == 7 || mkdir(candidate)
            outputDir = candidate;
            return;
        end
    catch
    end
end
end

function stem = local_safe_file_stem(pathValue)
[~, stem] = fileparts(char(pathValue));
if isempty(stem)
    stem = 'savedexperiment';
end
stem = regexprep(stem, '[^A-Za-z0-9_.-]', '_');
if numel(stem) > 96
    stem = stem(1:96);
end
end

function hashText = local_path_hash(pathValue)
text = char(pathValue);
try
    md = java.security.MessageDigest.getInstance('MD5');
    md.update(uint8(text));
    digest = typecast(md.digest(), 'uint8');
    hashText = lower(reshape(dec2hex(digest)', 1, []));
    hashText = hashText(1:12);
catch
    values = double(uint8(text));
    hashValue = mod(sum(values .* (1:numel(values))), 2^32);
    hashText = sprintf('%08x', hashValue);
end
end

function wslPath = local_to_wsl_path(pathValue)
wslPath = '';
pathText = char(pathValue);
distro = getenv('WSL_DISTRO_NAME');
if isempty(distro)
    uncPrefix = '';
else
    uncPrefix = ['\\' '\\' 'wsl.localhost\\' distro '\\'];
end
if strncmpi(pathText, uncPrefix, numel(uncPrefix))
    rest = pathText(numel(uncPrefix) + 1:end);
    wslPath = ['/' strrep(rest, '\', '/')];
    return;
end
if numel(pathText) >= 3 && pathText(2) == ':' && (pathText(3) == '\' || pathText(3) == '/')
    drive = lower(pathText(1));
    rest = strrep(pathText(4:end), '\', '/');
    wslPath = ['/mnt/' drive '/' rest];
end
end

function local_close_figure(fig)
try
    if ~isempty(fig) && all(ishandle(fig))
        close(fig);
    end
catch
end
end

function out = local_jsonable(value, depth)
if nargin < 2
    depth = 0;
end
if depth > 12
    out = local_text_or(class(value), 'depth_limit');
    return;
end

if isempty(value)
    out = value;
elseif isnumeric(value) || islogical(value)
    out = value;
elseif ischar(value)
    out = value;
elseif isstring(value)
    out = cellstr(value);
    if isscalar(value)
        out = char(value);
    end
elseif iscell(value)
    out = cell(size(value));
    for idx = 1:numel(value)
        out{idx} = local_jsonable(value{idx}, depth + 1);
    end
elseif isstruct(value)
    if numel(value) == 1
        out = struct();
        names = fieldnames(value);
        for idx = 1:numel(names)
            name = names{idx};
            out.(name) = local_jsonable(value.(name), depth + 1);
        end
    else
        out = cell(size(value));
        for idx = 1:numel(value)
            out{idx} = local_jsonable(value(idx), depth + 1);
        end
    end
elseif isa(value, 'function_handle')
    out = func2str(value);
elseif isobject(value)
    if numel(value) == 1
        out = struct();
        out.matlab_class = class(value);
        try
            propNames = properties(value);
        catch
            propNames = {};
        end
        for idx = 1:numel(propNames)
            name = propNames{idx};
            try
                out.(name) = local_jsonable(value.(name), depth + 1);
            catch
                out.(name) = '';
            end
        end
    else
        out = cell(size(value));
        for idx = 1:numel(value)
            out{idx} = local_jsonable(value(idx), depth + 1);
        end
    end
else
    try
        out = char(string(value));
    catch
        out = '';
    end
end
end

function value = local_struct_field(s, fieldName, defaultValue)
value = defaultValue;
if isstruct(s) && isfield(s, fieldName)
    value = s.(fieldName);
end
end

function value = local_object_property(cursor, fieldName, defaultValue)
value = defaultValue;
if isempty(cursor)
    return;
end
if isstruct(cursor)
    if isfield(cursor, fieldName)
        value = cursor.(fieldName);
    end
elseif isobject(cursor)
    if isprop(cursor, fieldName)
        value = cursor.(fieldName);
    end
end
end

function value = local_text_or(rawValue, defaultValue)
value = defaultValue;
if ischar(rawValue)
    value = rawValue;
elseif isstring(rawValue) && isscalar(rawValue)
    value = char(rawValue);
end
end

function merged = local_concat_cell(varargin)
merged = {};
for k = 1:nargin
    part = varargin{k};
    if isempty(part)
        continue;
    end
    if iscell(part)
        merged = [merged part]; %#ok<AGROW>
    else
        merged{end + 1} = part; %#ok<AGROW>
    end
end
end
