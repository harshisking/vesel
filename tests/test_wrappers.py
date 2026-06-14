import vesel
import pytest

def test_write_read_round_trip(tmp_path):
    path = tmp_path/"test.vesel"
    payload = b"Hello World"
    vesel.write(path,payload)

    loaded = vesel.read(path)
    assert loaded.header.payload_length == len(payload)
    assert loaded.payload == payload
    assert loaded.header.version == vesel.Version(0,2,2)

def test_compression_write_read_round_trip(tmp_path):
    path = tmp_path/"test.vesel"
    payload = b"Hello World"
    vesel.write(path,payload,"gzip")

    loaded = vesel.read(path)

    assert loaded.header.compression == "gzip"
    assert loaded.payload == payload
    assert loaded.header.payload_length == len(payload)
    assert loaded.header.version == vesel.Version(0,2,2)

def test_invalid_magic(tmp_path):
    path = tmp_path / "bad.vesel"

    path.write_bytes(
        b"ABCDE\x00\x01\x00hello"
    )

    with pytest.raises(vesel.InvalidMagicError):
        vesel.read(path)


def test_missing_file():
    with pytest.raises(vesel.exceptions.InvalidPathError):
        vesel.read("does_not_exist.vesel")

def test_empty_payload(tmp_path):
    path = tmp_path/'empty.vesel'
    vesel.write(path,b"")
    loaded = vesel.read(path)
    assert loaded.payload == b""

def test_compression_empty_payload(tmp_path):
    path = tmp_path/'empty.vesel'
    vesel.write(path,b"","gzip")
    loaded = vesel.read(path)
    assert loaded.payload == b""

def test_readjson(tmp_path):
    path = tmp_path/"test.vesel"
    vesel.write(path,b"Test Hello")
    loaded = vesel.readjson(path)
    assert type(loaded) is dict
    assert loaded["Header"]["Payload_length"]==len(b"Test Hello")
    assert loaded["Payload"] == b"Test Hello"

def test_compression_readjson(tmp_path):
    path = tmp_path/"test.vesel"
    vesel.write(path,b"Test Hello","gzip")
    loaded = vesel.readjson(path)
    assert type(loaded) is dict
    assert loaded["Payload"] == b"Test Hello"
    assert loaded["Header"]["Payload_length"]==len(b"Test Hello")