from .io import VeselIO
from .models import VeselFile,Header,Version
from .exceptions import *
from .compression import *

def write(path,payload:bytes,comrpession_name:str="none"):

    compressor = get_compressor(comrpession_name)
    payload = compressor.compress(payload)

    file = VeselFile(
        Header(compression=comrpession_name),
        payload
    )

    VeselIO.write(path,file)

def read(path) -> VeselFile:
    file = VeselIO.read(path)
    
    compressor = get_compressor(file.header.compression)
    decompressed_payload = compressor.decompress(file.payload)
    file.payload = decompressed_payload
    file.header.payload_length = len(file.payload)
    
    return file

def readjson(path) -> dict:
    loaded = VeselIO.read(path)

    compressor = get_compressor(loaded.header.compression)
    loaded.payload = compressor.decompress(loaded.payload)
    loaded.header.payload_length = len(loaded.payload)

    return {"Header":{
        "Magic":loaded.header.magic,
        'Version':loaded.header.version,
        "Compression_len":loaded.header.compression_len,
        "Compression":loaded.header.compression,
        "Payload_length":loaded.header.payload_length},
        "Payload":loaded.payload
        }

__all__ = [
    "VeselIO",
    "VeselFile",
    "Header",
    "Version",
]