#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

╭──────────────────────────-·-ˋˏ-༻𖤓༺-ˎˊ·-──────────────────────────╮
                                HALLO ^^
                   Dieses ist die Abgabe zum aktuellen
 Übungsblatt03. Sie finden weiter unten mehrere Abschnitte, passend zu
                  den einzelnen Aufgaben des Übungsblatts.
                                -Julia
╰──────────────────────────-·-ˋˏ-༻𖤓༺-ˎˊ·-──────────────────────────╯

"""

# Aufgabe 1
def print_square():
    """printet das Quadrat der Ziffer □️"""
    number = input("Bitte geben Sie eine Zahl ein: ")
    number = int(number)
    number = number ** 2
    print(number)

# Aufgabe 2
def account_number(number):
    """Formatiert zu 9 Ziffern, am anfang mit 0 aufgefüllt"""
    if 100 <= number <= 999999999:
        return str(number).zfill(9)
    return None

# Aufgabe 3
def translate(dictionary, word):
    """translate a word in the dict."""
    if word in dictionary:
        return dictionary[word]
    return None

# Aufgabe 4
def invert_dict(dictionary):
    """macht dict inverten"""
    inv_dict = {v: k for k, v in dictionary.items()}
    return inv_dict

# Aufgabe 4 Antwort Verständnisfrage:
# die wete im dict müssen, anders als die keys, nicht unique sein

# Aufgabe 5
def word_mincer(word, begin_upper=False):
    """bUcHsTaBeN So HoCh RuNtEr AnOrDnEn, DaSs sIe aBbWeChSeLnD GROß und klein GeScHrIeBeN wErDeN. /
    begin_upper gibt an, ob der erste Buchstabe GROß GESCHRIEBEN werden soll oder nicht."""
    if begin_upper:
        return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(word)])

    return ''.join([c.lower() if i % 2 == 0 else c.upper() for i, c in enumerate(word)])

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
