# Contributing

## What belongs here

- A public repository that is directly useful for computational mechanics: solid or structural mechanics, soft bodies, biomechanics, particle methods, or machine learning applied to them.
- General-purpose tools that computational mechanics work builds on, such as meshing, visualization, simulation languages and physics-informed learning libraries.
- A README or code that shows what it does.
- Not other general machine learning, trading, or programming resources.

## Adding or correcting an entry

1. Edit `data/repos.yml`. Do not edit `README.md` or `archive.md`, which are generated. Each entry is one line with all nine fields:

   ```yaml
   - {"url": "https://github.com/owner/repo", "category": "Virtual element method", "subtopic": "VEM libraries", "description": "What it does.", "language": "Python", "license": "MIT", "note": "", "status": "listed", "source": "topic"}
   ```

   `category` must match a topic title and `subtopic` one of that topic's sub-topic titles, both exactly and without the numbers, which are generated. To add a sub-topic, edit `TOPICS` in `scripts/check.py`. `status` is `listed` or `inactive`. End `description` with a period, but not `note`.
2. Write one factual sentence in your own words. Avoid "best", "fastest" and similar claims.
3. Copy the license from the repository, checking the license file, the README and source file headers. Use `none found` if there is none, and never guess.
4. Put required commercial software and usage restrictions in `note`.
5. Use status `inactive` for archived projects or ones their authors call unmaintained.
6. Set `source` to `major` for a widely used project. Every entry appears in the sub-topic named by its `category` and `subtopic`. Use `own` only for the maintainer's repositories, `stars` for the maintainer's stars, `related` for repositories found through related work, and `topic` for everything else.
7. GitHub, gitlab.com, gitlab.onelab.info and gitlab.dune-project.org URLs are supported. For an example inside a larger GitHub project, link to the file or folder.
8. Run `python3 scripts/check.py --write` (Python 3.9 or later). If you added or changed a URL, also run `python3 scripts/check.py --online`, which needs an authenticated `gh`: pull requests only check the data and generated files, and links are checked monthly. Then open a pull request.

By contributing, you release your contribution under [CC0 1.0](LICENSE). Linked projects keep their own licenses.
