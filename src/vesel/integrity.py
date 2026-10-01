import hashlib

def Hash(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()