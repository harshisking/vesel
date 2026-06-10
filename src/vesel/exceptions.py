class VeselError(Exception):
    pass

class InvalidPathError(VeselError):
    pass

class InvalidMagicError(VeselError):
    pass

class UnsupportedVersionError(VeselError):
    pass

class CorruptedFileError(VeselError):
    pass



__all__=[
    "VeselError",
    "InvalidPathError",
    "InvalidMagicError",
    "UnsupportedVersionError",
    "CorruptedFileError"
]