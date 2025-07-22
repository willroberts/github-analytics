#!/usr/bin/env python3
import json
from collections import Counter
from dataclasses import dataclass

@dataclass
class Options:
    '''
    Options influences the behavior of the parser, allowing it to filter some repository types.
    '''
    exclude_private: bool = False
    exclude_forks: bool = False

@dataclass
class Language:
    '''
    Language represents an occurrence of a programming language within a Repository, including
    the number of lines of code present in that repository.
    '''
    name: str
    lines: int

@dataclass
class Repository:
    '''
    Repository represents a Github source code repository.
    '''
    name: str
    visibility: str
    is_fork: bool
    stars: int
    disk_usage: int
    primary_language: str
    languages: list[Language]

def parse_repositories(opts: Options) -> list[Repository]:
    '''
    Reads a Github API response from data.json, parsing it into local types.
    Raises FileNotFoundError if data.json is missing.
    '''
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
    '''
    Prints the top `count` languages for all occurrences of languages across repositories.
    '''
    c = Counter([lang.name for repo in repos for lang in repo.languages])
    print('Most common programming languages:')
    for lang in c.most_common(count):
        print(lang)

def count_primary_languages(repos: list[Repository], count: int = 10) -> None:
    '''
    Prints the top `count` languages for the primary language among repositories.
    '''
    c = Counter([r.primary_language for r in repos])
    print('Most common primary programming languages:')
    for lang in c.most_common(count):
        print(lang)

def count_language_lines(repos: list[Repository], count: int = 10) -> None:
    '''
    Prints the top `count` languages by lines of code.
    '''
    c = Counter()
    for lang in [lang for repo in repos for lang in repo.languages]:
        c.update({lang.name: lang.lines})
    print('Lines of code by language:')
    for lang, lines in c.most_common(count):
        print((lang, lines))

def find_language_usage(repos: list[Repository], target_lang: str) -> None:
    '''
    Prints repository names which use the given `target_lang`.
    '''
    repos = [repo.name for repo in repos for lang in repo.languages if lang.name == target_lang]
    print(f'Usage of programming language {target_lang}:')
    for repo in repos:
        print(repo)

def show_largest(repos: list[Repository], count: int = 10) -> None:
    '''
    Prints the top `count` repositories by disk usage.
    '''
    repos = sorted(repos, key=lambda r: r.disk_usage, reverse=True)
    if count < len(repos):
        repos = repos[:count]
    print('Largest repositories:')
    for repo in repos:
        print((repo.name, repo.disk_usage))

def show_most_stars(repos: list[Repository], count: int = 10) -> None:
    '''
    Prints the top `count` languages by stargazer count.
    '''
    repos = sorted(repos, key=lambda r: r.stars, reverse=True)
    if count < len(repos):
        repos = repos[:count]
    print('Most starred repositories:')
    for repo in repos:
        print((repo.name, repo.stars))

if __name__ == '__main__':
    opts = Options(exclude_private=True, exclude_forks=True)
    try:
        repos = parse_repositories(opts)
    except Exception as e:
        print('Error:', str(e))
        print('Failed to read data.json; did you run `make download`?')
        exit(1)

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
