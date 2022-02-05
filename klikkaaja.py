#!/usr/bin/python3

# Klikkaaja

from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title('Klikkaaja')
ws.geometry('500x300')
#ws.config(bg='#ccc')
ws.config(bg='green')

def msg1():
    messagebox.showinfo('Infoo', 'Hei, tässä ois infoo!')
    messagebox.showerror('Virhe', 'Joku meni pieleen!')
    messagebox.showwarning('Varoitus', 'Siis jotain tapahtui!')
    messagebox.askquestion('Kysymys', 'Haluatko jatkaa?')
    messagebox.askokcancel('Ok Peruuta', 'Oletko ihan varma?')
    messagebox.askyesno('Kyllä|Ei', 'Siis, tota, niinku jatketaanko?')
    messagebox.askretrycancel('Uudelleen?', 'Ei onnistunu! Yritetäänkö uudelleen?')

Button(ws, text='Klikkaa mua', command=msg1).pack(pady=50)

ws.mainloop()
