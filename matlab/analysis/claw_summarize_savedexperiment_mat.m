function summary = claw_summarize_savedexperiment_mat(dataPath)
%CLAW_SUMMARIZE_SAVEDEXPERIMENT_MAT Summarize a saved Scan .mat for agent use.
%
% summary fields are intentionally compact and JSON-friendly so the
% OpenClaw planners can inspect raw savedexperiment artifacts without
% reading MATLAB objects directly. This helper is also intended for
% autosaved in-progress runs, where the legacy experiment is still active
% but the current savedexperiment MAT already exists on disk.

summary = struct( ...
    'ok', false, ...
    'source', 'savedexperiment_mat', ...
    'data_path', '', ...
    'sequence_name', '', ...
    'date_time', '', ...
    'position', [], ...
    'scan', struct(), ...
    'signal', struct(), ...
    'raw_readouts', struct(), ...
    'average_signal', struct(), ...
    'diagnostic_figures', struct(), ...
    'warnings', {{}}, ...
    'notes', {{}}, ...
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

    loaded = load(dataPath, 'Scan');
    if ~isfield(loaded, 'Scan')
        error('NVClaw:MissingScan', 'Savedexperiment file did not contain a Scan variable.');
    end

    scan = loaded.Scan;

    summary.ok = true;
    summary.data_path = dataPath;
    summary.sequence_name = local_text_or(local_object_property(scan, 'SequenceName', ''), '');
    summary.date_time = local_text_or(local_object_property(scan, 'DateTime', ''), '');
    summary.position = local_numeric_triplet(local_object_property(scan, 'position', []));
    summary.scan = local_scan_summary(scan);
    summary.raw_readouts = local_raw_readout_summary(scan);
    summary.average_signal = local_average_signal_summary(scan);
    summary.diagnostic_figures = local_savedexperiment_diagnostic_figures(dataPath, scan, summary.raw_readouts);
    summary.notes = { ...
        'Extracted directly from the saved Scan object.', ...
        'Useful for autosaved in-progress runs: call this on the current savedexperiment MAT before execute completes to inspect recent per-average results.'};
    summary.warnings = local_concat_cell(summary.warnings, local_struct_field(summary.diagnostic_figures, 'warnings', {}));

    analysis = claw_analyze_saved_scan(struct('data_path', dataPath, 'fit_kind', 'None'));
    if isstruct(analysis)
        signalSummary = local_struct_field(analysis, 'signal', struct());
        if isstruct(signalSummary) && ~isempty(fieldnames(signalSummary))
            summary.signal = local_agent_visible_signal_summary(signalSummary);
        end
        summary.warnings = local_concat_cell(summary.warnings, local_struct_field(analysis, 'warnings', {}));
        if ~local_truthy(local_struct_field(analysis, 'ok', false))
            errorMessage = local_text_or(local_struct_field(analysis, 'error_message', ''), '');
            if ~isempty(errorMessage)
                summary.warnings{end + 1} = ['Signal extraction warning: ' errorMessage]; %#ok<AGROW>
            end
        end
    end
catch ex
    summary.ok = false;
    summary.error_code = local_text_or(ex.identifier, 'NVClaw:SavedExperimentSummaryFailed');
    summary.error_message = local_text_or(ex.message, 'Failed to summarize the savedexperiment .mat file.');
end
end

function diagnostics = local_savedexperiment_diagnostic_figures(dataPath, scan, rawSummary)
diagnostics = struct( ...
    'available', false, ...
    'png_path', '', ...
    'png_path_wsl', '', ...
    'contents', {{}}, ...
    'warnings', {{}});

try
    if ~isstruct(rawSummary) || ~local_truthy(local_struct_field(rawSummary, 'available', false))
        diagnostics.warnings = {'Savedexperiment diagnostic PNG was not generated because raw readouts were unavailable.'};
        return;
    end

    combinedReadouts = local_values_from_series(local_struct_field(rawSummary, 'combined', {}));
    if isempty(combinedReadouts)
        diagnostics.warnings = {'Savedexperiment diagnostic PNG was not generated because combined raw readouts were empty.'};
        return;
    end

    outputDir = local_diagnostic_output_dir(dataPath);
    if isempty(outputDir)
        diagnostics.warnings = {'Savedexperiment diagnostic PNG was not generated because no writable output directory was available.'};
        return;
    end

    stem = local_safe_file_stem(dataPath);
    pathHash = local_path_hash(dataPath);
    pngPath = fullfile(outputDir, [stem '__' pathHash '__diagnostic.png']);

    fig = figure('Visible', 'off', 'Color', 'w', 'Position', [100 100 1200 700]);
    cleanupFig = onCleanup(@() local_close_figure(fig)); %#ok<NASGU>

    xValues = local_struct_field(rawSummary, 'x_values', []);
    sequenceName = local_text_or(local_object_property(scan, 'SequenceName', ''), '');
    dateTime = local_text_or(local_object_property(scan, 'DateTime', ''), '');
    averageEntries = local_struct_field(rawSummary, 'average_entries', {});

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
    diagnostics.contents = { ...
        'combined raw readouts', ...
        'per-average raw readout overlay'};
    if ~diagnostics.available
        diagnostics.warnings = {'Savedexperiment diagnostic PNG print completed but the output file was not found.'};
    end
catch ex
    diagnostics.available = false;
    diagnostics.warnings = {['Savedexperiment diagnostic PNG generation failed: ' local_text_or(ex.message, 'unknown error')]};
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
        entry = averageEntries{avgIdx};
        if ~isstruct(entry)
            continue;
        end
        readouts = local_values_from_series(local_struct_field(entry, 'readouts', {}));
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

function values = local_values_from_series(series)
values = {};
if ~iscell(series)
    return;
end
for idx = 1:numel(series)
    item = series{idx};
    if ~isstruct(item)
        continue;
    end
    y = local_struct_field(item, 'values', []);
    if isnumeric(y) && ~isempty(y)
        values{end + 1} = double(reshape(y, 1, [])); %#ok<AGROW>
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
uncPrefix = local_text_or(getenv('OPENCLAW_WSL_UNC_PREFIX'), '');
if ~isempty(uncPrefix) && strncmpi(pathText, uncPrefix, numel(uncPrefix))
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

function scanSummary = local_scan_summary(scan)
scanSummary = struct();
scanSummary.sequence_name = local_text_or(local_object_property(scan, 'SequenceName', ''), '');
scanSummary.date_time = local_text_or(local_object_property(scan, 'DateTime', ''), '');
scanSummary.vary_prop = local_object_property(scan, 'vary_prop', {});
scanSummary.vary_begin = local_object_property(scan, 'vary_begin', []);
scanSummary.vary_end = local_object_property(scan, 'vary_end', []);
scanSummary.vary_points = local_object_property(scan, 'vary_points', []);
scanSummary.vary_step_size = local_object_property(scan, 'vary_step_size', []);
scanSummary.sample_rate = local_object_property(scan, 'SampleRate', []);
scanSummary.averages = local_object_property(scan, 'Averages', []);
scanSummary.repetitions = local_object_property(scan, 'Repetitions', []);
scanSummary.position = local_numeric_triplet(local_object_property(scan, 'position', []));
scanSummary.variable_values = local_name_value_list(local_object_property(scan, 'Variable_values', {}));
scanSummary.bool_values = local_name_value_list(local_object_property(scan, 'Bool_values', {}));
end

function rawSummary = local_raw_readout_summary(scan)
rawSummary = struct( ...
    'available', false, ...
    'scan_index', 1, ...
    'readout_count', 0, ...
    'num_points', 0, ...
    'x_values', [], ...
    'combined', {{}}, ...
    'total_averages', 0, ...
    'average_entries', {{}}, ...
    'recent_average_limit', 4, ...
    'recent_average_entries', {{}}, ...
    'warnings', {{}});

xValues = local_scan_x_values(scan);
rawSummary.x_values = xValues;
rawSummary.num_points = numel(xValues);

experimentData = local_object_property(scan, 'ExperimentData', {});
scanIndex = local_first_nonempty_average_scan(experimentData);
if isempty(scanIndex)
    rawSummary.warnings = {'ExperimentData did not contain a usable raw readout scan entry.'};
    return;
end

rawSummary.scan_index = scanIndex;
combinedReadouts = local_numeric_readout_values(experimentData{scanIndex});
if isempty(combinedReadouts)
    rawSummary.warnings{end + 1} = 'ExperimentData did not expose numeric raw readout arrays.'; %#ok<AGROW>
else
    rawSummary.available = true;
    rawSummary.readout_count = numel(combinedReadouts);
    rawSummary.combined = local_readout_series_list(combinedReadouts);
    rawSummary.warnings = local_concat_cell(rawSummary.warnings, ...
        local_readout_length_warnings(combinedReadouts, xValues, 'combined'));
end

experimentDataEachAvg = local_object_property(scan, 'ExperimentDataEachAvg', {});
if ~iscell(experimentDataEachAvg) || numel(experimentDataEachAvg) < scanIndex || isempty(experimentDataEachAvg{scanIndex})
    return;
end

averageEntries = experimentDataEachAvg{scanIndex};
if ~iscell(averageEntries) || isempty(averageEntries)
    return;
end

rawSummary.total_averages = numel(averageEntries);
allEntries = {};
for idx = 1:numel(averageEntries)
    readoutValues = local_numeric_readout_values(averageEntries{idx});
    if isempty(readoutValues)
        rawSummary.warnings{end + 1} = sprintf('Average %d did not expose numeric raw readout arrays.', idx); %#ok<AGROW>
        continue;
    end
    entry = struct();
    entry.average_index = idx;
    entry.readout_count = numel(readoutValues);
    entry.num_points = local_readout_num_points(readoutValues);
    entry.readouts = local_readout_series_list(readoutValues);
    allEntries{end + 1} = entry; %#ok<AGROW>
    rawSummary.warnings = local_concat_cell(rawSummary.warnings, ...
        local_readout_length_warnings(readoutValues, xValues, sprintf('average %d', idx)));
end
rawSummary.average_entries = allEntries;

recentLimit = rawSummary.recent_average_limit;
recentStart = max(1, numel(allEntries) - recentLimit + 1);
recentEntries = allEntries(recentStart:end);
rawSummary.recent_average_entries = recentEntries;
end

function averageSummary = local_average_signal_summary(scan)
averageSummary = struct( ...
    'available', false, ...
    'scan_index', 1, ...
    'total_averages', 0, ...
    'recent_limit', 4, ...
    'readout_count', 0, ...
    'recent_entries', {{}}, ...
    'warnings', {{}}, ...
    'latest_mean_delta', [], ...
    'latest_max_abs_delta', []);

experimentDataEachAvg = local_object_property(scan, 'ExperimentDataEachAvg', {});
if ~iscell(experimentDataEachAvg) || isempty(experimentDataEachAvg)
    return;
end

scanIndex = local_first_nonempty_average_scan(experimentDataEachAvg);
if isempty(scanIndex)
    averageSummary.warnings = {'ExperimentDataEachAvg did not contain a usable scan entry.'};
    return;
end

averageEntries = experimentDataEachAvg{scanIndex};
if ~iscell(averageEntries) || isempty(averageEntries)
    averageSummary.warnings = {'ExperimentDataEachAvg did not contain any completed averages.'};
    return;
end

averageSummary.available = true;
averageSummary.scan_index = scanIndex;
averageSummary.total_averages = numel(averageEntries);

recentLimit = averageSummary.recent_limit;
recentStart = max(1, averageSummary.total_averages - recentLimit + 1);
recentEntries = {};
for idx = recentStart:averageSummary.total_averages
    [entrySummary, ~, warningText] = local_average_entry_summary(averageEntries{idx}, idx);
    if ~isempty(warningText)
        averageSummary.warnings{end + 1} = warningText; %#ok<AGROW>
    end
    if isempty(fieldnames(entrySummary))
        continue;
    end
    if averageSummary.readout_count == 0
        averageSummary.readout_count = local_struct_field(entrySummary, 'readout_count', 0);
    end
    recentEntries{end + 1} = entrySummary; %#ok<AGROW>
end

averageSummary.recent_entries = recentEntries;
end

function scanIndex = local_first_nonempty_average_scan(experimentDataEachAvg)
scanIndex = [];
if ~iscell(experimentDataEachAvg)
    return;
end

for idx = 1:numel(experimentDataEachAvg)
    candidate = experimentDataEachAvg{idx};
    if iscell(candidate) && ~isempty(candidate)
        scanIndex = idx;
        return;
    end
end
end

function [entrySummary, signalValues, warningText] = local_average_entry_summary(avgEntry, averageIndex)
entrySummary = struct();
signalValues = [];
warningText = '';

if ~iscell(avgEntry) || isempty(avgEntry)
    warningText = sprintf('Average %d did not contain a usable readout cell.', averageIndex);
    return;
end

readoutValues = local_numeric_readout_values(avgEntry);
readoutCount = numel(readoutValues);
if readoutCount == 0
    warningText = sprintf('Average %d did not expose any numeric readout arrays.', averageIndex);
    return;
end

[signalValues, source, signalMeta] = local_average_signal_from_readouts(readoutValues);
if isempty(signalValues)
    warningText = sprintf('Average %d produced an empty derived signal.', averageIndex);
    return;
end

finiteSignalValues = signalValues(isfinite(signalValues));
if isempty(finiteSignalValues)
    warningText = sprintf('Average %d produced only non-finite derived values.', averageIndex);
    return;
end

zeroDenominatorCount = local_struct_field(signalMeta, 'zero_denominator_count', 0);
derivedContainsNonfinite = logical(local_struct_field(signalMeta, 'derived_contains_nonfinite', false));
rawContainsNonfinite = logical(local_struct_field(signalMeta, 'raw_contains_nonfinite', false));
if isempty(warningText) && derivedContainsNonfinite && zeroDenominatorCount > 0 && ~rawContainsNonfinite
    warningText = sprintf(['Average %d derived contrast hit %d zero-denominator point(s); ' ...
        'raw autosave readouts remained finite.'], averageIndex, zeroDenominatorCount);
end

entrySummary.average_index = averageIndex;
entrySummary.source = source;
entrySummary.readout_count = readoutCount;
entrySummary.num_points = numel(signalValues);
entrySummary.num_finite_points = numel(finiteSignalValues);
entrySummary.contains_nan = rawContainsNonfinite;
entrySummary.derived_contains_nonfinite = derivedContainsNonfinite;
entrySummary.zero_denominator_count = zeroDenominatorCount;
entrySummary.derived_signal_hidden = true;
entrySummary.hidden_derived_fields = {'y_values', 'y_preview', 'y_min', 'y_max', 'y_mean', 'y_std'};
entrySummary.readout_means = local_readout_means(readoutValues);
entrySummary.raw_readouts = local_readout_series_list(readoutValues);
end

function visible = local_agent_visible_signal_summary(signalSummary)
visible = struct();
visible.source = local_text_or(local_struct_field(signalSummary, 'source', ''), '');
visible.readout_count = local_struct_field(signalSummary, 'readout_count', []);
visible.discard_first_average = local_truthy(local_struct_field(signalSummary, 'discard_first_average', false));
visible.averages_used = local_struct_field(signalSummary, 'averages_used', []);
visible.num_points = local_struct_field(signalSummary, 'num_points', []);
visible.x_begin = local_struct_field(signalSummary, 'x_begin', []);
visible.x_end = local_struct_field(signalSummary, 'x_end', []);
visible.x_values = local_struct_field(signalSummary, 'x_values', []);
visible.x_preview = local_struct_field(signalSummary, 'x_preview', []);
visible.derived_signal_hidden = true;
visible.hidden_derived_fields = {'y_values', 'y_preview', 'y_min', 'y_max'};
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

function [signalValues, source, meta] = local_average_signal_from_readouts(readoutValues)
signalValues = [];
source = '';
meta = struct('zero_denominator_count', 0, 'derived_contains_nonfinite', false, ...
    'raw_contains_nonfinite', local_readout_values_contain_nonfinite(readoutValues));

readoutCount = numel(readoutValues);
if readoutCount == 1
    signalValues = readoutValues{1};
    source = 'average_single_readout_raw';
    meta.derived_contains_nonfinite = any(~isfinite(signalValues));
    return;
end

if readoutCount >= 3
    y0 = readoutValues{1};
    y1 = readoutValues{2};
    y2 = readoutValues{3};
    if numel(y0) == numel(y1) && numel(y1) == numel(y2)
        denominator = y0 - y1;
        meta.zero_denominator_count = sum(denominator == 0);
        signalValues = (y2 - y1) ./ denominator;
        meta.derived_contains_nonfinite = any(~isfinite(signalValues));
        source = 'average_3readout_contrast';
        return;
    end
end

if readoutCount >= 2
    y0 = readoutValues{1};
    y1 = readoutValues{2};
    if numel(y0) == numel(y1)
        meta.zero_denominator_count = sum(y0 == 0);
        signalValues = (y1 - y0) ./ y0;
        meta.derived_contains_nonfinite = any(~isfinite(signalValues));
        source = 'average_2readout_contrast';
    end
end
end

function tf = local_readout_values_contain_nonfinite(readoutValues)
tf = false;
if ~iscell(readoutValues)
    return;
end

for idx = 1:numel(readoutValues)
    readout = readoutValues{idx};
    if isnumeric(readout) && any(~isfinite(readout(:)))
        tf = true;
        return;
    end
end
end

function means = local_readout_means(readoutValues)
means = [];
if ~iscell(readoutValues) || isempty(readoutValues)
    return;
end

means = nan(1, numel(readoutValues));
for idx = 1:numel(readoutValues)
    values = readoutValues{idx};
    if isnumeric(values) && ~isempty(values)
        means(idx) = mean(values);
    end
end
end

function series = local_readout_series_list(readoutValues)
series = {};
if ~iscell(readoutValues)
    return;
end

for idx = 1:numel(readoutValues)
    values = readoutValues{idx};
    if ~isnumeric(values) || isempty(values)
        continue;
    end
    finiteValues = values(isfinite(values));
    item = struct();
    item.readout_index = idx;
    item.num_points = numel(values);
    item.values = reshape(double(values), 1, []);
    item.preview = local_preview_vector(values);
    if isempty(finiteValues)
        item.mean = NaN;
        item.std = NaN;
        item.min = NaN;
        item.max = NaN;
    else
        item.mean = mean(finiteValues);
        item.std = std(finiteValues);
        item.min = min(finiteValues);
        item.max = max(finiteValues);
    end
    series{end + 1} = item; %#ok<AGROW>
end
end

function numPoints = local_readout_num_points(readoutValues)
numPoints = 0;
if ~iscell(readoutValues) || isempty(readoutValues)
    return;
end

for idx = 1:numel(readoutValues)
    values = readoutValues{idx};
    if isnumeric(values) && ~isempty(values)
        numPoints = max(numPoints, numel(values));
    end
end
end

function warnings = local_readout_length_warnings(readoutValues, xValues, label)
warnings = {};
if ~iscell(readoutValues) || isempty(readoutValues) || isempty(xValues)
    return;
end

expectedCount = numel(xValues);
for idx = 1:numel(readoutValues)
    values = readoutValues{idx};
    if isnumeric(values) && ~isempty(values) && numel(values) ~= expectedCount
        warnings{end + 1} = sprintf('%s readout %d has %d point(s), not matching %d x_values.', ...
            label, idx, numel(values), expectedCount); %#ok<AGROW>
    end
end
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

function preview = local_preview_vector(values)
preview = [];
if ~isnumeric(values) || isempty(values)
    return;
end
preview = reshape(values(1:min(5, numel(values))), 1, []);
end

function values = local_name_value_list(rawValues)
values = {};
if isempty(rawValues) || ~iscell(rawValues)
    return;
end

for k = 1:numel(rawValues)
    entry = rawValues{k};
    if ~isstruct(entry) || ~isfield(entry, 'name') || ~isfield(entry, 'value')
        continue;
    end
    item = struct();
    item.name = local_text_or(entry.name, '');
    item.value = entry.value;
    values{end + 1} = item; %#ok<AGROW>
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

function tf = local_truthy(value)
tf = false;
if islogical(value)
    tf = any(value(:));
elseif isnumeric(value)
    tf = any(value(:) ~= 0);
end
end

function values = local_numeric_triplet(rawValue)
values = [];
if isempty(rawValue)
    return;
end
if iscell(rawValue)
    converted = nan(1, numel(rawValue));
    for k = 1:numel(rawValue)
        converted(k) = local_to_double(rawValue{k});
    end
    if numel(converted) >= 3 && all(isfinite(converted(1:3)))
        values = converted(1:3);
    end
    return;
end
if isnumeric(rawValue)
    rawValue = rawValue(:).';
    if numel(rawValue) >= 3
        values = double(rawValue(1:3));
    end
end
end

function out = local_to_double(value)
out = NaN;
if isnumeric(value) && isscalar(value)
    out = double(value);
elseif ischar(value) || (isstring(value) && isscalar(value))
    out = str2double(char(value));
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
