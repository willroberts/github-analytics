.PHONY: download
download:
	gh repo list --limit 150 --json name,isFork,primaryLanguage,languages,stargazerCount,diskUsage > data.json
