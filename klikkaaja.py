#!/usr/bin/python3

# Klikkaaja

from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title('Klikkaaja')
ws.geometry('300x200')
ws.config(bg='#554477')

def msg1():
    messagebox.showinfo('information', 'Hei, tässä ois infoo!')
    messagebox.showerror('error', 'Joku meni pieleen!')
    messagebox.showwarning('warning', 'Varoitus! Siis jotain tapahtui!')
    messagebox.askquestion('Ask Question', 'Haluatko jatkaa?')
    messagebox.askokcancel('Ok Cancel', 'Oletko ihan varma?')
    messagebox.askyesno('Yes|No', 'Siis, tota, niinku jatketaanko?')
    messagebox.askretrycancel('retry', 'Ei onnistunu! Yritetäänkö uudelleen?')

Button(ws, text='Klikkaa mua', command=msg1).pack(pady=50)

ws.mainloop()
