class Cesar:

    def __init__(self, offset):
        self.offset = offset

    def encrypt(self, plainText):
        return "".join(chr((ord(caracter) + self.offset) % 256) for caracter in plainText)

    def decrypt(self, cipherText):
        return "".join(chr((ord(caracter) - self.offset) % 256) for caracter in cipherText)
