# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 13:57:25 2024

@author: konst
"""
import database
# =============================================================================
# KLASSE & BEFEHLE IMPORTIEREN
# in database laden, diese ist bereit veknüft mit user_database.db
# (extra Datei in der alle Daten gespeichert werden)
# =============================================================================
from database import UserDatabase
from database import create_user
database = UserDatabase()

# =============================================================================
# BENUTZER HINZUFÜGEN
# 
# aber zum Verständnis  für den Aufbau den Datenstrukt
# WICHTIG: Benutzernummer kann immer nur ein Mal vergeben werden, sonst Error 
# AUFBAU: number, name, max caffeine, favorite, counter
#
# IMPORTANT: Einmalig am Anfang die Funktion create_user(5) ausführen 
# danach nie wieder ausführen da sonst ERRORROROROROR O
# damit werden 5 leere user erstellt, damit in der GUI verwendet werden können
# =============================================================================

# create_user(5)


# database.add_user(100, 'Max Mustermann', 100, 'Filterkaffee', 0)


# =============================================================================
# Benutzer löschen
# falls man doch einen Benutzer lösche muss, wirst du ebenfalls nicht brauchen
# =============================================================================

# database.delete_user_by_number(100)


# =============================================================================
# BENUTZER ABFRAGEN
# wirst du zu 100% brauchen
# Übergabewerte ist die ID des Benutzers 
# Daten werden in einem Tuple gespeichert, die du mit user[x] aufrufen kann
# gleiche Struktur, wie bei der Speicherung 
# =============================================================================

user = database.get_user_by_number(1)
print(user[0])
print(user[1])
print(user[2])
print(user[3])
print(user[4])


# =============================================================================
# TÄGLICHER KOFFEINCOUNTER UPDATEN
# nachdem ein benutzer einen Heißgetränk bestellt hat, soll auch der Koffein Counter 
# erhöht werde, das wir mir dieser Funktion gemacht
# Übergabewerte: dieser Wert wird direkt ADDIERT, also du musst nicht nochmal den alten 
# Wert abfragen 

# nicht verwecheln mit: update_daily_counter(user_number, amount )
# hierbei wird direkt der amount gesetzt und nicht addiert
# =============================================================================

# database.update_add_daily_counter(1, 33)

# =============================================================================
# TÄGLICHER KOFFEINCOUNTER ZURÜCKSETZEN
# wirst dunicht brauchen
# dafuer gibt es bereits eine Funktion in der SETUP GUI
# =============================================================================

# database.update_daily_counter(1, 0)


# =============================================================================
# TÄGLICHER KOFFEINCOUNTER und MAX KOFFEIN abfragen

# einfach mit 
# user = database.get_user_by_number(1)  
# user[3] --> MAX KOFFEIN 
# user[5] --> TÄGLICHER KOFFEINCOUNTER 
# auslesen 

# =============================================================================

