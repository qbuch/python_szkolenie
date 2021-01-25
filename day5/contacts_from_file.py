# contacts = {
#     'Kowalski': ['Jan', '123456789', 'Warszawa', 'Zielona', '1'],
#     'Nowak': ['Anna', '987654321', 'Krakow', 'Warszawska', '55'],
#     'Mickiewicz': ['Adam', '123555111', 'Suwałki', 'Litewska', '123'],
#     'Pajton': ['Piotr', '888111444', 'Wroclaw', 'Pajtonowa', '99']
# }
#
#
#
# contacts = {
#     'Nowak': [
#         {
#             'imie': 'Anna',
#             'tel': '987654321',
#             'miasto': 'Krakow',
#             'ulica': 'Warszawska',
#             'nr_domu': '55'
#         },
#         {
#             'imie': 'Piotr',
#             'tel': '123123555',
#             'miasto': 'Krakow',
#             'ulica': 'Dielta',
#             'nr_domu': '15'
#         }
#     ],
# }
#
# print(contacts['Nowak'][0]['tel'])
# print(contacts['Nowak'][1]['tel'])


import csv
from pprint import pprint
from collections import defaultdict

#f = open('adresy.csv', 'r')
with open('adresy.csv', 'r') as f:
    reader = csv.DictReader(f, delimiter=';')

    contacts = defaultdict(list)
    print(reader.fieldnames)
    for line in reader:
            contacts[line['nazwisko']].append(
                {
                    'imie': line['imie'],
                    'tel': line['telefon'],
                    'miasto': line['miasto'],
                    'ulica': line['ulica'],
                    'nr domu': line['nr']
                }
            )
pprint(contacts)


#napisac funkcje ktora dodaje nowe pozycje do slownika