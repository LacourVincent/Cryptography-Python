from random import randint


class Vernam:

    def __init__(self, keySize):
        self.key = ""
        for i in range(keySize):
            self.key += chr(randint(0, 255))

    def encrypt(self, plainText):
        return "".join(chr((ord(plainText[i]) + ord(self.key[i])) % 256) for i in range(len(plainText)))

    def decrypt(self, cipherText):
        return "".join(chr((ord(cipherText[i]) - ord(self.key[i])) % 256) for i in range(len(cipherText)))
