.PHONY: download
download:
	gh repo list --limit 150 --json name,languages > data.json
