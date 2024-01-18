# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 16:18:04 2023

@author: konst
"""

import tkinter as tk
import time


#%% Database 
from database import UserDatabase
database = UserDatabase()


#%% funcrions 
def safe_data():
    print('Daten speichern und so ...')
    name = T_name.get("1.0", "end-1c")
    caffeine_amount = scale.get()
    favorite_coffee = fav_cafe.get()
    
    print(name)
    print(caffeine_amount)
    print(favorite_coffee)
    
    database.update_user(user_number, name, caffeine_amount, favorite_coffee)
    
def reset_data():
    print(f'daily caffein counter: {database.get_daily_counter(user_number)}')
    print('RESET....')
    database.update_daily_counter(user_number, 0)
    print(f'new daily caffein counter: {database.get_daily_counter(user_number)}')
    
    
def show_data():
    popup = tk.Toplevel(root)
    popup.title("User Info")
    print()
    
    user = database.get_user_by_number(1)
    label = tk.Label(popup, anchor="w", justify='left',text=f"Name: \t\t{user[1]}\nKoffeinmenge \t{user[2]}\nFavorit: \t\t{user[3]}\nCounter: \t{user[4]}")
    label.pack(padx=10, pady=10)
    
    close_button = tk.Button(popup, text="Close", command= popup.destroy)
    close_button.pack(pady=10)
    
    
def getTextInput():
    result = T.get(1.0, tk.END + "-1c")
    return result


def delete_text():
    T.delete("1.0", "end")
    configure_state(layout_setup+layout_setup2, tk.DISABLED)
    
def start_clicked(object):
    
    # b1.config(state=tk.DISABLED)
    
    object.pack_forget()
 
    print('Ich bin am arbeiten')
    time.sleep(1)
    delete_text()
    
    # Hier müsste dann die Funkion kommen, um ML zu starten, user speichern
    T.insert(tk.END, f"Willkommen Benutzer {user_number}\nWahrscheinlichkeit 99%")

    
    
    object.pack()
    object.place(x=180, y=90, anchor= 'center')
    
    configure_state(layout_setup, tk.ACTIVE)
    configure_state(layout_setup2, tk.NORMAL)
    
    fav_cafe.set(None)
     
def configure_state(radiobuttons, state):
    for rb in radiobuttons:
        rb.config(state=state)
        
def on_scale_change(value):
    print(value)
    value = int(value)
    result = value/40
    label.config(text= f"{value} mg = {result:.1f} Kaffee")
    
#%% Variables 

x_data = 150     
user_number = 1

root = tk.Tk()

# specify size of window.
root.geometry("350x350")

b1 = tk.Button(root, height=2, width=12, text = "Scan User", command = lambda: start_clicked(b1), state="normal" )


# Create text widget and specify size.
T = tk.Text(root, height = 2, width = 24)

# Create label
l = tk.Label(root, text = "Setup")
l.config(font =("Courier", 10))

l2 = tk.Label(root, text = "Name", justify="left")
l2.config(font =("Courier", 10))
l2.place(x=0, y=180)
l3 = tk.Label(root, text = "maximale\nKoffeinmenge", justify="left")
l3.config(font =("Courier", 10))
l3.place(x=0, y=205)
# l4 = tk.Label(root, text = "Alter", justify="left")
# l4.config(font =("Courier", 10))
# l4.place(x=0, y=220)
l5 = tk.Label(root, text = "Lieblingskaffee", justify="left")
l5.config(font =("Courier", 10))
l5.place(x=0, y=240)


T_name = tk.Text(root, height = 1, width = 19)
T_name.config(state=tk.DISABLED)
T_name.place(x=x_data, y=180)

# geschlecht = 0
# R1 = tk.Radiobutton(root, text="Männlich", variable=geschlecht, value=1)
# R1.place(x=x_data-5, y=200)
# R2 = tk.Radiobutton(root, text="Weiblich", variable=geschlecht, value=2)
# R2.place(x=x_data+70, y=200)


cb1 = tk.Checkbutton(root, )
# Create button for next text.
b2 = tk.Button(root, text = "Delete", command = delete_text )
# b3 = tk.Button(root, text = 'Lieblingskaffe')
# b4 = tk.Button(root, text = 'Surprise')
b5 = tk.Button(root, text = 'Speichern', command = safe_data)
b6 = tk.Button(root, text = 'Reset', command = reset_data)
b7 = tk.Button(root, text = 'Show', command = show_data)
b2.place(x=275, y=25)
b1.place(x=180, y=90, anchor= 'center')
# b3.place(x=160, y=140)
# b4.place(x=90, y=140)
b5.place(x=150, y=300)
b6.place(x=225, y=300)
b7.place(x=100, y=300)


# T_age = tk.Text(root, height = 1, width = 12)
# T_age.place(x=x_data, y=220)

label = tk.Label(root, text= "40 mg ≙ 1 Kaffee")
label.place(x = 180, y = 200)

max_koffein = 0
scale = tk.Scale( root, variable = max_koffein, showvalue=False, orient="horizontal", length= 155, from_=0, to_=400, resolution=20, command=on_scale_change)
scale.place(x= x_data-2, y = 220 )



fav_cafe = tk.StringVar()
R3 = tk.Radiobutton(root, text="Filterkaffee", variable=fav_cafe, value='Filterkaffee')
R3.place(x=x_data-5, y=240)
R4 = tk.Radiobutton(root, text="Espresso", variable=fav_cafe, value='Espresso')
R4.place(x=x_data+110, y=240)
R5 = tk.Radiobutton(root, text="Latte Macchiato", variable=fav_cafe, value='Latte Macchiato')
R5.place(x=x_data-5, y=260)
R6 = tk.Radiobutton(root, text="Cappuccino", variable=fav_cafe, value='Cappuccino')
R6.place(x=x_data+110, y=260)



layout_setup = [R3, R4, R4, R5, R6,  b5, b6, b7]#b3, b4,
layout_setup2 = [T_name, scale]
configure_state(layout_setup+layout_setup2, tk.DISABLED)


l.pack()
T.pack()



tk.mainloop()

    
