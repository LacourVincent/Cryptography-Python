class Vigenere:

    def __init__(self, key):
        self.key = key

    def encrypt(self, plainText):
        return "".join(chr((ord(plainText[i]) + ord(self.key[i % len(self.key)])) % 256) for i in range(len(plainText)))

    def decrypt(self, cipherText):
        return "".join(chr((ord(cipherText[i]) - ord(self.key[i % len(self.key)])) % 256) for i in range(len(cipherText)))
