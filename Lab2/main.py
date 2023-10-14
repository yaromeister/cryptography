
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return (key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return ("".join(key))


def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 32
        x += ord('А')
        cipher_text.append(chr(x))
    return ("".join(cipher_text))


def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 32) % 32
        x += ord('А')
        orig_text.append(chr(x))
    return ("".join(orig_text))



string = "тестовийтекст"
keyword = "ключ"
key = generateKey(string, keyword)
cipher_text = cipherText(string, key)
print("Зашифрований:", cipher_text)
print("Розшифрований:", originalText(cipher_text, key))


