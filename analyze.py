#!/usr/bin/env python3
import json
from collections import Counter
from dataclasses import dataclass

@dataclass
class Language:
    name: str
    lines: int

@dataclass
class Repository:
    name: str
    stars: int
    disk_usage: int
    primary_language: str
    languages: list[Language]

def parse_data() -> list[Repository]:
    with open('data.json', 'r') as f:
        data = json.loads(f.read())
    return [
        Repository(
            d['name'],
            d['stargazerCount'],
            d['diskUsage'],
            d['primaryLanguage']['name'] if d['primaryLanguage'] else 'N/A',
            [Language(l['node']['name'], l['size']) for l in d['languages']],
        ) for d in data
    ]

def count_languages(repos: list[Repository], count: int = 10) -> None:
    c = Counter([lang.name for repo in repos for lang in repo.languages])
    print('Most common programming languages:')
    for lang in c.most_common(count):
        print(lang)

def count_primary_languages(repos: list[Repository], count: int = 10) -> None:
    c = Counter([r.primary_language for r in repos])
    print('Most common primary programming languages:')
    for lang in c.most_common(count):
        print(lang)

def count_language_lines(repos: list[Repository], count: int = 10) -> None:
    langs = [lang for repo in repos for lang in repo.languages]
    c = Counter({lang.name: lang.lines for lang in langs})
    print('Lines of code by language:')
    for lang, lines in c.most_common(count):
        print((lang, lines))

def find_language_usage(repos: list[Repository], target_lang: str) -> None:
    repos = [r.name for r in repos if r.primary_language == target_lang]
    print(f'Usage of programming language {target_lang}:')
    for repo in repos:
        print(repo)

def show_largest(repos: list[Repository], count: int = 10) -> None:
    repos = sorted(repos, key=lambda r: r.disk_usage, reverse=True)
    if count < len(repos):
        repos = repos[:count]
    print('Largest repositories:')
    for repo in repos:
        print((repo.name, repo.disk_usage))

def show_most_stars(repos: list[Repository], count: int = 10) -> None:
    repos = sorted(repos, key=lambda r: r.stars, reverse=True)
    if count < len(repos):
        repos = repos[:count]
    print('Most starred repositories:')
    for repo in repos:
        print((repo.name, repo.stars))

if __name__ == '__main__':
    data = parse_data()
    count_languages(data)
    print()
    count_primary_languages(data)
    print()
    count_language_lines(data)
    print()
    find_language_usage(data, 'Rust')
    print()
    show_largest(data)
    print()
    show_most_stars(data)
