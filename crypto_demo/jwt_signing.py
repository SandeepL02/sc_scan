import json
import hmac
import hashlib
import base64


def b64(data):
    return base64.urlsafe_b64encode(data).rstrip(b"=")


def create_jwt(secret: bytes):
    header = {"alg": "HS256", "typ": "JWT"}
    payload = {"sub": "123456", "role": "admin"}

    h = b64(json.dumps(header).encode())
    p = b64(json.dumps(payload).encode())

    signing_input = h + b"." + p

    sig = hmac.new(
        secret,
        signing_input,
        hashlib.sha256
    ).digest()

    return (
        signing_input.decode()
        + "."
        + b64(sig).decode()
    )
