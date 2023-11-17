import random

def isPrime(n, k):
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def main():
    n = 0
    while n <= 3 or n % 2 == 0:
        n = int(input("Введіть натуральне непарне число n (>3): "))
        if n <= 3:
            print("Будь ласка, введіть число більше за 3.")
        elif n % 2 == 0:
            print("Будь ласка, введіть непарне число.")
    k = int(input("Введіть кількість раундів k: "))

    if isPrime(n, k):
        print(f"{n} є простим числом з ймовірністю {(1 - 0.25 ** k) * 100}%.")
    else:
        print(f"{n} не є простим числом.")

if __name__ == "__main__":
    main()
