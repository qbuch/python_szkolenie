# Napisz program który wprowadzony przez użytkownika tekst zakodje wg szyfru cezara
#* dodaj funkcjonalność dekodowania zaszyfrowanej wiadomości.

pass_to_encrypt = (input('Enter a string you would like to encrypt: ')).lower()
def encrypt_password():
    char_list = list(pass_to_encrypt)
    change_char_ascii = [ord(i) for i in char_list]
    encrypt_ascii = [i + 3 for i in change_char_ascii]
    encrypted_letters = [chr(i) for i in encrypt_ascii]
    encrypted_pass = ''.join(str(i) for i in encrypted_letters)
    return encrypted_pass

pass_to_decrypt = encrypt_password()

def decrypt_password():
    char_list = list(pass_to_decrypt)
    change_char_ascii = [ord(i) for i in char_list]
    decrypt_ascii = [i - 3 for i in change_char_ascii]
    decrypted_letters = [chr(i) for i in decrypt_ascii]
    decrypted_pass = ''.join(str(i) for i in decrypted_letters)
    return decrypted_pass

print(encrypt_password())
print(decrypt_password())

# print(user_input)
# print(change_char_ascii)
# print(encrypt_ascii)
# print(encrypted_letters)
# print(encrypted_pass)

