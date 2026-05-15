function [imageData, rangeX, rangeY, rangeZ, warnings, blockers] = claw_normalize_scan_image_axes(scan)
%CLAW_NORMALIZE_SCAN_IMAGE_AXES Normalize Imaging scan data to [Y X Z].
%
% The Imaging GUI can emit 3-D ImageData volumes with the z dimension in
% different positions depending on how the scan was produced. Downstream
% consumers expect rows=Y, cols=X, pages=Z, so normalize the scan volume to
% that layout using the scan range lengths as the source of truth.
%
% This function only changes axis order. It does not change pixel units.
% ConfocalScan.ImageData from the MATLAB Imaging GUI is already a count rate
% in kcps because ImagingFunctions.CalcCountRate converts APD counter
% differences before storing ImageData. Do not divide normalized ImageData by
% DwellTime to obtain kcps.

imageData = [];
rangeX = [];
rangeY = [];
rangeZ = [];
warnings = {};
blockers = {};

if nargin < 1 || isempty(scan)
    blockers{end + 1} = 'No scan object was provided.'; %#ok<AGROW>
    return;
end

imageData = local_object_property(scan, 'ImageData', []);
rangeX = local_row_vector(local_object_property(scan, 'RangeX', []));
rangeY = local_row_vector(local_object_property(scan, 'RangeY', []));
rangeZ = local_row_vector(local_object_property(scan, 'RangeZ', []));

if isempty(imageData) || ~isnumeric(imageData)
    blockers{end + 1} = 'Scan did not contain numeric ImageData.'; %#ok<AGROW>
    return;
end

imageData = double(imageData);
if ndims(imageData) <= 2
    return;
end

if ndims(imageData) ~= 3
    blockers{end + 1} = 'Scan had unsupported ImageData dimensionality.'; %#ok<AGROW>
    return;
end

sizeVec = size(imageData);
perm = local_infer_permutation(sizeVec, numel(rangeY), numel(rangeX), numel(rangeZ));
if isempty(perm)
    warnings{end + 1} = sprintf( ...
        'Could not infer scan ImageData axis order from size [%d %d %d] and range lengths X=%d Y=%d Z=%d; using raw ordering.', ...
        sizeVec(1), sizeVec(2), sizeVec(3), numel(rangeX), numel(rangeY), numel(rangeZ)); %#ok<AGROW>
    return;
end

if ~isequal(perm, [1 2 3])
    imageData = permute(imageData, perm);
    warnings{end + 1} = sprintf( ...
        'Reordered scan ImageData axes from [%d %d %d] to [%d %d %d] using permutation [%d %d %d].', ...
        sizeVec(1), sizeVec(2), sizeVec(3), size(imageData, 1), size(imageData, 2), size(imageData, 3), ...
        perm(1), perm(2), perm(3)); %#ok<AGROW>
end
end

function perm = local_infer_permutation(sizeVec, lenY, lenX, lenZ)
perm = [];
permsList = [1 2 3; 1 3 2; 2 1 3; 2 3 1; 3 1 2; 3 2 1];
target = [lenY lenX lenZ];
scores = inf(size(permsList, 1), 1);

for idx = 1:size(permsList, 1)
    candidate = permsList(idx, :);
    candidateSize = sizeVec(candidate);
    if local_matches_target(candidateSize, target)
        scores(idx) = local_permutation_score(candidate, sizeVec, target);
    end
end

[bestScore, bestIndex] = min(scores);
if isfinite(bestScore)
    perm = permsList(bestIndex, :);
end
end

function tf = local_matches_target(candidateSize, target)
tf = true;
for idx = 1:numel(target)
    if target(idx) > 0 && candidateSize(idx) ~= target(idx)
        tf = false;
        return;
    end
end
end

function score = local_permutation_score(candidate, sizeVec, target)
score = 0;
if isequal(candidate, [1 2 3])
    score = score - 0.25;
end
if target(3) > 1 && sizeVec(candidate(3)) == target(3)
    score = score - 1.0;
end
if target(1) == target(2) && candidate(1) < candidate(2)
    score = score - 0.1;
end
end

function value = local_object_property(obj, propertyName, fallback)
value = fallback;
if isempty(obj)
    return;
end
try
    value = obj.(propertyName);
catch
end
end

function row = local_row_vector(value)
if isnumeric(value)
    row = double(value(:).');
else
    row = [];
end
end
