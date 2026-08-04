from .compressor import Compressor
from .exceptions import *

class CompressorRegistry():

    def __init__(self) -> None:
        self._compressors: dict[str, Compressor] = {}


    def register(self,compressor:Compressor):

        if compressor.name in self._compressors:
            raise CompressorAlreadyExists(f"Compressor: '{compressor.name}' already exists.")
        
        self._compressors[compressor.name] = compressor
    
    
    def get(self, name:str)-> Compressor:
        try:
            return self._compressors[name]
        except KeyError:
            raise CompressorNotFoundError(
                f"Unknown Compressor: {name}"
            )
    

    def exists(self,name:str) -> bool:
        return name in self._compressors
    
registry = CompressorRegistry()