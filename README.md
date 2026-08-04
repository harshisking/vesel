# VESEL
> [!WARNING]
> VESEL is currently in active development and has not yet reached version 1.0.0. The file format and public APIs may change between releases.
A binary file format and Python library for storing arbitrary byte payloads in a custom binary container.

VESEL provides magic number validation, versioning support, and pluggable compression while remaining lightweight and easy to understand.

This project was created to explore how file formats work under the hood by implementing one from scratch.

## Features

* Custom binary container format
* Magic number validation
* Versioned files
* Arbitrary byte payloads
* Compression support
* Plugin architecture
* Cross-platform
* Tested

## Installation

```bash
pip install vesel
```
## Quick Example

```python
import vesel

vesel.write(path="example.vesel",payload=b"Lorem Ipsum",compression_name="none")

loaded = vesel.read("example.vesel")
print(loaded.payload.decode("utf-8"))
```
## Compression

VESEL includes built-in support for gzip compression.

```python
vesel.write(
    path="example.vesel",
    payload=b"Lorem Ipsum",
    compression_name="gzip"
)
```

For the complete compression specification, see:
```text
docs/compression.md
```

## File Format Overview

A VESEL file consists of four main components:

1. **Magic Number** – Identifies the file as a valid VESEL file.
2. **Version Information** – Stores the format version used to create the file.
3. **Compression Metadata** – Stores the name of the compression algorithm used for the payload.
4. **Payload** – The raw binary data contained within the file.

VESEL stores payloads as arbitrary bytes and does not impose any restrictions on the content. Applications are responsible for interpreting the payload data.

A simplified layout is shown below:

```text
+--------------------+
| Magic Number       |
+--------------------+
| Format Version     |
+--------------------+
| Compression Info   |
+--------------------+
| Payload Length     |
+--------------------+
| Payload            |
+--------------------+
```

For the complete binary specification, see:

```text
docs/specifications.md
```

## Project Goals

VESEL was created as a learning project to explore how binary file formats are designed and implemented.

The project aims to provide a simple and readable codebase that demonstrates concepts such as:

* Binary serialization and deserialization
* File format design
* Versioning and compatibility
* Data validation using magic numbers
* Extensible architectures through plugins
* Automated testing and maintainability

VESEL is intentionally lightweight and focuses on clarity and experimentation rather than competing with established formats such as ZIP, TAR, or database storage systems.

The long-term goal is to evolve VESEL into a stable, well-documented format while preserving its educational value.

## Specification

The complete VESEL format specification can be found in:

```text
docs/specifications.md
```

## Stability

VESEL is currently in active development.

The project has not yet reached version 1.0.0, which means the file format, APIs, and internal implementation may change between releases.

Compatibility guarantees will be introduced once the format reaches a stable 1.x release.


## Roadmap

* Metadata support
* Multiple data sections
* Encryption
* Archive/container support
* CLI tooling
* Formal specification revisions

## License

MIT License

---

"The first vessel has been made."
