from pathlib import Path

# local imports
from .models import (
    Version,
    Header,
    VeselFile
)
from .constants import MAGIC
from .exceptions import (
    InvalidPathError,
    InvalidMagicError
)

class VeselIO:
    
    @staticmethod
    def write(path,file:VeselFile):
        path = Path(path)

        if (not path.parent.exists()) & (not path.parent.is_dir()):
            raise InvalidPathError(
                f"Directory does not exists: {path.parent}"
            )
        data = VeselIO.to_bytes(file)

        with open(path, "wb") as f:
            f.write(data)
    
    @staticmethod
    def read(path) -> VeselFile:
        path = Path(path)

        if (not path.exists()) & (not path.is_file()):
            raise InvalidPathError(
                f"File does not exists: {path}"
            )
        with open(path,"rb") as f:
            data = f.read()
        
        return VeselIO.from_bytes(data)

    

    @staticmethod
    def to_bytes(file:VeselFile)->bytes:
        version= bytes([
                    file.header.version.major,
                    file.header.version.minor,
                    file.header.version.patch
                ])
        
        compression = file.header.compression.encode("utf-8")
        file.header.compression_len = len(compression)
        compression_len = file.header.compression_len.to_bytes(1,"big")

        file.header.payload_length = len(file.payload)
        length = file.header.payload_length.to_bytes(4,"big")

        return (file.header.magic)+version+compression_len+compression+length+file.payload
    

    @staticmethod
    def from_bytes(data:bytes)->VeselFile:
        magic = data[:5]
        if magic != MAGIC:
            raise InvalidMagicError(
                "Not a vesel file"
            )
        
        major,minor,patch = int.from_bytes(data[5:6]),int.from_bytes(data[6:7]),int.from_bytes(data[7:8])
        version = Version(major,minor,patch)
        
        compression_length = int.from_bytes(data[8:9])
        compression = data[9:(9+compression_length)].decode("utf-8")

        length = int.from_bytes(data[(9+compression_length):(13+compression_length)],'big')
        
        payload = data[(13+compression_length):(13+compression_length+length)]

        return VeselFile(
            Header(compression_len=compression_length,compression=compression,payload_length=length),
            payload
        )
        