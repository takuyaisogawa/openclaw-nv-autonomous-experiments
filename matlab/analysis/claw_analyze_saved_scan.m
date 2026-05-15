function analysis = claw_analyze_saved_scan(request)
%CLAW_ANALYZE_SAVED_SCAN Analyze a saved Scan artifact and return fit/Aux-style outputs.
%
% request fields:
%   - result_path or data_path
%   - fit_kind (FitCW, FitRabi, FitFFT, FitHyperfine, FindMax, FindMin, CustomFunction)
%   - aux_key (optional)
%   - aux_slot (optional numeric; >4 implies discard first average to match NVautomizer)
%   - discard_first_average (optional logical override)
%   - custom_fit_function (optional for CustomFunction; function name or .m file path)
%   - custom_fit_path (optional additional folder/file to add to MATLAB path before feval)
%   - custom_fit_args (optional struct payload forwarded to the custom function)
%   - fit_label (optional fallback label for CustomFunction)

if nargin < 1
    request = struct();
end

analysis = struct();
analysis.ok = false;
analysis.result_path = '';
analysis.data_path = '';
analysis.sequence_name = '';
analysis.fit_kind = local_text_or(local_struct_field(request, 'fit_kind', 'None'), 'None');
analysis.fit = struct('ok', false, 'value', [], 'name', '', 'error', '');
analysis.aux_update = struct('ok', false, 'key', '', 'value', [], 'label', '', 'source', '');
analysis.signal = struct();
analysis.request = struct();
analysis.error_code = '';
analysis.error_message = '';
analysis.warnings = {};

try
    repoRoot = fileparts(fileparts(mfilename('fullpath')));
    addpath(fullfile(repoRoot, 'Analysis v8', 'Fitting'));
    addpath(fullfile(repoRoot, 'experiment', 'Functions'));

    requestSummary = struct();
    requestSummary.fit_kind = analysis.fit_kind;
    requestSummary.aux_key = local_text_or(local_struct_field(request, 'aux_key', ''), '');
    requestSummary.aux_slot = local_numeric_or(local_struct_field(request, 'aux_slot', []), []);
    requestSummary.discard_first_average = local_truthy(local_struct_field(request, 'discard_first_average', false));
    requestSummary.custom_fit_function = local_text_or(local_struct_field(request, 'custom_fit_function', ''), '');
    requestSummary.custom_fit_path = local_text_or(local_struct_field(request, 'custom_fit_path', ''), '');
    requestSummary.custom_fit_args = local_struct_field(request, 'custom_fit_args', struct());
    requestSummary.fit_label = local_text_or(local_struct_field(request, 'fit_label', ''), '');
    analysis.request = requestSummary;

    [resultPath, dataPath] = local_resolve_input_paths(request);
    analysis.result_path = resultPath;
    analysis.data_path = dataPath;

    loaded = load(dataPath, 'Scan');
    if ~isfield(loaded, 'Scan')
        error('NVClaw:MissingScan', 'Saved artifact did not contain a Scan variable.');
    end
    scan = loaded.Scan;

    analysis.sequence_name = local_text_or(local_object_property(scan, 'SequenceName', ''), '');

    [x, y, signalInfo] = local_extract_signal(scan, requestSummary);
    analysis.signal = signalInfo;

    fit = local_dispatch_fit(analysis.fit_kind, x, y, scan, requestSummary);
    analysis.fit = fit;

    auxKey = requestSummary.aux_key;
    if fit.ok && ~isempty(auxKey)
        analysis.aux_update = struct( ...
            'ok', true, ...
            'key', auxKey, ...
            'value', fit.value, ...
            'label', fit.name, ...
            'source', analysis.fit_kind);
    end

    analysis.ok = fit.ok;
catch ex
    analysis.ok = false;
    analysis.error_code = local_text_or(ex.identifier, 'NVClaw:AnalyzeSavedScanFailed');
    analysis.error_message = local_text_or(ex.message, 'Failed to analyze saved scan.');
    if isfield(analysis, 'fit') && isstruct(analysis.fit)
        analysis.fit.ok = false;
        analysis.fit.error = analysis.error_message;
    end
end
end

function [resultPath, dataPath] = local_resolve_input_paths(request)
resultPath = local_text_or(local_struct_field(request, 'result_path', ''), '');
dataPath = local_text_or(local_struct_field(request, 'data_path', ''), '');
repoRoot = fileparts(fileparts(mfilename('fullpath')));

