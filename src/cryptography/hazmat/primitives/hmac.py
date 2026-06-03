import hmac, hashlib

def sign(k,m):
    return hmac.new(k,m,hashlib.sha256).hexdigest()
