echo "Syncing into pyportal"

set dest=%1

xcopy .\*.py %dest% /S /Y
xcopy .\*.toml %dest% /S /Y
