class CompressorNotFoundError(Exception):
    pass

class CompressorAlreadyExists(Exception):
    pass

__all__=[
    "CompressorNotFoundError",
    "CompressorAlreadyExists"
    ]