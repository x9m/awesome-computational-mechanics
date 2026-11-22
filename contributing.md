# Contributing

## What belongs here

- A public repository that is directly useful for mechanical simulation: solid or structural mechanics, soft bodies, biomechanics, particle methods, or machine learning applied to them.
- A README or code that shows what it does.
- Not general machine learning, trading, or programming resources.

## Adding or correcting an entry

1. Edit `data/repos.yml`. Do not edit `README.md` or `archive.md`, which are generated.
2. Write one factual sentence in your own words. Avoid "best", "fastest" and similar claims.
3. Copy the license from the repository. Use `none found` if there is none, and never guess.
4. Put required commercial software and usage restrictions in `note`.
5. Use status `inactive` for archived projects or ones their authors call unmaintained.
6. Run `python3 scripts/check.py --write` (Python 3.9 or later), then open a pull request.

By contributing, you release your contribution under [CC0 1.0](LICENSE). Linked projects keep their own licenses.
