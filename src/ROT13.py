class ROT13:

    def __init__(self):
        self.rotation = 13

    def encrypt(self, plainText):
        return "".join(chr((ord(caracter) + self.rotation) % 256) for caracter in plainText)

    def decrypt(self, cipherText):
        return "".join(chr((ord(caracter) - self.rotation) % 256) for caracter in cipherText)
