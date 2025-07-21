.PHONY: download
download:
	gh repo list --limit 150 --json name,primaryLanguage,languages,stargazerCount,diskUsage > data.json
