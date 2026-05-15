param(
    [Parameter(Mandatory = $true)]
    [string]$Source,

    [Parameter(Mandatory = $true)]
    [string]$Destination,

    [string[]]$OperatorNames = @()
)

$ErrorActionPreference = "Stop"

# Path account names are sanitized by generic path patterns below. Use
# -OperatorNames for free-text personal names that may appear outside paths.

$textExtensions = @(
    ".aux",
    ".cfg",
    ".csv",
    ".ini",
    ".json",
    ".jsonl",
    ".log",
    ".m",
    ".md",
    ".ps1",
    ".py",
    ".sh",
    ".stderr",
    ".stdout",
    ".tex",
    ".toml",
    ".tsv",
    ".txt",
    ".xml",
    ".yaml",
    ".yml"
)

$skipDirectoryNames = @(
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".venv",
    "__pycache__",
    "node_modules",
    "venv"
)

$skipExtensions = @(
    ".asv",
    ".bak",
    ".lock",
    ".m~",
    ".pyc",
    ".pyo",
    ".tmp"
)

$wslHomePattern = "[\\/]+wsl\.localhost[\\/]+[^\\/]+[\\/]+home[\\/]+[^\\/]+"
$posixHomePattern = "[\\/]+home[\\/]+[^\\/]+"
$mountedMatlabPattern = "[\\/]+mnt[\\/]+[A-Za-z][\\/]+[^\\/]+[\\/]+Documents[\\/]+MATLAB"
$windowsMatlabPattern = "[A-Za-z]:[\\/]+[^\\/]+[\\/]+Documents[\\/]+MATLAB"
$documentsPattern = "\b[^\\/\s]+[\\/]+Documents\b"

function Convert-ToPublicText {
    param([string]$Text)

    $out = $Text

    # Specific roots first, then broader fallbacks. The patterns intentionally
    # avoid local account, lab, and WSL distribution names.
    $out = $out -replace "(?i)$($wslHomePattern)[\\/]+openclaw_cold_archive", "<OPENCLAW_COLD_ARCHIVE>"
    $out = $out -replace "(?i)$($wslHomePattern)[\\/]+\.openclaw[\\/]+workspace", "<OPENCLAW_WORKSPACE>"
    $out = $out -replace "(?i)$($wslHomePattern)[\\/]+\.npm-global[\\/]+lib[\\/]+node_modules[\\/]+openclaw", "<OPENCLAW_PACKAGE_ROOT>"
    $out = $out -replace "(?i)$($wslHomePattern)", "<HOME>"

    $out = $out -replace "(?i)$($posixHomePattern)[\\/]+openclaw_cold_archive", "<OPENCLAW_COLD_ARCHIVE>"
    $out = $out -replace "(?i)$($posixHomePattern)[\\/]+\.openclaw[\\/]+workspace", "<OPENCLAW_WORKSPACE>"
    $out = $out -replace "(?i)$($posixHomePattern)[\\/]+\.npm-global[\\/]+lib[\\/]+node_modules[\\/]+openclaw", "<OPENCLAW_PACKAGE_ROOT>"
    $out = $out -replace "(?i)$($posixHomePattern)", "<HOME>"

    $out = $out -replace "(?i)$($mountedMatlabPattern)[\\/]+23-C", "<MATLAB_23C_ROOT>"
    $out = $out -replace "(?i)$($mountedMatlabPattern)[\\/]+nv_bridge", "<NV_BRIDGE_ROOT>"
    $out = $out -replace "(?i)$($mountedMatlabPattern)", "<MATLAB_ROOT>"

    $out = $out -replace "(?i)$($windowsMatlabPattern)[\\/]+23-C", "<MATLAB_23C_ROOT>"
    $out = $out -replace "(?i)$($windowsMatlabPattern)[\\/]+nv_bridge", "<NV_BRIDGE_ROOT>"
    $out = $out -replace "(?i)$($windowsMatlabPattern)", "<MATLAB_ROOT>"
    $out = $out -replace "(?i)$($documentsPattern)", "<LAB_DOCUMENTS>"

    $out = $out -replace "(?i)nv_bridge[\\/]+queue", "<NV_BRIDGE_QUEUE>"
    $out = $out -replace "(?i)\.openclaw[\\/]+workspace", "<OPENCLAW_WORKSPACE>"

    # Remove personal/operator and notification-service identifiers from public copies.
    foreach ($name in $OperatorNames) {
        $trimmed = $name.Trim()
        if ($trimmed) {
            $out = $out -replace ("(?i)\b" + [regex]::Escape($trimmed) + "\b"), "operator"
        }
    }
    $out = $out -replace "(?i)telegram", "notification_service"
    $out = $out -replace "(?i)slack", "notification_service"
    $out = $out -replace "(?i)whatsapp", "notification_service"

    # Conservative keyword redaction for records/logs. These are mostly logs and
    # metadata, so avoiding accidental credential-looking strings is worth the
    # small loss of cosmetic fidelity.
    $out = $out -replace "(?i)api[-_]?key", "api_auth_value"
    $out = $out -replace "(?i)chat[-_]?id", "notification_chat"
    $out = $out -replace "(?i)authorization", "authz_header"
    $out = $out -replace "(?i)credential", "auth_material"
    $out = $out -replace "(?i)password", "redacted_passphrase"
    $out = $out -replace "(?i)webhook", "notification_endpoint"
    $out = $out -replace "(?i)bearer", "auth_scheme"
    $out = $out -replace "(?i)cookie", "session_value"
    $out = $out -replace "(?i)private", "nonpublic"
    $out = $out -replace "(?i)secret", "redacted_value"
    $out = $out -replace "(?i)token", "usageunit"

    return $out
}

