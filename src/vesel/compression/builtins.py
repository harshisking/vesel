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

    def compress(self,data:bytes)->bytes:
        return gzip.compress(data)
    
    def decompress(self,data:bytes)->bytes:
        return gzip.decompress(data)


BUILTINS = [
    NoneCompressor,
    GzipCompressor
    ]