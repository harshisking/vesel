# VESEL Format Specification

Version: 1.0

Status: Draft

## 1. Introduction

VESEL is a lightweight binary file format designed to store UTF-8 encoded textual data.

The format is intentionally minimal and serves as a learning implementation of binary file format design.

## 2. Terminology

* MUST: Required for compliance.
* SHOULD: Recommended but not required.
* MAY: Optional.

## 3. File Structure

A Version 1 VESEL file consists of three sections:

| Offset | Length          | Description           |
| ------ | --------------- | --------------------- |
| 0      | 5 bytes         | Magic Number          |
| 5      | 1 byte          | Format Version        |
| 6      | Remaining Bytes | UTF-8 Encoded Payload |

## 4. Magic Number

The first five bytes of every VESEL file MUST contain:

```text
VESEL
```

Hexadecimal representation:

```hex
56 45 53 45 4C
```

Readers MUST reject files whose magic number does not match.

## 5. Version Field

The version field occupies one byte immediately following the magic number.

Current version:

```text
1
```

Hexadecimal representation:

```hex
01
```

Readers SHOULD reject unsupported versions.

## 6. Payload

All bytes following the version field are interpreted as UTF-8 encoded text.

Example payload:

```text
THE FIRST VESSEL IS MADE!
```

Readers MUST decode the payload using UTF-8.

## 7. Example File

Payload:

```text
Hello World
```

Binary Layout:

```text
VESEL
01
Hello World
```

Hexadecimal Representation:

```hex
56 45 53 45 4C
01
48 65 6C 6C 6F 20 57 6F 72 6C 64
```

## 8. Compliance Requirements

A valid Version 1 VESEL file MUST:

1. Begin with the magic number `VESEL`.
2. Contain a supported version byte.
3. Contain a UTF-8 payload.

## 9. Future Compatibility

Future versions MAY introduce:

* Metadata sections
* Payload length fields
* Multiple data blocks
* Compression
* Encryption
* Archive/container functionality

Version changes SHOULD preserve backward compatibility whenever possible.

---

End of Specification.
