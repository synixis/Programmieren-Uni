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
"""Aufgabe 3 (1 Punkt)
Sie haben in der Vorlesung Strings und die Methoden dieses Datentyps kennengelernt. Wir wollen
dieses Wissen benutzen, um in den folgenden Aufgaben eine erste rudimentäre Korpusanalyse
durchzuführen.
Die Variable CORPUS_TEXT enthält unseren zu analysierenden Beispieltext. Sie finden in der Vorlage
bereits mehrere Beispiele und können auch die Beispiele aus der Aufgabenstellung oder Ihre eigenen
Beispiele zum Testen verwenden. Wichtig ist nur, dass Ihr Code allgemein formuliert ist und am
Ende mit allen diesen Texten funktioniert und die richtigen Ergebnisse produziert.
Wir verwenden für die Aufgaben vereinfachte Definitionen. Zunächst wollen wir herausfinden, wie
viele Sätze das Korpus enthält.
Definition: Ein Satz ist ein String, der mit dem Punktzeichen . endet. Sie können davon ausgehen,
dass keine anderen Satzzeichen, wie ! oder ? , ein Satzende markieren. Ihr Code muss also nur
Punkte unterstützen. Gleichzeitig können Sie andererseits annehmen, dass alle Punkte im Text auch
Satzende sind, und nicht beispielsweise Dezimal- oder Tausendertrennzeichen.
Als ersten Schritt soll CORPUS_TEXT in seine Sätze aufgeteilt und das Ergebnis in einer Liste
SENTENCES gespeichert werden. Jedes der Elemente der Variable SENTENCES enthält dann einen
der Sätze, also entspricht die Anzahl der Elemente in SENTENCES genau der Anzahl der Sätze im
Korpus. Diese Zahl soll dann in SENTENCES_COUNT gespeichert werden.
Es gibt mehrere korrekte Varianten für SENTENCES , denn zwischen den Sätzen befindet sich ein
Punkt und ein Leerzeichen. Je nachdem, was man genau noch als Bestandteil eines Satzes definiert,
erhält man unterschiedliche Ergebnisse für die Elemente in SENTENCES . Das spielt für diese Aufgabe
allerdings keine Rolle, denn für die gesuchte Anzahl der Sätze ist diese Information irrelevant.
Beispiel:
>>> CORPUS_TEXT
'I have no quarrel with you, good Sir Knight. But I must cross this bridge.'
Mögliche Lösungen für SENTENCES :
>>> SENTENCES
['I have no quarrel with you, good Sir Knight', 'But I must cross this bridge.']
Oder:
>>> SENTENCES
['I have no quarrel with you, good Sir Knight', 'But I must cross this bridge']
Oder:
>>> SENTENCES
['I have no quarrel with you, good Sir Knight.', 'But I must cross this bridge.']
↪→
4
Alle diese Lösungen liefern das korrekt Endergebnis für SENTENCES_COUNT :
>>> SENTENCES_COUNT
2
Tipp: Zum Trennen eines Strings ( CORPUS_TEXT ) in eine Liste mehrerer Substrings ( SENTENCES )
gibt es eine passende String-Methode und zum Zählen der Elemente einer Liste (für
SENTENCES_COUNT ) gibt es eine passende Built-in-Funktion. Ganz allgemein werden sich die
Methoden von Variablen vom Typ String für die folgenden Aufgaben als äußerst nützlich erweisen.
Es lohnt sich also, alle einfach mal anzuschauen, um einen Überblick zu bekommen.
Außerdem kann es sinnvoll sein, mehrere print -Befehle zum “Debugging” einzubauen, also die
Werte der verwendeten Variablen in Zwischenschritten anzuschauen. Sie können dann diese Ausgabe
Ihres Codes damit vergleichen, was Sie “manuell” durch Untersuchen des jeweiligen CORPUS_TEXT
(durch Zählen der Sätze) als Lösung erwarten würden.
Häufiger Fehler: Bedenken Sie, dass auch der letzte Satz mit einem Punkt endet und was das eventuell
für den letzten Eintrag in Ihrer Liste bedeutet, wenn Sie str.split verwenden. Sie sollten sich im
Zweifel Ihr Zwischenergebnis mit print(SENTENCES) anschauen."""

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

CORPUS_CLEANED = CORPUS_TEXT
TOKENS = None
TOKENS_COUNT = None


# Aufgabe 5

TYPES = None
TYPES_COUNT = None


# Aufgabe 6

LONGEST_TYPE = None


# Aufgabe 7

LONGEST_TYPE_PROPERTIES = {}
LONGEST_TYPE_PROPERTIES["letters_converted_to_capitals"] = None
LONGEST_TYPE_PROPERTIES["contains_only_letters"] = None
LONGEST_TYPE_PROPERTIES["all_letters_are_lowercase"] = None
LONGEST_TYPE_PROPERTIES["how_many_letter_e"] = None
LONGEST_TYPE_PROPERTIES["index_of_first_letter_e"] = None

# Oder direkt so:
# LONGEST_TYPE_PROPERTIES = {
#     "letters_converted_to_capitals": None,
#     "contains_only_letters": None,
#     "all_letters_are_lowercase": None,
#     "how_many_letter_e": None,
#     "index_of_first_letter_e": None,
# }


# Zusatzaufgabe 8

# Antwort:


# Zusatzaufgabe 9

# Antwort:
