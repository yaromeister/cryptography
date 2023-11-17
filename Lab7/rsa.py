import random
import math

from Lab7.prime import isPrime

def generatePrime(bits):
    while True:
        num = random.getrandbits(bits)
        if isPrime(num, 10):
            return num


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = egcd(b % a, a)
        return g, y - (b // a) * x, x


def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g == 1:
        return x % m


def generateKeypair(bits):
    p = generatePrime(bits)
    q = generatePrime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)

    while math.gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    d = modinv(e, phi)

    return ((n, e), (n, d))


bit_length = 512
public_key, private_key = generateKeypair(bit_length)

print("Відкритий ключ:", public_key)
print("Закритий ключ:", private_key)
