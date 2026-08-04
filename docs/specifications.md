# VESEL Format Specification

**Version:** 0.3.0

**Status:** Draft

---

# 1. Introduction

VESEL is a lightweight binary file format designed to store arbitrary binary data.

The format is intentionally minimal and serves as a learning implementation of binary file format design. VESEL makes no assumptions about the contents of the payload and may store text, images, serialized objects, or any other binary data.

Beginning with Version **0.3.0**, every VESEL file stores the compression algorithm used to encode the payload. This allows readers to automatically determine how the payload should be decompressed.

---

# 2. Terminology

- **MUST** — Required for compliance.
- **SHOULD** — Recommended but not required.
- **MAY** — Optional.

---

# 3. File Structure

A Version **0.3.0** VESEL file consists of the following sections:

| Offset | Length | Description |
|--------:|-------:|-------------|
| 0 | 5 bytes | Magic Number |
| 5 | 1 byte | Major Version |
| 6 | 1 byte | Minor Version |
| 7 | 1 byte | Patch Version |
| 8 | 1 byte | Compression Name Length |
| 9 | N bytes | Compression Name (UTF-8) |
| 9 + N | 4 bytes | Payload Length |
| 13 + N | Payload Length bytes | Payload |

The header is therefore variable in size depending on the length of the compression name.

---

# 4. Magic Number

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

# 5. Version

The version immediately follows the magic number and consists of three unsigned one-byte integers.

| Byte | Description |
|------|-------------|
| 5 | Major Version |
| 6 | Minor Version |
| 7 | Patch Version |

Current format version:

```text
0.3.0
```

Encoded as:

```hex
00 03 00
```

Readers SHOULD reject unsupported versions.

---

# 6. Compression Name Length

The Compression Name Length field is a single unsigned byte specifying the number of bytes used by the Compression Name field.

The maximum supported compression name length is **255 bytes**.

---

# 7. Compression Name

The Compression Name field stores the name of the compression algorithm used for the payload.

The value MUST be encoded using UTF-8.

Examples include:

```text
none
gzip
```

Readers SHOULD use this value to determine which decompression algorithm should be applied to the payload.

---

# 8. Payload Length

The Payload Length field immediately follows the Compression Name field.

It is stored as an unsigned four-byte integer.

Unless otherwise specified, the integer MUST be stored using big-endian byte order.

The value specifies the exact size of the payload in bytes.

---

# 9. Payload

The Payload field contains the binary data stored within the VESEL file.

If compression is used, this field contains the compressed representation of the original data.

The VESEL format does not define the meaning of the payload itself.

Examples include:

- UTF-8 text
- Images
- Serialized objects
- Arbitrary binary data

Applications are responsible for interpreting the payload after decompression.

---

# 10. Example File

Payload:

```text
Hello World
```

Compression:

```text
none
```

Binary Layout:

```text
Magic
HBVSL

Version
00 03 00

Compression Length
04

Compression
none

Payload Length
00 00 00 0B

Payload
Hello World
```

Hexadecimal Representation:

```hex
48 42 56 53 4C
00 03 00
04
6E 6F 6E 65
00 00 00 0B
48 65 6C 6C 6F 20 57 6F 72 6C 64
```

---

# 11. Compliance Requirements

A valid VESEL Version **0.3.0** file MUST:

1. Begin with the magic number `HBVSL`.
2. Contain three version bytes.
3. Contain a Compression Name Length field.
4. Contain a UTF-8 encoded Compression Name.
5. Contain a Payload Length field.
6. Contain exactly the specified number of payload bytes.
7. Use a supported format version.

---

# 12. Future Compatibility

Future versions MAY introduce:

- Additional metadata fields
- Checksums
- Encryption
- Archive/container functionality
- Extended header fields

Applications SHOULD reject unsupported major versions unless compatibility is explicitly provided.

---

End of Specification.