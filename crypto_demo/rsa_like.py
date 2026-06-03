import secrets


def generate_rsa_keypair():
    public_exponent = 65537

    p = secrets.randbits(1024)
    q = secrets.randbits(1024)

    n = p * q

    return {
        "e": public_exponent,
        "n": n
    }
