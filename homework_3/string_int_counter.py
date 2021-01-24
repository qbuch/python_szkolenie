#Napisz program, obliczający liczbę cyfr i liter w dowolnym ciągu znaków
# np.“Tomek123” - 5 liter, 3 cyfry. Dane wejściowe wprowadza użytkownik po uruchomieniu programu.

user_prompt = input("Hey, give me an input to count: ")

letters = 0
digits = 0

for i in user_prompt:
    if(i.isalpha()):
        letters+=1
    elif(i.isdigit()):
        digits+=1

#print("Your input has " + str(letters) + " letters and " + str(digits) + " digits.")

print(f"Your input has {letters} letters and {digits} digits.")