function Convert-ToPublicRelativePath {
    param([string]$RelativePath)

    $out = $RelativePath
    foreach ($name in $OperatorNames) {
        $trimmed = $name.Trim()
        if ($trimmed) {
            $out = $out -replace ("(?i)\b" + [regex]::Escape($trimmed) + "\b"), "operator"
        }
    }
    $out = $out -replace "(?i)api[-_]?key", "api_auth_value"
    $out = $out -replace "(?i)chat[-_]?id", "notification_chat"
    $out = $out -replace "(?i)authorization", "authz_header"
    $out = $out -replace "(?i)credential", "auth_material"
    $out = $out -replace "(?i)password", "redacted_passphrase"
    $out = $out -replace "(?i)webhook", "notification_endpoint"
    $out = $out -replace "(?i)bearer", "auth_scheme"
    $out = $out -replace "(?i)cookie", "session_value"
    $out = $out -replace "(?i)private", "nonpublic"
    $out = $out -replace "(?i)secret", "redacted_value"
    $out = $out -replace "(?i)token", "usageunit"
    $out = $out -replace "(?i)telegram", "notification_service"
    $out = $out -replace "(?i)slack", "notification_service"
    $out = $out -replace "(?i)whatsapp", "notification_service"
    return $out
}

function Test-ShouldSkip {
    param([string]$RelativePath)

    $segments = $RelativePath -split "[\\/]+"
    foreach ($segment in $segments) {
        if ($skipDirectoryNames -contains $segment) {
            return $true
        }
    }

    $leaf = Split-Path -Leaf $RelativePath
    foreach ($extension in $skipExtensions) {
        if ($leaf.EndsWith($extension, [System.StringComparison]::OrdinalIgnoreCase)) {
            return $true
        }
    }

    return $false
}

function Test-IsTextFile {
    param([string]$Path)

    $extension = [System.IO.Path]::GetExtension($Path).ToLowerInvariant()
    return $textExtensions -contains $extension
}

function Copy-RawOrSkip {
    param(
        [string]$SourceFile,
        [string]$TargetFile
    )

    try {
        Copy-Item -LiteralPath $SourceFile -Destination $TargetFile -Force
        $script:binary += 1
        return $true
    }
    catch {
        Write-Warning "Skipping unreadable or missing source file: $SourceFile"
        $script:skipped += 1
        return $false
    }
}

function Convert-ToLongPath {
    param([string]$Path)

    if ($Path.StartsWith("\\?\")) {
        return $Path
    }

    if ($Path.StartsWith("\\")) {
        return "\\?\UNC\" + $Path.TrimStart("\")
    }

    if ($Path -match "^[A-Za-z]:[\\/]") {
        return "\\?\" + $Path
    }

    return $Path
}

$resolvedSource = Resolve-Path -LiteralPath $Source
if ($resolvedSource.ProviderPath) {
    $sourcePath = (Convert-ToLongPath $resolvedSource.ProviderPath).TrimEnd("\", "/")
}
else {
    $sourcePath = (Convert-ToLongPath $resolvedSource.Path).TrimEnd("\", "/")
}
if ([System.IO.Path]::IsPathRooted($Destination)) {
    $destinationPath = Convert-ToLongPath ([System.IO.Path]::GetFullPath($Destination))
}
else {
    $destinationPath = Convert-ToLongPath ([System.IO.Path]::GetFullPath((Join-Path (Get-Location).Path $Destination)))
}

New-Item -ItemType Directory -Force -Path $destinationPath | Out-Null

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$copied = 0
$sanitized = 0
$binary = 0
$skipped = 0

Get-ChildItem -LiteralPath $sourcePath -Recurse -File -Force -ErrorAction SilentlyContinue | ForEach-Object {
    $sourceFile = $_.FullName
    $relativePath = $sourceFile.Substring($sourcePath.Length).TrimStart("\", "/")
    if (Test-ShouldSkip $relativePath) {
        $script:skipped += 1
        return
    }

    $publicRelativePath = Convert-ToPublicRelativePath $relativePath
    $targetPath = [System.IO.Path]::Combine($destinationPath, $publicRelativePath)
    $targetDirectory = [System.IO.Path]::GetDirectoryName($targetPath)
    New-Item -ItemType Directory -Force -Path $targetDirectory | Out-Null

    if (Test-IsTextFile $sourceFile) {
        try {
            $content = [System.IO.File]::ReadAllText($sourceFile)
            $publicContent = Convert-ToPublicText $content
            [System.IO.File]::WriteAllText($targetPath, $publicContent, $utf8NoBom)
            $script:sanitized += 1
        }
        catch {
            if (-not (Copy-RawOrSkip -SourceFile $sourceFile -TargetFile $targetPath)) {
                return
            }
        }
    }
    else {
        if (-not (Copy-RawOrSkip -SourceFile $sourceFile -TargetFile $targetPath)) {
            return
        }
    }

    $script:copied += 1
}

Write-Host "Source:      $sourcePath"
Write-Host "Destination: $destinationPath"
Write-Host "Copied:      $copied"
Write-Host "Sanitized:   $sanitized"
Write-Host "Binary/raw:  $binary"
Write-Host "Skipped:     $skipped"
