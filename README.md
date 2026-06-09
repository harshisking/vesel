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

## Example

Writing a vessel:

```python
writer("message.vesel", "Hello World")
```

Reading a vessel:

```python
data = reader("message.vesel")
print(data)
```

Output:

```python
{
    'VERSION': 1,
    'DATA': 'Hello World'
}
```

## Project Structure

```text
vesel/
├── main.py
├── data/
│   └── the-first.vesel
├── docs/
│   └── specifications.md
└── README.md
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
