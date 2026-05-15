addpath(genpath('<MATLAB_23C_ROOT>'));
path = '<MATLAB_23C_ROOT>\SavedImages\3DXYZ-Image-2026-05-13-145844.mat';
vars = whos('-file', path);
fprintf('WHOS\n');
for i=1:numel(vars)
  fprintf('%s class=%s size=%s\n', vars(i).name, vars(i).class, mat2str(vars(i).size));
end
S = load(path);
fns = fieldnames(S);
fprintf('FIELDS %s\n', strjoin(fns',','));
for i=1:numel(fns)
  name=fns{i}; obj=S.(name);
  fprintf('VAR %s class=%s size=%s\n', name, class(obj), mat2str(size(obj)));
  try
    props = properties(obj);
    fprintf('PROPS %s\n', strjoin(props',','));
    for j=1:numel(props)
      p=props{j};
      try
        v=obj.(p);
        fprintf('PROP %s class=%s size=%s', p, class(v), mat2str(size(v)));
        if isnumeric(v) || islogical(v)
          vv=double(v(:)); vv=vv(isfinite(vv));
          if isempty(vv), fprintf(' empty'); else, fprintf(' min=%g max=%g first=', min(vv), max(vv)); fprintf('%g ', vv(1:min(8,end))); end
        elseif ischar(v) || isstring(v)
          fprintf(' value=%s', char(string(v)));
        elseif iscell(v)
          fprintf(' cell_len=%d', numel(v));
        end
        fprintf('\n');
      catch ME
        fprintf('PROPERR %s %s\n', p, ME.message);
      end
    end
  catch ME
    fprintf('NO_PROPS %s\n', ME.message);
  end
end
