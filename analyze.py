#!/usr/bin/env python3
import json
from collections import Counter

def count_languages(data: list, count: int) -> None:
    occurrences = list()
    for repo in data:
        for lang in repo['languages']:
            occurrences.append(lang['node']['name'])
    counter = Counter(occurrences)
    print('Most common programming languages:')
    for lang in counter.most_common(count):
        print(lang)

def count_primary_languages(data: list, count: int) -> None:
    occurrences = list()
    for repo in data:
        if repo['primaryLanguage'] is not None:
            occurrences.append(repo['primaryLanguage']['name'])
    counter = Counter(occurrences)
    print('Most common primary programming languages:')
    for lang in counter.most_common(count):
        print(lang)

def find_language_usage(data: list, target_lang: str) -> None:
    repos = list()
    for repo in data:
        for lang in repo['languages']:
            if lang['node']['name'] == target_lang:
                repos.append(repo['name'])
    for repo in repos:
        print(repo)

def show_largest(data: list, count: int) -> None:
    data = sorted(data, key=lambda r: r['diskUsage'], reverse=True)
    if count < len(data):
        data = data[:count]
    print('Largest repos:')
    for repo in data:
        print((repo['name'], repo['diskUsage']))

def show_most_stars(data: list, count: int) -> None:
    data = sorted(data, key=lambda r: r['stargazerCount'], reverse=True)
    if count < len(data):
        data = data[:count]
    print('Most starred repos:')
    for repo in data:
        print((repo['name'], repo['stargazerCount']))

if __name__ == '__main__':
    with open('data.json', 'r') as f:
        data = json.loads(f.read())
    count_primary_languages(data, 10)
    show_largest(data, 10)
