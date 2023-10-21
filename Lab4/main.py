
def gcdex(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = gcdex(b % a, a)
        return (g, y - (b // a) * x, x)

a = 612
b = 342
d, x, y = gcdex(a, b)
print(f"GCD({a}, {b}) = {d}" + f", x = {x}, y = {y}")

def inverse_element(a, n):
    d, x, y = gcdex(a, n)
    if d != 1:
        raise ValueError(f"Мультиплікативний обернений елемент не існує для a = {a} та n = {n}")
    else:
        x = (x % n + n) % n  # Перевірка на від'ємне значення x та зменшення його до діапазону [0, n)
        return x

# Приклад використання:
a = 5
n = 18
result = inverse_element(a, n)
print(f"Мультиплікативний обернений елемент для {a} за модулем {n} дорівнює {result}")


def phi(m):
    result = m  # Ініціалізуємо результат значення m
    p = 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            result -= result // p
        p += 1
    if m > 1:
        result -= result // m
    return result

# Приклад використання:
m = 543
result = phi(m)
print(f"Значення функції Ейлера для {m} дорівнює {result}")

def inverse_element_2(a, p):
    if a == 0:
        raise ValueError("Оберненого елементу для 0 не існує")
    return pow(a, p - 2, p)

# Приклад використання:
a = 5
n = 18
result = inverse_element_2(a, n)
print(f"Мультиплікативний обернений елемент для {a} за модулем {n} дорівнює {result}")