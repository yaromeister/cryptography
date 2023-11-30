import random
import sympy

from Lab7.prime import isPrime

# Функція для генерації простого числа за допомогою тесту Рабіна-Міллера
def generate_prime(bits):
    prime = random.getrandbits(bits)
    while not isPrime(prime, 10):
        prime = random.getrandbits(bits)
    return prime

# Функція для знаходження первісного кореня за модулем p
def find_primitive_root(p):
    for i in range(2, p):
        if sympy.is_primitive_root(i, p):
            return i

# Функція для шифрування повідомлення
def elgamal_encrypt(plaintext, p, g, public_key):
    k = random.randint(2, p - 2)
    A = pow(g, k, p)
    B = (pow(public_key, k, p) * plaintext) % p
    return A, B

# Функція для дешифрування шифртексту
def elgamal_decrypt(ciphertext, private_key, p):
    A, B = ciphertext
    decrypted_message = (B * pow(A, p - 1 - private_key, p)) % p
    return decrypted_message

# Генерація параметрів p та g
p = generate_prime(16)  # Виберіть бажану довжину бітів
g = find_primitive_root(p)

# Генерація приватного ключа
private_key = random.randint(2, p - 2)

# Визначення публічного ключа
public_key = pow(g, private_key, p)

# Повідомлення, яке потрібно зашифрувати
message = 42  # Замініть це повідомленням, яке ви хочете зашифрувати

# Шифрування повідомлення
ciphertext = elgamal_encrypt(message, p, g, public_key)

# Дешифрування шифртексту
decrypted_message = elgamal_decrypt(ciphertext, private_key, p)

# Вивід результатів
print("Параметр p:", p)
print("Первісний корінь g:", g)
print("Приватний ключ:", private_key)
print("Публічний ключ:", public_key)
print("Повідомлення для шифрування:", message)
print("Зашифроване повідомлення (A, B):", ciphertext)
print("Дешифроване повідомлення:", decrypted_message)
