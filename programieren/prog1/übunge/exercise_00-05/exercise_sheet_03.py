#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Vorlage zu Übungsblatt 03

Dieses Dokument dient Ihnen als Vorlage für Ihre Abgabe zum aktuellen
Übungsblatt. Sie finden weiter unten mehrere Abschnitte, passend zu
den einzelnen Aufgaben des Übungsblatts.

"""


# Aufgabe 1

def print_square():
    number = input("Bitte geben Sie eine Zahl ein: ")
    number = int(number)
    number = number ** 2
    return number

# Aufgabe 2
"""ervollständigen Sie die Funktion account_number . Sie hat einen Parameter number mit welchem
eine Kontonummer als Typ Integer übergeben wird. Die Funktion soll dieser Nummer so viele Nullen
voranstellen, dass sich insgesamt 9 Ziffern ergeben. Dieses Ergebnis soll als String zurückgegeben
werden. Sollte number eine negative Zahl sein, weniger als 3 Ziffern oder mehr als 9 Ziffern besitzen,
dann soll None zurückgegeben werden. (Negative Kontonummern sowie Kontonummern von Länge
kleiner 3 oder größer 9 werden von dieser Bank nicht vergeben.)"""
def account_number(number):
    if number < 999 or number > 1000000:
        return None
    else:
        return f"{number:09d}"
    # TODO

# Aufgabe 3

def translate(dictionary, word):
    if word in dictionary:
        return dictionary[word]
    else:
        return None


# Aufgabe 4
"""Vervollständigen Sie die Funktion invert_dict . Sie hat einen Parameter dictionary für ein
Wörterbuch vom Typ dict . Die Schlüssel-Wert-Paare von dictionary sollen invertiert und
anschließend als neues Objekt vom Typ dict zurückgegeben werden.
Ein Aufruf von invert_dict(DE_EN) soll also beispielsweise folgenden Rückgabewert besitzen:
{"King": "König", "Knight": "Ritter", "Dragon": "Drache", "Aaaarrggh": "Aaaarrggh"}"""

def invert_dict(dictionary):
    inv_dict = {v: k for k, v in dictionary.items()}
    return inv_dict


# Aufgabe 4 Antwort Verständnisfrage:
# die wete im dict müssen, anders als die keys, nicht unique sein
#


# Aufgabe 5

def word_mincer(word, begin_upper=False):
    pass


# Testaufrufe

if __name__ == "__main__":
    print_square()
    print(account_number(12345))
    print(account_number(0))
    print(account_number(123456789))
    print(account_number(-999))
    print(account_number(11))
    print(account_number(1111111111))
    DE_EN = {
        'König': 'King',
        'Ritter': 'Knight',
        'Drache': 'Dragon',
        'Aaaarrggh': 'Aaaarrggh'
    }
    print(translate(DE_EN, 'Ritter'))
    print(translate(DE_EN, 'Pferd'))
    print(invert_dict(DE_EN))
    print(word_mincer('König'))
    print(word_mincer('KÖNIG'))
    print(word_mincer('kÖnIg'))
    print(word_mincer('KöNiG'))
    print(word_mincer('Kaugummiautomat'))
    print(word_mincer('Kaugummiautomat', begin_upper=True))
