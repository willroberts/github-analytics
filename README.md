# github-analytics

A parser and analyzer for data produced by the Github CLI.

## Functionality

Download repository metadata with the `Makefile`. Saves to `data.json`:
```sh
make download
```
Interact with repository data via Python:
```python
opts = Options(exclude_private=True, exclude_forks=True)
repos = parse_repositories(opts)

count_languages(repos: list[Repository], count: int = 10)
count_primary_languages(repos: list[Repository], count: int = 10)
count_language_lines(repos: list[Repository], count: int = 10)
find_language_usage(repos: list[Repository], target_lang: str)
show_largest(repos: list[Repository], count: int = 10)
show_most_stars(repos: list[Repository], count: int = 10)
```
