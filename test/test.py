import sys
sys.path.append('../src')
from pocha import describe, it
from Cesar import *
from Vigenere import *
from ROT13 import *
from Vernam import *
from RSA import *


@describe('Test of encryptions modules')
def _():
    message = "This text is a sample to be encode and decode with various encryption methods."
    cesar = Cesar(3)  # Offset = 3
    vigenere = Vigenere("password")  # Key = password
    rot13 = ROT13()
    vernam = Vernam(len(message))  # RandomKey length = length of message
    rsa = RSA(33967, 917227)  # p et q prime number

    @it('should test the constructor of Cesar encryption module')
    def testConstructorOfCesarModule():
        assert cesar.offset == 3

    @it('should test the constructor of Vigenere encryption module')
    def testConstructorOfVigenereModule():
        assert vigenere.key == "password"

    @it('should test the constructor of ROT13 encryption module')
    def testConstructorOfROT13Module():
        assert rot13.rotation == 13

    @it('should test the constructor of Vernam encryption module')
    def testConstructorOfVernamModule():
        assert len(vernam.key) == len(message)

    @it('should test the constructor of RSA encryption module')
    def testConstructorOfRSAModule():
        assert rsa.p == 33967
        assert rsa.q == 917227

    @it('should test the Cesar encryption method')
    def testCesarEncryptionMethod():
        encoded = cesar.encrypt(message)
        decoded = cesar.decrypt(encoded)
        assert decoded == message

    @it('should test the Vigenere encryption method')
    def testVigenereEncryptionMethod():
        encoded = vigenere.encrypt(message)
        decoded = vigenere.decrypt(encoded)
        assert decoded == message

    @it('should test the ROT13 encryption method')
    def testROT13EncryptionMethod():
        encoded = rot13.encrypt(message)
        decoded = rot13.decrypt(encoded)
        assert decoded == message

    @it('should test the Vernam encryption method')
    def testVernamEncryptionMethod():
        encoded = vernam.encrypt(message)
        decoded = vernam.decrypt(encoded)
        assert decoded == message

    @it('should test the RSA encryption method')
    def testRSAEncryptionMethod():
        encoded = rsa.encrypt(message)
        decoded = rsa.decrypt(encoded)
        assert decoded == message
