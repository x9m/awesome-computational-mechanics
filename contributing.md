# Contributing

## What belongs here

- A public repository that is directly useful for computational mechanics (solid or structural mechanics, soft bodies, biomechanics or particle methods), or for using machine learning, deep learning or large language models with simulation in mechanics or fluids. This covers surrogates, equation discovery, learned closures and solvers, coupling tools, flow control, agents, tool servers, datasets and benchmarks. General CFD codes are out unless they are built for use with machine learning.
- General-purpose tools that computational mechanics work builds on, such as solvers, meshing, visualization, simulation languages and physics-informed learning libraries.
- Material that helps make or judge a simulation: reference texts, verification cases, benchmarks, measured data, and calibration or uncertainty tools. Say in `note` when results could be mistaken for measured data or independent reference solutions.
- A README or code that shows what it does.
- Software needs readable source code in the repository: documentation, examples of calling it or binaries alone are not enough.
- Not other general machine learning, trading, or programming resources.

## Adding or correcting an entry

1. Edit `data/repos.yml`. Do not edit `README.md`, `archive.md` or the pages in `topics/`, which are generated. Each entry is one line with all nine fields:

   ```yaml
   - {"url": "https://github.com/owner/repo", "category": "Virtual element method", "subtopic": "VEM libraries", "description": "What it does.", "language": "Python", "license": "MIT", "note": "", "status": "listed", "maintainer": false}
   ```

   `category` must match a topic title and `subtopic` one of that topic's sub-topic titles, both exactly and without the numbers, which are generated. To add a sub-topic, edit `TOPICS` in `scripts/check.py`. To rename a topic, rename a sub-topic or move a sub-topic, also edit `FIRST_TITLES`, `FORMER_TITLES` or `MOVED` there, so old links keep working. To change a topic's introduction, edit `INTROS` there, and for the "Start here" table, edit `START`. `status` is `listed` or `inactive`. End `description` with a period, but not `note`.
2. Write one factual sentence in your own words. Avoid "best", "fastest" and similar claims.
3. Copy the license from the repository, checking the license file, the README and source file headers. Use `none found` if there is none, and never guess.
4. Put required commercial software and usage restrictions in `note`.
5. Use status `inactive` for archived projects or ones their authors call unmaintained.
6. Set `maintainer` to `true` only for the list maintainer's own repositories, which are marked as such. Use `false` for everything else.
7. GitHub, gitlab.com, gitlab.onelab.info and gitlab.dune-project.org URLs are supported. For an example inside a larger GitHub project, link to the file or folder, writing any `/` in the branch name as `%2F`.
8. Run `python3 scripts/check.py --write` (Python 3.9 or later). If you added or changed a URL, also run `python3 scripts/check.py --online`, which needs an authenticated `gh`: pull requests only check the data and generated files, and links, including those in descriptions, notes and introductions, are checked monthly. A warning means a link could not be checked by script, so open it in a browser. Then open a pull request.

By contributing, you release your contribution under [CC0 1.0](LICENSE). Linked projects keep their own licenses.

## For the maintainer

GitHub [disables scheduled workflows](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/disable-and-enable-workflows) in public repositories after 60 days without activity, so the monthly link check can stop. To restart and run it:

```sh
gh workflow enable check.yml
gh workflow run check.yml
```
