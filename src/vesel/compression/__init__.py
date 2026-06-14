from .compressor import Compressor
from .registry import registry
from .builtins import BUILTINS
from .exceptions import *

register_compressor = registry.register
get_compressor = registry.get

for _compressor in BUILTINS:
    register_compressor(_compressor())

__all__ = [
    "Compressor",
    "register_compressor",
    "get_compressor",
    "registry"
]