if ~isempty(resultPath)
    if exist(resultPath, 'file') ~= 2
        error('NVClaw:MissingResultPath', 'Result JSON not found: %s', resultPath);
    end
    resultStruct = local_read_json_file(resultPath);
    if isempty(dataPath)
        dataPath = local_text_or(local_struct_field(resultStruct, 'data_path', ''), '');
    end
end

if isempty(dataPath)
    error('NVClaw:MissingDataPath', 'Either result_path or data_path is required.');
end

dataPath = local_resolve_repo_relative_data_path(dataPath, repoRoot);
if exist(dataPath, 'file') ~= 2
    error('NVClaw:MissingDataPath', 'Saved data artifact not found: %s', dataPath);
end
end

function [x, y, info] = local_extract_signal(scan, request)
experimentData = local_object_property(scan, 'ExperimentData', {});
if ~iscell(experimentData) || isempty(experimentData) || ~iscell(experimentData{1})
    error('NVClaw:MissingExperimentData', 'Scan.ExperimentData{1} was unavailable.');
end

experimentDataEachAvg = local_object_property(scan, 'ExperimentDataEachAvg', {});
discardFirst = local_truthy(local_struct_field(request, 'discard_first_average', false));
auxSlot = local_numeric_or(local_struct_field(request, 'aux_slot', []), []);
if ~discardFirst && ~isempty(auxSlot) && auxSlot > 4
    discardFirst = true;
end

readoutBlock = experimentData{1};
readoutCount = numel(readoutBlock);
if readoutCount == 1 && isnumeric(readoutBlock{1}) && numel(readoutBlock{1}) > 1
    y = readoutBlock{1};
    averagesUsed = 0;
    source = 'ExperimentData_flat';
elseif readoutCount > 2
    if discardFirst && local_can_use_each_avg(experimentDataEachAvg, 3)
        [y0, y1, y2, averagesUsed] = local_sum_each_avg(experimentDataEachAvg, 3);
        y = (y2 - y1) ./ (y0 - y1);
        source = 'ExperimentDataEachAvg_3readout_discard_first';
    else
        y = (readoutBlock{3} - readoutBlock{2}) ./ (readoutBlock{1} - readoutBlock{2});
        averagesUsed = 0;
        source = 'ExperimentData_3readout';
    end
else
    if discardFirst && local_can_use_each_avg(experimentDataEachAvg, 2)
        [y0, y1, ~, averagesUsed] = local_sum_each_avg(experimentDataEachAvg, 2);
        y = (y1 - y0) ./ y0;
        source = 'ExperimentDataEachAvg_2readout_discard_first';
    else
        y = (readoutBlock{2} - readoutBlock{1}) ./ readoutBlock{1};
        averagesUsed = 0;
        source = 'ExperimentData_2readout';
    end
end

x = local_scan_axis(scan, numel(y));
if numel(x) ~= numel(y)
    error('NVClaw:SignalLengthMismatch', 'x/y length mismatch while extracting saved scan signal.');
end

info = struct();
info.source = source;
info.readout_count = readoutCount;
info.discard_first_average = discardFirst;
info.averages_used = averagesUsed;
info.num_points = numel(x);
info.x_begin = x(1);
info.x_end = x(end);
info.y_min = min(y);
info.y_max = max(y);
info.x_values = reshape(x, 1, []);
info.y_values = reshape(y, 1, []);
info.x_preview = local_preview_vector(x);
info.y_preview = local_preview_vector(y);
end

function x = local_scan_axis(scan, nPoints)
varyBegin = local_first_numeric(local_object_property(scan, 'vary_begin', []), []);
varyEnd = local_first_numeric(local_object_property(scan, 'vary_end', []), []);
varyPoints = local_first_numeric(local_object_property(scan, 'vary_points', []), []);

if ~isempty(varyPoints) && varyPoints > 1 && ~isempty(varyBegin) && ~isempty(varyEnd)
    x = linspace(varyBegin, varyEnd, round(varyPoints));
elseif ~isempty(varyBegin) && ~isempty(varyEnd) && nPoints > 1
    x = linspace(varyBegin, varyEnd, nPoints);
else
    varyStep = local_first_numeric(local_object_property(scan, 'vary_step_size', []), []);
    if isempty(varyBegin) || isempty(varyStep)
        error('NVClaw:MissingScanAxis', 'Saved scan did not expose a usable x axis.');
    end
    x = varyBegin + (0:(nPoints - 1)) * varyStep;
end
end

