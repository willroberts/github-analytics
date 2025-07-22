# github-analytics

Playing around with data produced by the Github CLI.

## Functionality

```python
opts = Options(exclude_private=True, exclude_forks=True)
repos = parse_repositories()

count_languages(repos: list[Repository], opts: Options, count: int = 10) -> None
count_primary_languages(repos: list[Repository], opts: Options, count: int = 10) -> None
count_language_lines(repos: list[Repository], opts: Options, count: int = 10) -> None
find_language_usage(repos: list[Repository], target_lang: str, opts: Options) -> None
show_largest(repos: list[Repository], opts: Options, count: int = 10) -> None
show_most_stars(repos: list[Repository], opts: Options, count: int = 10) -> None
```
