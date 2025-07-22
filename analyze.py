#!/usr/bin/env python3
import json
from collections import Counter
from dataclasses import dataclass

@dataclass
class Options:
    exclude_private: bool = False
    exclude_forks: bool = False

@dataclass
class Language:
    name: str
    lines: int

@dataclass
class Repository:
    name: str
    visibility: str
    is_fork: bool
    stars: int
    disk_usage: int
    primary_language: str
    languages: list[Language]

def parse_repositories(opts: Options) -> list[Repository]:
    with open('data.json', 'r') as f:
        data = json.loads(f.read())
    repos = [
        Repository(
            d['name'],
            d['visibility'],
            d['isFork'],
            d['stargazerCount'],
            d['diskUsage'],
            d['primaryLanguage']['name'] if d['primaryLanguage'] else 'N/A',
            [Language(l['node']['name'], l['size']) for l in d['languages']],
        ) for d in data
    ]
    if opts.exclude_private:
        repos = [r for r in repos if r.visibility != "PRIVATE"]
    if opts.exclude_forks:
        repos = [r for r in repos if not r.is_fork]
    return repos

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
    repos = [repo.name for repo in repos for lang in repo.languages if lang.name == target_lang]
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
    opts = Options(exclude_private=True, exclude_forks=True)
    repos = parse_repositories(opts)

    count_languages(repos)
    print()
    count_primary_languages(repos)
    print()
    count_language_lines(repos)
    print()
    find_language_usage(repos, 'Rust')
    print()
    show_largest(repos)
    print()
    show_most_stars(repos)
