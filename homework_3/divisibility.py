#wypisz wszystkie liczy z zakresu od 1 do 100, ktore sa podzielne przez 3 lub 7

for i in range(100):
    if(i % 3==0) or (i %  7==0):
        print(i)
