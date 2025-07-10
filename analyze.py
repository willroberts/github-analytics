#!/usr/bin/env python3
import json
from collections import Counter

def count_languages(data: list, count: int) -> None:
    occurrences = list()
    for repo in data:
        for lang in repo['languages']:
            occurrences.append(lang['node']['name'])
    counter = Counter(occurrences)
    for lang in counter.most_common(count):
        print(lang)

def find_usage(data: list, target: str) -> None:
    repos = list()
    for repo in data:
        for lang in repo['languages']:
            if lang['node']['name'] == target:
                repos.append(repo['name'])
    for repo in repos:
        print(repo)

if __name__ == '__main__':
    with open('data.json', 'r') as f:
        data = json.loads(f.read())
    print('COUNTING LANGUAGES')
    count_languages(data, 15)
