.PHONY: download
download:
	gh repo list --limit 150 --json name,visibility,isFork,primaryLanguage,languages,stargazerCount,diskUsage > data.json
