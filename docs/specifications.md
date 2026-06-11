# VESEL Format Specification

Version: 0.2.2

Status: Draft

## 1. Introduction

VESEL is a lightweight binary file format designed to store arbitrary binary data.

The format is intentionally minimal and serves as a learning implementation of binary file format design. VESEL makes no assumptions about the contents of the payload and may store text, images, serialized objects, or any other binary data.

---

## 2. Terminology

* MUST: Required for compliance.
* SHOULD: Recommended but not required.
* MAY: Optional.

---

## 3. File Structure

A Version 0.2.2 VESEL file consists of three sections:

| Offset | Length          | Description   |
| ------ | --------------- | ------------- |
| 0      | 5 bytes         | Magic Number  |
| 5      | 1 byte          | Major Version |
| 6      | 1 byte          | Minor Version |
| 7      | 1 byte          | Patch Version |
| 8      | 4 bytes         | Payload length|
| 12     | N Bytes         | Payload       |

---

## 4. Magic Number

The first five bytes of every VESEL file MUST contain:

```text
HBVSL
```

Hexadecimal representation:

```hex
48 42 56 53 4C
```

Readers MUST reject files whose magic number does not match.

---

## 5. Version Fields

The version immediately follows the magic number and consists of three one-byte unsigned integers:

| Byte | Description   |
| ---- | ------------- |
| 5    | Major Version |
| 6    | Minor Version |
| 7    | Patch Version |

Current format version:

```text
0.2.2
```

Encoded as:

```hex
00 02 02
```

Readers SHOULD reject unsupported versions.

---
## 6. Payload Length

The Payload Length field follows the Version field. It represents the length of the payload, in bytes, encoded as a four-byte unsigned integer.

The value specifies the exact number of bytes that make up the payload section of the file.

Unless otherwise specified, the integer MUST be stored in big-endian byte order.

---

## 7. Payload

All bytes following the version fields are interpreted as payload data.

The VESEL format does not define the meaning of the payload.

Examples include:

* UTF-8 text
* Images
* Serialized objects
* Compressed data
* Arbitrary binary data

Readers SHOULD interpret the payload according to the application's requirements.

---

## 8. Example File

Payload:

```text
Hello World
```

Binary Layout:

```text
HBVSL
00 02 02
Hello World
```

Hexadecimal Representation:

```hex
48 42 56 53 4C
00 02 02
48 65 6C 6C 6F 20 57 6F 72 6C 64
```

---

## 9. Compliance Requirements

A valid VESEL Version 0.1.0 file MUST:

1. Begin with the magic number `HBVSL`.
2. Contain three version bytes.
3. Contain a payload section.
4. Use a supported format version.

---

## 10. Future Compatibility

Future versions MAY introduce:

* Metadata sections
* Payload length fields
* Multiple data blocks
* Compression
* Checksums
* Encryption
* Archive/container functionality

Version changes SHOULD preserve backward compatibility whenever possible.

---

End of Specification.
