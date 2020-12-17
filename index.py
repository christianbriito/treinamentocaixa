#Importação da biblioteca

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#Criação da Janela

Janela = Tk()
Janela.title("Acesso ao Sistema")
Janela.geometry("600x300")
Janela.configure(background="white")
Janela.resizable(width=False, height=False)

#SEPARADORES# ---WIDGETS---
LeftFrame = Frame(Janela, width=100, height=300, bg="midnightblue", relief="raise") #Frame da Esquerda
LeftFrame.pack(side=LEFT)

RightFrame = Frame(Janela, width=470, height=500, bg="midnightblue", relief="raise") #Frame da Direita
RightFrame.pack(side=RIGHT)


#Aba de Login
UserLabel = Label(RightFrame, text="Login:", font=("Century Gothic", 20), bg="midnightblue", fg="white")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=90, y=110)

#Aba de Senha
PassLabel = Label(RightFrame, text="Senha:", font=("Century Gothic", 20), bg="midnightblue", fg="white")
PassLabel.place(x=5, y=170)

PassEntry = ttk.Entry(RightFrame, width=30, show="*")
PassEntry.place(x=100, y=180)

#Botão Login

LoginButton = ttk.Button(RightFrame, text="Login", width=10 )
LoginButton.place(x=120, y=250) 




Janela.mainloop()