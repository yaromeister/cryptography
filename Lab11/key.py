import random

def is_prime(n, k=5):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False

    # n-1 = 2^s * d
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits=1024):
    while True:
        potential_prime = random.getrandbits(bits)
        if potential_prime % 2 != 0 and is_prime(potential_prime):
            return potential_prime

def primitive_root(p):
    if p == 2:
        return 1
    p1 = 2
    p2 = (p - 1) // p1

    while True:
        g = random.randint(2, p - 1)
        if not (pow(g, (p - 1) // p1, p) == 1):
            if not pow(g, (p - 1) // p2, p) == 1:
                return g

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1

    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0

    return x1 + m0 if x1 < 0 else x1

def generate_keys():
    p = generate_prime()
    g = primitive_root(p)
    x = random.randint(2, p - 2)
    y = pow(g, x, p)
    return (p, g, y), x

def encrypt(message, public_key):
    p, g, y = public_key
    k = random.randint(2, p - 2)
    c1 = pow(g, k, p)
    s = pow(y, k, p)
    c2 = [(s * ord(char)) % p for char in message]
    return c1, c2

def decrypt(ciphertext, private_key, p):
    c1, c2 = ciphertext
    x = private_key
    s = pow(c1, x, p)
    message = ''.join([chr((mod_inverse(s, p) * char) % p) for char in c2])
    return message

# Генеруємо ключі
public_key, private_key = generate_keys()
print("Публічний ключ (p, g, y):", public_key)
print("Приватний ключ (x):", private_key)

# Повідомлення для шифрування
message = "Lab11"

# Шифруємо повідомлення
encrypted = encrypt(message, public_key)
print("\nЗашифроване повідомлення:", encrypted)

# Розшифровуємо повідомлення
decrypted = decrypt(encrypted, private_key, public_key[0])
print("Розшифроване повідомлення:", decrypted)
