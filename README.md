# VESEL

A tiny binary file format written in Python.

VESEL files store UTF-8 text data inside a custom binary container with magic number validation and versioning support.

This project was created to explore how file formats work under the hood by implementing one from scratch.

## Features

* Custom binary file format
* Magic number validation
* Version checking
* UTF-8 text storage
* Cross-platform file handling using pathlib
* Simple and extensible format design

## Quick Example
```bash
pip install vesel
```

```python
from vesel import VeselIO, Version, Header, VeselFile

file = VeselFile(
    header=Header(
        version=Version(0, 2, 2)
    ),
    payload=b"Hello World"
)

VeselIO.write(
    "hello.vesel",
    file
)

loaded = VeselIO.read(
    "hello.vesel"
)

print(
    loaded.payload.decode("utf-8")
)
```

## Project Structure

```text
vesel/
├── docs/
│   └── specifications.md
├── examples/
│   └── basic_usage.py
├── src/
│   └── vesel/
│       ├── __init__.py
│       ├── cli.py
│       ├── constants.py
│       ├── exceptions.py
│       ├── io.py
│       ├── models.py
│       └── utils.py
├── tests/
│   └── test_io.py
├── LICENSE
├── pyproject.toml
├── README.md
└── the-first.vesel
```

### Directory Overview

| Path | Purpose |
|--------|---------|
| `docs/` | Technical documentation and format specifications |
| `examples/` | Example programs demonstrating Vesel usage |
| `src/vesel/` | Main package source code |
| `tests/` | Automated test suite |
| `LICENSE` | Project license |
| `pyproject.toml` | Package configuration and build settings |
| `README.md` | Project overview and usage guide |
| `the-first.vesel` | First Vesel file created during development |

### Core Modules

| Module | Responsibility |
|----------|---------------|
| `models.py` | Data structures (`Version`, `Header`, `VeselFile`) |
| `io.py` | Serialization, deserialization, file reading and writing |
| `constants.py` | Format-wide constants such as magic bytes |
| `exceptions.py` | Custom Vesel exceptions |
| `utils.py` | Shared helper functions |
| `cli.py` | Command-line interface |
| `__init__.py` | Public package exports |
```

## Specification

The complete VESEL format specification can be found in:

```text
docs/specifications.md
```

## Why?

Most developers interact with file formats every day:

* ZIP
* PNG
* PDF
* MP3

VESEL exists as a learning project to understand how binary formats are structured, parsed, and versioned.

## Future Ideas

* Metadata support
* Multiple data sections
* Compression
* Encryption
* Archive/container support
* CLI tooling
* Formal specification revisions

## License

MIT License

---

"The first vessel is made."
