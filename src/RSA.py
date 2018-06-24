class RSA:

    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.e = p // 2
        while self.bezout(self.e, self.phi)[0] != 1:
            self.e += 1
        self.d = (self.modinv(self.e, self.phi)) % self.phi

    def encrypt(self, plainText):
        return [self.lpowmod(ord(caracter), self.e, self.n) for caracter in plainText]

    def decrypt(self, cipherText):
        return "".join(chr((self.lpowmod(code, self.d, self.n))) for code in cipherText)

    def lpowmod(self, x, y, n):
        result = 1
        while y > 0:
            if y & 1 > 0:
                result = (result * x) % n
            y >>= 1
            x = (x * x) % n
        return result

    def bezout(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.bezout(b % a, a)
        return (g, x - (b // a) * y, y)

    def modinv(self, a, m):
        g, x, y = self.bezout(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m
