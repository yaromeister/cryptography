def mul02(byte):
    if byte & 0x80:
        return ((byte << 1) ^ 0x1B) & 0xFF
    else:
        return (byte << 1) & 0xFF

def mul03(byte):
    return mul02(byte) ^ byte


def main():
    try:
        input_byte = int(input("Введіть шістнадцятковий байт: "), 16)

        result_mul02 = mul02(input_byte)
        result_mul03 = mul03(input_byte)

        print(f"mul02: {hex(result_mul02)}")
        print(f"mul03: {hex(result_mul03)}")

    except ValueError:
        print("Помилка: Введення не є шістнадцятковим байтом.")


if __name__ == "__main__":
    while True:
        main()