function fit = local_dispatch_fit(fitKind, x, y, scan, request)
fit = struct('ok', false, 'value', [], 'name', '', 'error', '');
switch lower(strtrim(fitKind))
    case {'', 'none'}
        fit.ok = true;
        fit.name = 'No fit requested';
    case 'fitcw'
        [fit.value, fit.name] = local_fit_cw(x, y);
        fit.ok = true;
    case 'fitrabi'
        [fit.value, fit.name] = local_fit_rabi(x, y);
        fit.ok = true;
    case 'fitfft'
        [fit.value, fit.name] = local_fit_fft(x, y);
        fit.ok = true;
    case 'fithyperfine'
        [fit.value, fit.name] = local_fit_hyperfine(x, y);
        fit.ok = true;
    case 'findmax'
        [fit.value, fit.name] = local_find_max(x, y);
        fit.ok = true;
    case 'findmin'
        [fit.value, fit.name] = local_find_min(x, y);
        fit.ok = true;
    case 'customfunction'
        fit = local_run_custom_fit(x, y, scan, request);
    otherwise
        error('NVClaw:UnknownFitKind', 'Unsupported fit_kind: %s', fitKind);
end
end

function [out, name] = local_fit_cw(x, y)
myfun = @(c, xVal) c(4) - c(1) .* local_sinc((xVal - c(2)) / c(3)).^2;
gamma = (x(end) - x(1)) / 4;
cont = max(y) - min(y);
[~, idx] = min(y);
f = x(idx);
pinit = [cont, f, gamma, y(1) - myfun([cont, f, gamma, 0], x(1))];
LB = [-2, x(1), gamma / 1e4, -10];
UB = [2, x(end), gamma * 1e2, 10];
[pbest, ~] = easyfit(x, y, pinit, myfun, LB, UB);
out = round(pbest(2));
name = 'MW frequency(Hz)';
end

function [out, name] = local_fit_rabi(x, y)
myfun = @(c, xVal) c(3) + c(2) * cos(xVal * pi * c(1) + c(4)).^2;
phase = 0;
delta = abs(x(2) - x(1));
fs = 1 / delta;
l = length(x);
nfft = 2 * 2^nextpow2(l);
freq = fs / 2 * linspace(0, 1, nfft / 2 + 1);
yFft = fft(y - mean(y), nfft) / l;
dataY = abs(yFft(1:nfft / 2 + 1)).^2;
[~, idx] = max(dataY);
amp = max(y) - min(y);
rabi = freq(idx);
pinit = [rabi, amp, mean(y), phase];
LB = [0.8 * rabi, -2, -1, -pi];
UB = [1.2 * rabi, 2, 1, pi];
[pbest, ~] = easyfit(x, y, pinit, myfun, LB, UB);
out = round((1 / 2 - pbest(4) / pi) / pbest(1) / 1e-9) * 1e-9;
if out < 20e-9
    out = round((1 - pbest(4) / pi) / pbest(1) / 1e-9) * 1e-9;
end
name = 'pi pulse(s)';
end

function [out, name] = local_fit_fft(x, y)
myfun = @(c, xVal) c(4) - c(1) .* local_sinc((xVal - c(2)) / c(3)).^2;
gamma = (x(end) - x(1)) / 4;
cont = min(y) - max(y);
[~, idx] = max(y);
f = x(idx);
pinit = [cont, f, gamma, y(1) - myfun([cont, f, gamma, 0], x(1))];
LB = [-2, x(1), gamma / 1e4, -10];
UB = [2, x(end), gamma * 1e2, 10];
[pbest, ~] = easyfit(x, y, pinit, myfun, LB, UB);
out = round(pbest(2));
name = 'MW frequency(Hz)';
end

function [out, name] = local_fit_hyperfine(x, y)
myfun1 = @(c, xVal) -c(1) .* local_sinc((xVal - c(2)) / c(3)).^2;
myfun3 = @(c, xVal) myfun1([c(4), c(1), c(3)], xVal) + ...
    myfun1([c(5), c(1) + c(2), c(3)], xVal) + ...
    myfun1([c(6), c(1) + 2 * c(2), c(3)], xVal) + c(7);
cont = max(y) - min(y);
[~, idx] = min(y);
f = x(idx);
pinit = [f, 2.16e6, 1e6, cont, cont, cont, 0];
pinit(7) = y(1) - myfun3(pinit, x(1));
LB = [x(1), 2e6, 0.05e6, 0, 0, 0, -1.3];
UB = [x(end), 3e6, 10e6, 2, 2, 2, 1.2];
[pbest, ~] = easyfit(x, y, pinit, myfun3, LB, UB);
out = round(pbest(1));
name = 'MW frequency(Hz)';
end

