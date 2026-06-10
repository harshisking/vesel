from dataclasses import dataclass

@dataclass
class Version:
    major:int
    minor:int
    patch:int

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"
    
@dataclass
class Header:
    version: Version

@dataclass
class VeselFile:
    header: Header
    payload: bytes