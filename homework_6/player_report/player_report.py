# 3.Napisz program, który wczyta plik o nazwie players.csv i wygeneruje następujący raport:
# a.Top 3 graczy wg największej ilości zdobytych punktów
# b.Średnia wieku graczy
# c.Najczęściej występujące imię wśród graczy
# d.Średnia ilość punktów
# e.Maksymalna ilość punktów
# f.Minimalna ilość punktów
# g.Najstarszy gracz
# h.Najmloszy gracz

import csv
from collections import counter

def data_load(filename='players.csv'):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f, delimiter=',')
        return (list(reader))
# print(data_load())

#top 3 players

def sorted_by_score(players, column_name='score'):
    players.sort(key=lambda player: player['score'], reverse=True)
    players_sorted_by_score = sorted(players, key=lambda player: player[column_name], reverse=True)
    return players_sorted_by_score
print(sorted_by_score())

def get_averages(players, column_name='age'):
    total = 0
    for player in players:
        total += int(player[column_name])

    return total / len(players)


def get_most_common_name(players):
    names = []
    for player in players:
        full_name = player['name']
        # ['imie', 'nazwisko']
        firstname = full_name.split(' ')[0]
        names.append(firstname)
    names_counter = Counter(names)
    names_sorted = names_counter.most_common()
    return names_sorted