function [out, name] = local_find_max(x, y)
[~, idx] = max(y);
out = x(idx);
name = 'max value';
end

function [out, name] = local_find_min(x, y)
[~, idx] = min(y);
out = x(idx);
name = 'min value';
end

function fit = local_run_custom_fit(x, y, scan, request)
functionRef = local_text_or(local_struct_field(request, 'custom_fit_function', ''), '');
if isempty(functionRef)
    error('NVClaw:MissingCustomFitFunction', 'CustomFunction requires custom_fit_function.');
end

additionalPath = local_text_or(local_struct_field(request, 'custom_fit_path', ''), '');
[functionName, pathsToAdd] = local_prepare_custom_fit_paths(functionRef, additionalPath);
for idx = 1:numel(pathsToAdd)
    addpath(pathsToAdd{idx});
end

customArgs = local_struct_field(request, 'custom_fit_args', struct());
rawResult = local_invoke_custom_fit(functionName, x, y, scan, request, customArgs);
fit = local_normalize_custom_fit_result(rawResult, request, functionName);
end

function [functionName, pathsToAdd] = local_prepare_custom_fit_paths(functionRef, additionalPath)
pathsToAdd = {};
[functionName, primaryPaths] = local_parse_custom_fit_reference(functionRef);
pathsToAdd = [pathsToAdd, primaryPaths];

if ~isempty(additionalPath)
    [~, extraPaths] = local_parse_custom_fit_reference(additionalPath);
    pathsToAdd = [pathsToAdd, extraPaths];
end

if isempty(functionName)
    error('NVClaw:MissingCustomFitFunction', 'Could not resolve a MATLAB function name for CustomFunction.');
end
end

function [functionName, pathsToAdd] = local_parse_custom_fit_reference(value)
pathsToAdd = {};
functionName = '';
text = strtrim(local_text_or(value, ''));
if isempty(text)
    return;
end

if exist(text, 'file') == 2
    [folderPath, baseName, ext] = fileparts(text);
    if strcmpi(ext, '.m')
        functionName = baseName;
        if ~isempty(folderPath)
            pathsToAdd = {folderPath};
        end
        return;
    end
end

if exist(text, 'dir') == 7
    pathsToAdd = {text};
    return;
end

