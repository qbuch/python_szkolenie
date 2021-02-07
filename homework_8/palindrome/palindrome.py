# Wczytaj dane z pliku words.txt i wyświetl wszystkie wyrazy które są palindromem.

filename  = 'words.txt'

with open('words.txt') as f:
    for line in f:
        if str(filename) == str(filename)[::-1]:
            print("It`s a palindrome")
        else:
            print('It`s not a palindrome')




