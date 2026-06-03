class Cipher:
    def __init__(self, algorithm, mode):
        self.algorithm = algorithm
        self.mode = mode

    class _Encryptor:
        def update(self, data):
            return data
        def finalize(self):
            return b''

    def encryptor(self):
        return self._Encryptor()
