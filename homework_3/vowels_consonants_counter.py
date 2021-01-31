# 6.Napisz program zliczający osobno ilość wystąpień spółgłosek i samogłosek dladowolnego ciągu znaków.
# Dane wejściowe wprowadza użytkownik po uruchomieniu programu.

user_input = input('Type in word you would like to process: ')

word = user_input.lower()
vowels_count = 0
consonants_count = 0
vowels = 'aeiou'
if len(word) > 0 and word.isalpha():
    for i in word:
        if i in vowels:
            vowels_count += 1
        else:
            consonants_count += 1

print(f'Your input has {vowels_count} vowels and {consonants_count} consonants.'),
