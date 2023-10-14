from encryptionMethods import *

# Example usage
text = "програмне забезпечення"
col_key = 'крипто'
row_key = 'шифр'

encrypted = encrypt(text, col_key,row_key)

print('Зашифровано:',encrypted)

decrypted = decrypt(encrypted, col_key,row_key)

print('Розшифровано:',decrypted)