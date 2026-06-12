from .io import VeselIO
from .models import VeselFile,Header,Version
from .exceptions import *

def write(path,payload:bytes):
    file = VeselFile(
        Header(Version(0,2,2)),
        payload
    )

    VeselIO.write(path,file)

def read(path) -> VeselFile:
    return VeselIO.read(path)

def readjson(path) -> dict:
    loaded = VeselIO.read(path)
    return {"Header":{
        'Version':loaded.header.version,
        "Payload_length":loaded.header.payload_length},
        "Payload":loaded.payload
        }

__all__ = [
    "VeselIO",
    "VeselFile",
    "Header",
    "Version",
]