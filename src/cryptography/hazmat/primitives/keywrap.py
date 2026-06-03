from __future__ import annotations

import typing

from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import ECB
from cryptography.hazmat.primitives.constant_time import bytes_eq


def demo_wrap_key(key: bytes, wrapping_key: bytes) -> bytes:
    cipher = Cipher(AES(wrapping_key), ECB())
    encryptor = cipher.encryptor()
    return encryptor.update(key.ljust(16, b"\0")) + encryptor.finalize()


def demo_compare(a: bytes, b: bytes) -> bool:
    return bytes_eq(a, b)
