import hmac
import hashlib


def sign_message(secret: bytes, message: bytes):
    return hmac.new(
        secret,
        message,
        hashlib.sha256
    ).hexdigest()
