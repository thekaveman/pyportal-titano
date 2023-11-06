echo "Syncing into pyportal"

dest="$1"
cp -r ./app ./*.py ./settings.toml "$dest"

echo "Done"
