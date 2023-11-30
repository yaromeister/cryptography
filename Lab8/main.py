import random
import sympy

from Lab7.prime import isPrime

# Функція для генерації простого числа за допомогою тесту Рабіна-Міллера
def generate_prime(bits):
    prime = random.getrandbits(bits)
    while not isPrime(prime, 5):
        prime = random.getrandbits(bits)
    return prime

# Функція для знаходження первісного кореня за модулем p
def find_primitive_root(p):
    for i in range(2, p):
        if sympy.is_primitive_root(i, p):
            return i

# Функція для обміну ключами по протоколу Діффі-Хелмана
def diffie_hellman():
    # Генерація простого числа p
    p = generate_prime(16)  # Виберіть бажану довжину бітів

    # Знаходження первісного кореня за модулем p
    g = find_primitive_root(p)

    # Генерування випадкових секретних ключів для двох сторін
    a = random.randint(2, p - 2)
    b = random.randint(2, p - 2)

    # Обчислення обмінюваних значень
    A = pow(g, a, p)
    B = pow(g, b, p)

    # Обчислення спільного секретного ключа для обох сторін
    secret_key_A = pow(B, a, p)
    secret_key_B = pow(A, b, p)

    return p, g, A, B, secret_key_A, secret_key_B

# Виклик функції для обміну ключами
p, g, A, B, secret_key_A, secret_key_B = diffie_hellman()

print("Просте число p:", p)
print("Первісний корінь g:", g)
print("Перший обмінений ключ A:", A)
print("Другий обмінений ключ B:", B)
print("Спільний секретний ключ для сторони A:", secret_key_A)
print("Спільний секретний ключ для сторони B:", secret_key_B)
