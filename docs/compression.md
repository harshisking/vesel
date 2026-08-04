# Compression

The `vesel.compression` module provides a simple, extensible compression framework for Vesel. Compression algorithms are implemented as subclasses of `Compressor` and are registered in a global registry, allowing them to be retrieved and used by name.

Built-in compressors are registered automatically when the module is imported, so no manual setup is required.

---

# Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Built-in Compressors](#built-in-compressors)
- [API Reference](#api-reference)
  - [Compressor](#compressor)
  - [register_compressor()](#register_compressor)
  - [get_compressor()](#get_compressor)
  - [registry](#registry)
- [Creating a Custom Compressor](#creating-a-custom-compressor)
- [Exceptions](#exceptions)

---

# Overview

The compression system is designed around three concepts:

- A common abstract base class (`Compressor`)
- A global compressor registry
- Automatically registered built-in compressors

Every compressor:

- Has a unique name.
- Accepts `bytes`.
- Returns `bytes`.
- Implements both compression and decompression.

---

# Quick Start

Import the compression module:

```python
from vesel.compression import get_compressor
```

Retrieve a compressor:

```python
compressor = get_compressor("gzip")
```

Compress data:

```python
data = b"Hello, Vesel!"

compressed = compressor.compress(data)
```

Decompress data:

```python
original = compressor.decompress(compressed)
```

---

# Built-in Compressors

## none

Performs no compression.

This compressor simply returns the original bytes unchanged.

Example:

```python
from vesel.compression import get_compressor

compressor = get_compressor("none")

data = b"Example"

compressed = compressor.compress(data)

assert compressed == data
```

---

## gzip

Uses Python's built-in `gzip` module.

Example:

```python
from vesel.compression import get_compressor

compressor = get_compressor("gzip")

compressed = compressor.compress(b"Hello")

original = compressor.decompress(compressed)
```

---

# API Reference

## Compressor

Abstract base class for all compression algorithms.

Every custom compressor must inherit from `Compressor`.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `name` | `str` | Unique compressor identifier. |

### Methods

#### compress(data)

Compresses raw bytes.

**Parameters**

| Name | Type |
|------|------|
| `data` | `bytes` |

**Returns**

```python
bytes
```

---

#### decompress(data)

Decompresses previously compressed bytes.

**Parameters**

| Name | Type |
|------|------|
| `data` | `bytes` |

**Returns**

```python
bytes
```

---

## register_compressor

Registers a compressor instance.

```python
register_compressor(compressor)
```

### Parameters

| Name | Type |
|------|------|
| `compressor` | `Compressor` |

### Raises

- `CompressorAlreadyExists`

Example:

```python
from vesel.compression import register_compressor

register_compressor(MyCompressor())
```

---

## get_compressor

Retrieves a registered compressor by name.

```python
compressor = get_compressor(name)
```

### Parameters

| Name | Type |
|------|------|
| `name` | `str` |

### Returns

```python
Compressor
```

### Raises

- `CompressorNotFoundError`

Example:

```python
compressor = get_compressor("gzip")
```

---

## registry

The global compressor registry.

Most users should use `register_compressor()` and `get_compressor()`, but the registry can also be accessed directly.

```python
from vesel.compression import registry
```

### Methods

#### register(compressor)

Registers a compressor.

#### get(name)

Returns the requested compressor.

#### exists(name)

Returns whether a compressor with the given name has been registered.

Example:

```python
if registry.exists("gzip"):
    print("Available")
```

---

# Creating a Custom Compressor

Create a subclass of `Compressor` and implement both required methods.

```python
from vesel.compression import Compressor

class ReverseCompressor(Compressor):

    name = "reverse"

    def compress(self, data: bytes) -> bytes:
        return data[::-1]

    def decompress(self, data: bytes) -> bytes:
        return data[::-1]
```

Register it:

```python
from vesel.compression import register_compressor

register_compressor(ReverseCompressor())
```

Retrieve and use it:

```python
from vesel.compression import get_compressor

compressor = get_compressor("reverse")

compressed = compressor.compress(b"Hello")

original = compressor.decompress(compressed)
```

---

# Exceptions

## CompressorAlreadyExists

Raised when attempting to register a compressor whose name is already registered.

Example:

```python
register_compressor(MyCompressor())
register_compressor(MyCompressor())
```

---

## CompressorNotFoundError

Raised when requesting a compressor that does not exist.

Example:

```python
get_compressor("lz4")
```

---

# Automatic Registration

The following compressors are automatically registered when `vesel.compression` is imported:

- `none`
- `gzip`

No manual registration is required for these built-in compressors.

---

# Example

```python
from vesel.compression import get_compressor

compressor = get_compressor("gzip")

data = b"Hello, World!"

compressed = compressor.compress(data)

original = compressor.decompress(compressed)

assert original == data
```