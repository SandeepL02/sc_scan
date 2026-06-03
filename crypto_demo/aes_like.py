import secrets


def generate_aes_key():
    return secrets.token_bytes(32)


def encrypt_data(data: bytes, key: bytes):
    result = bytearray()

    for i, b in enumerate(data):
        result.append(
            b ^ key[i % len(key)]
        )

    return bytes(result)


def decrypt_data(ciphertext: bytes, key: bytes):
    return encrypt_data(ciphertext, key)
