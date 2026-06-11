from dataclasses import dataclass
from .constants import MAGIC

@dataclass
class Version:
    major:int
    minor:int
    patch:int

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"
    
@dataclass
class Header:
    magic=MAGIC
    version: Version
    payload_length:int = 0

@dataclass
class VeselFile:
    header: Header
    payload: bytes