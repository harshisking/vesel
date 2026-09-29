import gzip

from .compressor import Compressor

class NoneCompressor(Compressor):
    name = "none"

    def compress(self,data:bytes)->bytes:
        return data
    
    def decompress(self, data: bytes) -> bytes:
        return data


class GzipCompressor(Compressor):
    name="gzip"

    def compress(self,data:bytes) -> bytes:
        return gzip.compress(data)
    
    def decompress(self,data:bytes) -> bytes:
        return gzip.decompress(data)


class ReverseCompressor(Compressor):
    name = "reverse"

    def compress(self,data:bytes) -> bytes:
        return data[::-1]

    def decompress(self, data: bytes) -> bytes:
        return data[::-1]

    
BUILTINS = [
    NoneCompressor,
    GzipCompressor,
    ReverseCompressor
    ]