# Napisz program obliczający wiek psa z ludzkich lat w psich latach.
# Przez pierwsze dwa lata każdy psi rok to 10.5 ludzkiego, kolejne lata - psi rok to 4 ludzkie lata.
# Na przykład:15 ludzkich lat to 73 psie lata. Dane wejściowe wprowadza użytkownik po uruchomieniuprogramu.


human_age = int(input("Podaj wiek czlowieka: "))

if human_age == 1:
    print(10.5)
elif human_age == 2:
    print(21)
elif human_age >= 3:
    print("Twoj wiek w psich latach to " + str(((human_age - 2) * 4) + 21))
