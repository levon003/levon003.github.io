Stochtree Exploration
===

See <stochtree.ai>.

## Development

Installing `stochtree` on MacOS required me to:
 1. Download Xcode. For reasons that are not clear to me, neither my Developer Tools clang or my brew clang were sufficient.
 2. Clone the stochtree GitHub repo.
 3. Build with cmake.
 4. Install with pip. Not all of the steps below may be necessary.
 ```bash
uv venv --python 3.11  # newer versions of Python played badly with the deps frozen in requirements.txt
uv pip install -r requirements.txt
uv pip install .
 ```
 5. Add the directory of the cloned repo to tool.uv.sources in pyproject.toml.
 6. `uv add stochtree`

To play around with notebooks: `uv run jupyter lab`
