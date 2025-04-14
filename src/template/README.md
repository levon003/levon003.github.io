Template
===

Install deps with `uv sync`.

To run tests:

```bash
uv run pytest
```

To play around with notebooks: 

```bash
uv run jupyter lab
```

To add dependencies:

```bash
uv add numpy
# or, for dev dependencies
uv add --group dev pytest
```
