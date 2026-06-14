import pytest

from vesel.exceptions import InvalidMagicError, InvalidPathError
from vesel.io import VeselIO
from vesel.models import Version, Header, VeselFile
from vesel.compression import *
from vesel.compression.exceptions import *


class TestCompressor(Compressor):
    name="test"

    def compress(self,data):
        return data
    
    def decompress(self,data):
        return data
    

def test_get_unknown_compressor_raises():
    with pytest.raises(CompressorNotFoundError):
        get_compressor("zip")

def test_register_compressor():
    register_compressor(TestCompressor())
    assert get_compressor("test").name == "test"

def test_duplicate_compressor():
    with pytest.raises(CompressorAlreadyExists):
        register_compressor(TestCompressor())

def test_gzip_roundtrip():
    compressor = get_compressor('gzip')
    original = b"Hello World!"

    compressed = compressor.compress(data=original)
    decompressed = compressor.decompress(data=compressed)
    
    assert original == decompressed
