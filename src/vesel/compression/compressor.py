from abc import ABC, abstractmethod

class Compressor(ABC):
    name:str

    @abstractmethod
    def compress(self,data:bytes)->bytes:
        pass

    @abstractmethod
    def decompress(self,data:bytes)->bytes:
        pass