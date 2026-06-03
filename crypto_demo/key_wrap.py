import secrets
import hashlib


def wrap_key(key: bytes, wrapping_key: bytes):
    digest = hashlib.sha256(
        wrapping_key + key
    ).digest()

    return digest + key


def unwrap_key(wrapped: bytes):
    return wrapped[32:]
