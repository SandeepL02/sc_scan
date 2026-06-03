import hashlib

def sha256_hash(d):
    return hashlib.sha256(d.encode()).hexdigest()
