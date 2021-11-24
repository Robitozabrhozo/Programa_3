#Programa 3

'''
Entradas:
Salidas:
Funcion:
'''

#Cristhian Ureña Ureña
#2021031824

import tkinter as tk
from tkinter import messagebox
from tkinter import Radiobutton
import random
import os
from playsound import playsound
import pickle

#Creamos la ventana principal
ventana=tk.Tk()
ventana.title('Juego Sudoku')
ventana.geometry('340x70')
ventana.config(bg='grey')
ventana.resizable(False,False)
inicio = tk.Label(ventana,text='JuegoSudoku',
                  bg="#29e1f2",font=("Arial Black",34)
)
inicio.grid(row=0,column=0)




#barra de menu y sus componentes
menubar=tk.Menu(ventana)

menubar.add_cascade(label='Jugar',command= lambda:jugar() )

menubar.add_cascade(label='Configurar',command= lambda:configurar())

menubar.add_cascade(label='Ayuda',command= lambda:ayuda() )

menubar.add_cascade(label='Acerca de',command= lambda:showmessage ('Acerca del Programa ',
                                                                 'Creador: Cristhian UU \n'
                                                                   'Nombre del programa: programa_3_Cristhian_Ureña_Ureña'
                                                                 '\n Version:1.0 \n Fecha de creacion 1/12/2021' ) )

menubar.add_cascade(label='Salir',command= lambda: salir() )

ventana.configure(menu=menubar)




def jugar():

    
    #se crea la ventana del juego
    juego=tk.Toplevel(ventana)
    juego.title('2048')
    juego.geometry('900x740')
    juego.config(bg='#ffdb80')
    juego.resizable(False,False)

    


















#funcion ayuda
'''
Entradas: un click en la interfaz
Salidas: un pdf
Funcion: abre un pdf con el manual de usuario
'''
def ayuda():

    os.startfile('manual_de_usuario_2048.pdf')



#funcion showmessage
'''
Entradas: dos string
Salidas: interfaz estilo cuandro de texto
Funcion: proyecta un cuadro de texto con el titulo y el mensaje indicado
'''
def showmessage(titulo, mensaje):
    messagebox.showinfo(titulo,mensaje)
#funcion salir
'''
Entradas: un click en la interfaz
Salidas: nada 
Funcion: cierra el programa cuando se activa
'''

def salir():

    ventana.destroy()










ventana.mainloop()
