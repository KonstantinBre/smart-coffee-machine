import sqlite3
import datetime

class UserDatabase:
    def __init__(self, db_file='user_database.db'):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_number INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                caffeine_amount INTEGER NOT NULL,
                favorite_coffee TEXT NOT NULL,
                daily_counter INTEGER NOT NULL
            )
        ''')
        self.connection.commit()

    def add_user(self, user_number, name, caffeine_amount, favorite_coffee, daily_counter = 0):
        self.cursor.execute('''
            INSERT INTO users (user_number, name, caffeine_amount, favorite_coffee, daily_counter)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_number, name, caffeine_amount, favorite_coffee, daily_counter))
        self.connection.commit()
        
    def delete_user_by_number(self, user_number):
        self.cursor.execute('''
            DELETE FROM users WHERE user_number = ?
        ''', (user_number,))
        self.connection.commit()
        
    def get_user_by_number(self, user_number):
        self.cursor.execute('SELECT * FROM users WHERE user_number = ?', (user_number,))
        return self.cursor.fetchone()
    
    def get_daily_counter(self, user_number):
        try:
            # SQL-Abfrage ausführen, um den daily_counter für den angegebenen Benutzer abzurufen
            self.cursor.execute("SELECT daily_counter FROM users WHERE user_number = ?", (user_number,))
            
            # Ergebnis abrufen
            result = self.cursor.fetchone()

            # Überprüfen, ob ein Ergebnis vorhanden ist
            if result:
                daily_counter = result[0]
                return daily_counter
            else:
                print(f"Benutzer mit der Nummer {user_number} nicht gefunden.")
                return None

        except sqlite3.Error as e:
            print(f"Fehler beim Abrufen des daily_counter: {e}")
            return None

    def update_user(self, user_number, name=None, caffeine_amount=None, favorite_coffee=None, daily_counter=None):
        # Erstelle ein leeres Update-Statement
        update_query = 'UPDATE users SET '
    
        # Überprüfe welche Parameter angegeben wurden und füge sie zum Statement hinzu
        if name is not None:
            update_query += 'name = ?, '
        if caffeine_amount is not None:
            update_query += 'caffeine_amount = ?, '
        if favorite_coffee is not None:
            update_query += 'favorite_coffee = ?, '
        if daily_counter is not None:
            update_query += 'daily_counter = ?, '
    
        # Entferne das letzte Komma und füge die WHERE-Bedingung hinzu
        update_query = update_query.rstrip(', ')
        update_query += ' WHERE user_number = ?'
    
        # Erstelle ein Tupel mit den Werten für das Statement
        values = tuple(filter(None, [name, caffeine_amount, favorite_coffee, user_number, daily_counter]))
    
        # Führe das Update-Statement aus
        self.cursor.execute(update_query, values)
        self.connection.commit()


    def update_caffeine_amount(self, user_number, new_amount):
        self.cursor.execute('''
            UPDATE users 
            SET caffeine_amount = ? 
            WHERE user_number = ?
        ''', (new_amount, user_number))
        self.connection.commit()
        

    def update_favorite_coffee(self, user_number, new_favorite_coffee):
        self.cursor.execute('''
            UPDATE users SET favorite_coffee = ? WHERE user_number = ?
        ''', (new_favorite_coffee, user_number))
        self.connection.commit()
        
    def update_daily_counter(self, user_number, daily_counter):
        self.cursor.execute('''
            UPDATE users SET daily_counter = ? WHERE user_number = ?
        ''', (daily_counter, user_number))
        self.connection.commit()
        

    def update_add_daily_counter(self, user_number, amount_to_add):
        # Zuerst aktuellen Koffeingehalt abrufen
        current_amount = self.get_daily_counter(user_number)

        # Neuen Koffeingehalt berechnen
        new_amount = current_amount + amount_to_add

        # Koffeingehalt in der Datenbank aktualisieren
        self.cursor.execute('''
            UPDATE users
            SET daily_counter = ?
            WHERE user_number = ?
        ''', (new_amount, user_number))
        self.connection.commit()
        
def create_user(number):
    for i in range(1, number): 
        database.add_user(i, '', 0, '', 0)
        

# Beispiel für die Verwendung der Datenbank
database = UserDatabase()

#x Benutzer erstellen 
# create_user(5)



# Koffeinmenge aktualisieren
# database.update_caffeine_amount(1, 150)

# Lieblingskaffee aktualisieren
# database.update_favorite_coffee(2, 'Cappuccino')

# update user 
# database.update_user(1, "Tim", 72, 'caffee', 0)
# database.update_daily_counter(1, 20)

# Benutzer abrufen
user = database.get_user_by_number(1)
# print(database.get_daily_counter(1))
# print(user)
