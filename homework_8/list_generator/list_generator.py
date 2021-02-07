# 1.Wygeneruj dwie listy po 1000 elementów, w której będą się znajdować liczby losowe zprzedziału 1-1000(randint).
# Porównaj obydwie listy i wyświetl:
# a.Liczby znajdujące się w obydwu listach.
# b.Liczby znajdujące się tylko w pierwszej liście.
# c.Liczby znajdujące się tylko w drugiej liście.
# d.Liczbę wystąpień każdej z liczby w obydwu listach i wyświetl top 3 najczęściej występujące w każdej z nich.
# e.Obydwie listy posortowane rosnąco i malejąco.

import random
from collections import Counter
import csv

random1 = random.sample(range(5000), 1000)
random2 = random.sample(range(3000), 1000)

random_set1 = set(random1)
random_set2 = set(random2)

numbers_in_both_sets = random_set1 & random_set2
# print(numbers_in_both_sets)

not_in_random1 = { x for x in random_set1 if x not in random_set2 }
not_in_random2 = { x for x in random_set2 if x not in random_set1 }

# print(not_in_random1)
# print(not_in_random2)

occurences_num = Counter(random_set1)
occurences_num2 = Counter(random_set2)

# print(occurences_num)
# print(occurences_num2)

sorted1 = sorted(random_set1)
sorted2 = sorted(random_set2)

# print(sorted1)
# print(sorted2)


common_num = random_set1.intersection(random_set2)
top3_num = Counter(common_num).most_common(3)
# print(common_num)
# print(top3_num) #za kazdym razem otrzymuje zestawienie liczb ktore wystepuja tylko 1 raz. Dlaczego nie pojawiaja sie zdublowane wartosci w obydwu setach?
