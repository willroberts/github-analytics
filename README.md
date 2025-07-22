# github-analytics

Playing around with data produced by the Github CLI.

## Functionality

```python
count_languages(repos: list[Repository], exclude_private: bool = False, exclude_forks: bool = False, count: int = 10) -> None
count_primary_languages(repos: list[Repository], exclude_private: bool = False, exclude_forks: bool = False, count: int = 10) -> None
count_language_lines(repos: list[Repository], exclude_private: bool = False, exclude_forks: bool = False, count: int = 10) -> None
find_language_usage(repos: list[Repository], target_lang: str, exclude_private: bool = False, exclude_forks: bool = False) -> None
show_largest(repos: list[Repository], exclude_private: bool = False, exclude_forks: bool = False, count: int = 10) -> None
show_most_stars(repos: list[Repository], exclude_private: bool = False, exclude_forks: bool = False, count: int = 10) -> None
```
