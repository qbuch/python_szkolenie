# Stworzyc klase czlowieka
# stan wewnetrzny (atrybuty): imie, nazwisko, pesel, wiek
#interfejs (metody):
    #metoda introduce - 'Hej, jestem Jan Kowalski, mam X lat'
    #metoda do wyswietlenia dokladnej daty urodzin(na podstawie nr pesel

class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        # self.pesel = pesel
        self.age = age

    def introduce(self):
        print(f'Hi, my name is {self.name} {self.surname} and I`m {self.age} years old.')

if __name__ == '__main__':
    man = Human('Jan', 'Nowak', 35)
    # woman = Human('Anna', 'Nowak', '1234567899', '44')

man.introduce()