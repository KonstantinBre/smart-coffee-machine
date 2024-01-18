# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 16:18:04 2023

@author: konst
"""

import tkinter as tk
import time



def getTextInput():
    result = T.get(1.0, tk.END + "-1c")
    return result

def delete_text():

    T.delete("1.0", "end")
    b3.config(state=tk.DISABLED)
    b4.config(state=tk.DISABLED)
    

def start_clicked(object):
    
    # b1.config(state=tk.DISABLED)
    
    object.pack_forget()
 
    print('Ich bin am arbeiten')
    time.sleep(3)
    delete_text()
    T.insert(tk.END, "Willkommen Tim\nWahrscheinlichkeit 99%")
    
    object.pack()
    object.place(x=160, y=110)
    
    b3.config(state=tk.ACTIVE)
    b4.config(state=tk.ACTIVE)
    
    # b1.config(state=tk.ACTIVE)
    
     

root = tk.Tk()

# specify size of window.
root.geometry("300x200")

b1 = tk.Button(root, text = "Start ML", command = lambda: start_clicked(b1), state="normal" )


# Create text widget and specify size.
T = tk.Text(root, height = 5, width = 50)

# Create label
l = tk.Label(root, text = "Smart ass coffemaker")
l.config(font =("Courier", 12))

# Create button for next text.
b2 = tk.Button(root, text = "Delete", command = delete_text )
b3 = tk.Button(root, text = 'Lieblingskaffe')
b4 = tk.Button(root, text = 'Surprise')
b2.place(x=90, y=110)
b1.place(x=160, y=110)
b3.place(x=160, y=140)
b4.place(x=90, y=140)
b3.config(state=tk.DISABLED)
b4.config(state=tk.DISABLED)

l.pack()
T.pack()


tk.mainloop()

    