if contains(text, filesep) || contains(text, '/') || contains(text, '\')
    [folderPath, baseName] = fileparts(text);
    functionName = baseName;
    if ~isempty(folderPath)
        pathsToAdd = {folderPath};
    end
    return;
end

functionName = text;
end

function fit = local_normalize_custom_fit_result(rawResult, request, functionName)
fit = struct('ok', false, 'value', [], 'name', '', 'error', '');
fallbackLabel = local_text_or(local_struct_field(request, 'fit_label', ''), '');
if isempty(fallbackLabel)
    fallbackLabel = functionName;
end

if isnumeric(rawResult) && isscalar(rawResult) && isfinite(rawResult)
    fit.ok = true;
    fit.value = double(rawResult);
    fit.name = fallbackLabel;
    return;
end

if isstruct(rawResult)
    if isfield(rawResult, 'ok')
        fit.ok = local_truthy(rawResult.ok);
    else
        fit.ok = true;
    end
    if isfield(rawResult, 'value')
        fit.value = rawResult.value;
    end
    if isfield(rawResult, 'name')
        fit.name = local_text_or(rawResult.name, fallbackLabel);
    elseif isfield(rawResult, 'label')
        fit.name = local_text_or(rawResult.label, fallbackLabel);
    else
        fit.name = fallbackLabel;
    end
    if isfield(rawResult, 'error')
        fit.error = local_text_or(rawResult.error, '');
    end
    if ~fit.ok && isempty(fit.error)
        fit.error = sprintf('CustomFunction %s returned ok=false.', functionName);
    end
    return;
end

error('NVClaw:InvalidCustomFitResult', ...
    'CustomFunction %s must return either a numeric scalar or a struct with at least value/name fields.', ...
    functionName);
end

function rawResult = local_invoke_custom_fit(functionName, x, y, scan, request, customArgs)
try
    rawResult = feval(str2func(functionName), x, y, scan, request, customArgs);
    return;
catch ex
    if ~local_is_argcount_error(ex)
        rethrow(ex);
    end
end

try
    rawResult = feval(str2func(functionName), x, y, scan, request);
    return;
catch ex
    if ~local_is_argcount_error(ex)
        rethrow(ex);
    end
end

try
    rawResult = feval(str2func(functionName), x, y, scan);
    return;
catch ex
    if ~local_is_argcount_error(ex)
        rethrow(ex);
    end
end

rawResult = feval(str2func(functionName), x, y);
end

function tf = local_is_argcount_error(ex)
identifier = lower(local_text_or(ex.identifier, ''));
message = lower(local_text_or(ex.message, ''));
tf = strcmp(identifier, 'matlab:minrhs') || ...
    strcmp(identifier, 'matlab:maxrhs') || ...
    strcmp(identifier, 'matlab:toomanyinputs') || ...
    contains(message, 'not enough input arguments') || ...
    contains(message, 'too many input arguments');
end

function tf = local_can_use_each_avg(experimentDataEachAvg, requiredReadouts)
tf = iscell(experimentDataEachAvg) && ~isempty(experimentDataEachAvg) && ...
    iscell(experimentDataEachAvg{1}) && numel(experimentDataEachAvg{1}) > 1 && ...
    iscell(experimentDataEachAvg{1}{2}) && numel(experimentDataEachAvg{1}{2}) >= requiredReadouts;
end

function [y0, y1, y2, averagesUsed] = local_sum_each_avg(experimentDataEachAvg, requiredReadouts)
y0 = [];
y1 = [];
y2 = [];
averagesUsed = 0;
for idx = 2:numel(experimentDataEachAvg{1})
    avgEntry = experimentDataEachAvg{1}{idx};
    if ~iscell(avgEntry) || numel(avgEntry) < requiredReadouts
        continue;
    end
    if isempty(y0)
        y0 = zeros(size(avgEntry{1}));
        y1 = zeros(size(avgEntry{2}));
        if requiredReadouts >= 3
            y2 = zeros(size(avgEntry{3}));
        else
            y2 = [];
        end
    end
    y0 = y0 + avgEntry{1};
    y1 = y1 + avgEntry{2};
    if requiredReadouts >= 3
        y2 = y2 + avgEntry{3};
    end
    averagesUsed = averagesUsed + 1;
end

if averagesUsed < 1
    error('NVClaw:MissingEachAverageData', 'ExperimentDataEachAvg did not contain enough averages to discard the first average.');
end
end

function text = local_text_or(value, defaultValue)
text = defaultValue;
if ischar(value)
    if ~isempty(value)
        text = value;
    end
elseif isstring(value) && isscalar(value) && strlength(value) > 0
    text = char(value);
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

function tf = local_truthy(value)
if islogical(value)
    tf = value;
elseif isnumeric(value)
    tf = value ~= 0;
elseif ischar(value) || (isstring(value) && isscalar(value))
    text = strtrim(char(value));
    tf = any(strcmpi(text, {'1', 'true', 'yes', 'on'}));
else
    tf = false;
end
end

function value = local_numeric_or(rawValue, defaultValue)
value = defaultValue;
if isnumeric(rawValue) && isscalar(rawValue) && isfinite(rawValue)
    value = double(rawValue);
elseif ischar(rawValue) || (isstring(rawValue) && isscalar(rawValue))
    parsed = str2double(char(rawValue));
    if isfinite(parsed)
        value = parsed;
    end
end
end

function value = local_first_numeric(rawValue, defaultValue)
value = defaultValue;
if isnumeric(rawValue) && ~isempty(rawValue)
    value = double(rawValue(1));
elseif iscell(rawValue) && ~isempty(rawValue) && isnumeric(rawValue{1}) && ~isempty(rawValue{1})
    value = double(rawValue{1}(1));
end
end

function preview = local_preview_vector(values)
count = min(numel(values), 5);
preview = values(1:count);
end

function values = local_sinc(x)
values = ones(size(x));
mask = abs(x) > eps;
values(mask) = sin(pi * x(mask)) ./ (pi * x(mask));
end

function payload = local_read_json_file(pathValue)
raw = fileread(pathValue);
if ~isempty(raw) && raw(1) == char(65279)
    raw = raw(2:end);
end
payload = jsondecode(raw);
end

function dataPath = local_resolve_repo_relative_data_path(dataPath, repoRoot)
if exist(dataPath, 'file') == 2
    return;
end

lowerPath = lower(dataPath);
marker = lower([filesep 'savedexperiments' filesep]);
idx = strfind(lowerPath, marker);
if isempty(idx)
    return;
end

suffix = dataPath((idx(1) + 1):end);
candidate = fullfile(repoRoot, suffix);
if exist(candidate, 'file') == 2
    dataPath = candidate;
end
end
