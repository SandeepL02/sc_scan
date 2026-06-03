import secrets

def generate_rsa_keypair():
    return {'n': secrets.randbits(2048), 'e':65537}
