# Uzupełnij program książki telefonicznej o dodatkową funkcjonalność edycji kontaktu
# np.w wersji uproszczonej wystarczy możliwość edycji numeru telefonu a w wersji rozszerzonej, edycja dowolnego pola.

import csv
from pprint import pprint
from collections import defaultdict


def add_contact(contact_book, person):
    if person['nazwisko'] in contact_book:
        contact_book[person['nazwisko']].append(
            {
                'imie': person['imie'],
                'nazwisko': person['nazwisko'],
                'tel': person['telefon'],
                'miasto': person['miasto'],
                'ulica': person['ulica'],
                'nr_domu': person['nr']
            }
        )
    else:
        contact_book[person['nazwisko']] = []


def export_to_csv(header, contact_book, filename='adresy.csv'):
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for last_name in contact_book:
            for person in contact_book[last_name]:
                writer.writerow(person.values())


def import_from_csv(filename='adresy.csv', delimiter=','):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        # contacts = defaultdict(list)
        contacts = {}

        for line in reader:
            add_contact(contacts, line)

        return contacts, reader.fieldnames


def search(contact_book, firstname, lastname):
    try:
        people = contact_book[lastname]
    except KeyError:
        print(f'Osoba o nazwisku {lastname} nie istnieje w ksiazce telefonicznej')
    else:
        for person in people:
            if firstname == person['imie']:
                return person['tel']

# def modify_contacts(contact_book)



contact_book, header = import_from_csv(delimiter=';')  # -> (contacts, ['imie', 'nazwisko'])
tel = search(contact_book,'Jan','Kowalski')
print('nr telefonu', tel)
# # export_to_csv(header, contact_book, filename='test.csv')

def update_contact(contact_book, firstname, lastname, field_to_update, value_to_update):
    person = search(contact_book, firstname, lastname)
    person[field_to_update] = value_to_update
    return person


contact_book, header = import_from_csv(delimiter=';')  # -> (contacts, ['imie', 'nazwisko'])
firstname = input('Podaj imie: ')
updated = update_phone_number(contact_book, 'Piotr', 'Nowak', '123123123')
pprint(updated)

updated2 = update_contact(contact_book, 'Piotr', 'Nowak', 'miasto', 'Biłgoraj')
pprint(updated2)