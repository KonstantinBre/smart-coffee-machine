# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 16:43:30 2023

@author: konst
"""

def überprüfen_liste(liste):
    name_wahrscheinlichkeit = {}

    for eintrag in liste:
        name, prozent = eintrag
        if name not in name_wahrscheinlichkeit:
            name_wahrscheinlichkeit[name] = []

        name_wahrscheinlichkeit[name].append(prozent)

    erfüllte_kriterien = []

    for name, wahrscheinlichkeiten in name_wahrscheinlichkeit.items():
        if len(wahrscheinlichkeiten) >= 0.75 * len(liste):
            durchschnitt = sum(wahrscheinlichkeiten) / len(wahrscheinlichkeiten)
            if durchschnitt >= 0.8:
                erfüllte_kriterien.append((name, durchschnitt))

    return erfüllte_kriterien

# Beispielaufruf
meine_liste = [
    ["Tim", 0.9],
    ["ff", 0.78],
    ["s", 0.85],
    ["Tissm", 0.95],
    ["Tim", 0.82],
    ["Null", 0.88],
    ["Tim", 0.75],
    ["Null", 0.91],
]

ergebnis = überprüfen_liste(meine_liste)

if ergebnis == []:
    ergebnis = ['Unbekannt', 0.0
                ]
print(ergebnis)
