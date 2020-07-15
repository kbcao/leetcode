$date = Get-Date -Format 'yyyyMMdd-HH:mm:ss'

git add .
git commit -m "xjf-${date}"
git push