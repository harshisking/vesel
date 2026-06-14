import pytest

from vesel.exceptions import InvalidMagicError, InvalidPathError
from vesel.io import VeselIO
from vesel.models import Version, Header, VeselFile


def test_write_read_roundtrip(tmp_path):
    file = VeselFile(
        header=Header(),
        payload=b"Hello World"
    )

    path = tmp_path / "test.vesel"

    VeselIO.write(path, file)

    loaded = VeselIO.read(path)

    assert loaded.header.version == file.header.version
    assert loaded.payload == file.payload



def test_invalid_magic(tmp_path):
    path = tmp_path / "bad.vesel"

    path.write_bytes(
        b"ABCDE\x00\x01\x00hello"
    )

    with pytest.raises(InvalidMagicError):
        VeselIO.read(path)


def test_missing_file():
    with pytest.raises(InvalidPathError):
        VeselIO.read("does_not_exist.vesel")


def test_empty_payload(tmp_path):
    file = VeselFile(
        header=Header(),
        payload=b""
    )

    path = tmp_path / "empty.vesel"

    VeselIO.write(path, file)

    loaded = VeselIO.read(path)

    assert loaded.payload == b""


def test_binary_payload(tmp_path):
    payload = bytes([
        0,
        255,
        17,
        128,
        64
    ])

    file = VeselFile(
        header=Header(),
        payload=payload
    )

    path = tmp_path / "binary.vesel"

    VeselIO.write(path, file)

    loaded = VeselIO.read(path)

    assert loaded.payload == payload