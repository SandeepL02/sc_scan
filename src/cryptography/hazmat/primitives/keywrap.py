import hashlib

def wrap_key(k,w):
    return hashlib.sha256(w+k).digest()+k
