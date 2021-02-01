# Napisz program, który jako dane wejściowe przyjmuje hasło od użytkownika i sprawdza poprawność hasła względem poniższym kryteriów:
# a.Conajmniej jedna mała litera
# b.Conajmniej jedna cyfra
# c.Conajmniej jedna wielka litera
# d.Conajmniej jeden znak specjalny np. - @
# e.Minimalna długość hasła 8 znaków
# f.Maksymalna długość hasła 64 znaki (aby nikt nie wkleił całej treści PanaTadeusza ;) )

print('Welcome to password checker!')
user_pass = input('Please enter your password and let us check its validity(totally not a scam): ')


letters = set(user_pass)
lowercase = any(letter.islower() for letter in letters)
uppercase = any(letter.isupper() for letter in letters)

if uppercase:
    print("OK. Your password contains at least one uppercase letter.")
else:
    print("ERROR. Your password doesn`t include at least one uppercase letter.")

if lowercase:
    print("OK. Your password contains at least one lowercase letter.")
else:
    print("ERROR. Your password doesn`t include at least one lowercase letter.")



if len(user_pass) >= 8 and len(user_pass) <= 64:
    print('OK. The length of your password is acceptable.')
elif len(user_pass) < 8:
    print('ERROR. Your password is too short.')
elif len(user_pass) > 64:
    print('ERROR. Your password is too long.')

def digit_check(user_pass):
    no_digit = 0
for char in user_pass:
    if char.isdigit:
        no_digit += 1
if no_digit > 0:
    print('OK. Your password has at least one digit.')
else:
    print('ERROR. Your password doesn`t include any digits.')

def special_char(user_pass):
    special = any(not char.isalnum() for char in user_pass)
if special:
    print('ERROR. There is at least one unacceptable character in your password')
else:
    print('OK. All characters in your password are acceptable')
