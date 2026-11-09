#!/usr/bin/env python3
# -*- coding: utf-8 -*-  # noqa: UP009

"""Vorlage zu Übungsblatt 02

Dieses Dokument dient Ihnen als Vorlage für Ihre Abgabe zum aktuellen
Übungsblatt. Sie finden weiter unten mehrere Abschnitte, passend zu den
einzelnen Aufgaben des Übungsblatts.

"""


# Aufgabe 1
A = 35669
B = 1
print(A + 2 * B)

C = 10
print((3 ** (C - 1)) + 1)

D = 37
print(True and not D - 37)


# Aufgabe 2

QUOTE = "Python ist eine universelle, üblicherweise interpretierte höhere Programmiersprache."

# Falls sich Tutron über eine veränderte `QUOTE`-Variable beschwert
# und Sie Probleme mit der Kodierung vermuten, können Sie mit dem
# folgenden String testen, ob die Fehlermeldung verschwindet:
#     QUOTE = (
#         "Python ist eine universelle, \u00fcblicherweise "
#         "interpretierte h\u00f6here Programmiersprache."
#     )
# Diese Definition des Strings verwendet Unicode-Escapesequenzen
# statt der Unicode-Zeichen für die Umlaute. Sie sollten dann
# unbedingt herausfinden, welches Ihrer verwendeten Programme die
# Korruption verursacht.

F = 0
G = 11
H = 51
I = -17
J = -59
K = -1
print(QUOTE[F:G] + QUOTE[H] + QUOTE[I] + 2 * QUOTE[J] + QUOTE[K])

L = 11
M = 51
N = 5
print(QUOTE[:L] + "su" + QUOTE[48:M:2] + QUOTE[-6::N])

print("abc")
# Aufgabe 3

CORPUS_TEXT = (
    "Listen. Strange women lying in ponds distributing swords is no "
    "basis for a system of government. Supreme executive power "
    "derives from a mandate from the masses, not from some farcical "
    "aquatic ceremony."
)

# Erinnerung: Der Code soll mit *jedem beliebigen Text-Korpus*
# funktionieren. Sie finden deshalb hier weitere Beispiele für die
# Variable `CORPUS_TEXT` zum Testen.
#
# CORPUS_TEXT = (
#     "The wise Sir Bedevere was the first to join King Arthur's "
#     "knights, but other illustrious names were soon to follow: Sir "
#     "Lancelot the Brave, Sir Gallahad the Pure, and Sir Robin "
#     "the-not-quite-so-brave-as-Sir-Lancelot, who had nearly fought "
#     "the Dragon of Angnor, who had nearly stood up to the vicious "
#     "Chicken of Bristol, and who had personally wet himself at the "
#     "Battle of Badon Hill, and the aptly named Sir "
#     "Not-appearing-in-this-film. Together they formed a band whose "
#     "names and deeds were to be retold throughout the centuries: "
#     "The Knights of the Round Table."
# )
#
# CORPUS_TEXT = (
#     "First shalt thou take out the Holy Pin. Then, shalt thou count "
#     "to three. No more. No less. Three shalt be the number thou "
#     "shalt count, and the number of the counting shall be three. "
#     "Four shalt thou not count, nor either count thou two, "
#     "excepting that thou then proceed to three. Five is right out. "
#     "Once the number three, being the third number, be reached, "
#     "then, lobbest thou thy Holy Hand Grenade of Antioch towards "
#     "thy foe, who, being naughty in My sight, shall snuff it."
# )

SENTENCES = [sentence.strip() for sentence in CORPUS_TEXT.split(".") if sentence.strip()]
SENTENCES_COUNT = len(SENTENCES)
print(SENTENCES_COUNT)
print(SENTENCES)
print("bhjbjh")

# Aufgabe 4

CORPUS_CLEANED = CORPUS_TEXT.replace(".", "").replace(":", "").replace(",", "")

TOKENS = CORPUS_CLEANED.split()
TOKENS_COUNT = len(TOKENS)

# Aufgabe 5

TYPES = set(TOKENS)
TYPES_COUNT = len(TYPES)


# Aufgabe 6

LONGEST_TYPE = max(TYPES, key=len)

# Aufgabe 7

LONGEST_TYPE_PROPERTIES = {}
LONGEST_TYPE_PROPERTIES["letters_converted_to_capitals"] = LONGEST_TYPE.upper()
LONGEST_TYPE_PROPERTIES["contains_only_letters"] = LONGEST_TYPE.isalpha()
LONGEST_TYPE_PROPERTIES["all_letters_are_lowercase"] = LONGEST_TYPE.islower()
LONGEST_TYPE_PROPERTIES["how_many_letter_e"] = LONGEST_TYPE.count("e")
LONGEST_TYPE_PROPERTIES["index_of_first_letter_e"] = LONGEST_TYPE.find("e")

# Oder direkt so:
# LONGEST_TYPE_PROPERTIES = {
#     "letters_converted_to_capitals": None,
#     "contains_only_letters": None,
#     "all_letters_are_lowercase": None,
#     "how_many_letter_e": None,
#     "index_of_first_letter_e": None,
# }


# Zusatzaufgabe 8

# Antwort: In Python beginnt die Indizierung bei 0 und nicht bei 1.


# Zusatzaufgabe 9

# Antwort: Ein Tuple ist in Python unveränderlich (immutable).
