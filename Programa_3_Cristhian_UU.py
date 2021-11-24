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
ventana.geometry('340x330')
ventana.config(bg='grey')
ventana.resizable(False,False)
inicio = tk.Label(ventana,text='JuegoSudoku',
                  bg="#29e1f2",font=("Arial Black",34)
)
inicio.grid(row=0,column=0)




#barra de menu y sus componentes

jugar_boton= tk.Button(ventana,text='Jugar',
                              bg='#00d9fa', activebackground = '#3091db',height=2,width=10 ,command= lambda:jugar())
jugar_boton.grid(row=1,column=0,pady=5)

configurar_boton= tk.Button(ventana,text='Configurar',
                              bg='#00d9fa', activebackground = '#3091db',height=2,width=10 ,command= lambda:configurar())
configurar_boton.grid(row=2,column=0,pady=5)

ayuda_boton= tk.Button(ventana,text='Ayuda',
                              bg='#00d9fa', activebackground = '#3091db',height=2,width=10,command= lambda:ayuda() )
ayuda_boton.grid(row=3,column=0,pady=5)
    
Acerca_de_boton= tk.Button(ventana,text='Acerca de',
                              bg='#00d9fa', activebackground = '#3091db',height=2,width=10 ,command= lambda:showmessage ('Acerca del Programa ',
                                                                 'Creador: Cristhian UU \n'
                                                                   'Nombre del programa: programa_3_Cristhian_Ureña_Ureña'
                                                                 '\n Version:1.0 \n Fecha de creacion 1/12/2021' ))
Acerca_de_boton.grid(row=4,column=0,pady=5)

Salir_boton= tk.Button(ventana,text='Salir',
                              bg='#00d9fa', activebackground = '#3091db',height=2,width=10 ,command= lambda: salir() )
Salir_boton.grid(row=5,column=0,pady=5)






def jugar():

    
    #se crea la ventana del juego
    juego=tk.Toplevel(ventana)
    juego.title('Sudoku')
    juego.geometry('900x740')
    juego.config(bg='#b2ff17')
    juego.resizable(False,False)


    #se crean los frames a utilizar:

    titulo_frame = tk.Frame(juego,height=128,width=540)
    titulo_frame.grid(row=0,column=0,padx=1,pady=1)
    
    nombre_frame = tk.Frame(juego,bg='#b2ff17',height=128,width=350)
    nombre_frame.grid(row=0,column=1,padx=1,pady=1)

    partida_frame = tk.Frame(juego,bg="#b2ff17",height=450,width=540)
    partida_frame.grid(row=1,column=0,padx=1,pady=1)

    numeral_frame = tk.Frame(juego,bg="#ffdb80",height=450,width=350)
    numeral_frame.grid(row=1,column=1,padx=1,pady=1)
    #se hace un frame dentro del frame de numeral
    numeros_frame = tk.Frame(numeral_frame,bg="#b2ff17",height=225,width=350)
    numeros_frame.grid(row=0,column=0,padx=1,pady=1)
    
    botones_frame = tk.Frame(numeral_frame,bg="#4c05ff",height=225,width=350)
    botones_frame.grid(row=1,column=0,padx=1,pady=1)
    ################################################
    cronometro_frame = tk.Frame(juego,bg="#c105ff",height=315,width=540)
    cronometro_frame.grid(row=2,column=0,padx=1,pady=1)

    botones2_frame = tk.Frame(juego,bg="#ff05e6",height=315,width=350)
    botones2_frame.grid(row=2,column=1,padx=1,pady=1)

    #se crean los botones e interfaz Gráfica

    #TITULO
    titulo = tk.Label(titulo_frame,text='Sudoku',font=("Arial Black",54),bg='#b2ff17')
    titulo.grid(row=0,column=0)

    #NOMBRE
    nombre_label=tk.Label(nombre_frame,text='Nombre del jugador',font=("Arial Black",12),bg='#b2ff17')
    nombre_label.grid(row=0,column=0)
    
    nombre_entry=tk.Entry(nombre_frame,bg='#ffffff',width=40) 
    nombre_entry.grid(row=1,column=0)

    nombre_boton= tk.Button(nombre_frame,text=' Guardar \n Nombre',
                              bg='#00d9fa', activebackground = '#3091db',height=2,width=10 )
    nombre_boton.grid(row=2,column=0,pady=2)
    

    #CUADRO DE JUEGO
    matriz=[]
    
    for x in range (3):
        for y in range (3):
            partida2_frame = tk.Frame(partida_frame,bg="#b2ff17")
            partida2_frame.grid(row=x,column=y,padx=5,pady=5)
            for i in range(3):
                fila = []
                for j in range(3):
                    cuadro =  tk.Button(partida2_frame,text='',
                                      bg='#e4e9f2', activebackground = '#a5a9b0',height=2,width=6,state='disabled' )
                    cuadro.grid(row=i,column=j,padx=2,pady=2)
                    fila.append(cuadro)
                matriz.append(fila)

    #NUMEROS
    

    boton_1 =  tk.Button(numeros_frame,text='1',
                              bg='#29f2de', activebackground = '#51db7b',height=1,width=3,font=("Arial Black",14))
    boton_1.grid(row=0,column=0,padx=3,pady=3)

    boton_2 =  tk.Button(numeros_frame,text='2',
                              bg='#29f2de', activebackground = '#51db7b',height=1,width=3,font=("Arial Black",14))
    boton_2.grid(row=0,column=1,padx=3,pady=3)

    boton_3 =  tk.Button(numeros_frame,text='3',
                              bg='#29f2de', activebackground = '#51db7b',height=1,width=3,font=("Arial Black",14))
    boton_3.grid(row=0,column=2,padx=3,pady=3)
    ###########################################
    boton_4 =  tk.Button(numeros_frame,text='4',
                              bg='#29f2de', activebackground = '#51db7b',height=1,width=3,font=("Arial Black",14))
    boton_4.grid(row=1,column=0,padx=3,pady=3)

    boton_5 =  tk.Button(numeros_frame,text='5',
                              bg='#29f2de', activebackground = '#51db7b',height=1,width=3,font=("Arial Black",14))
    boton_5.grid(row=1,column=1,padx=3,pady=3)

    boton_6 =  tk.Button(numeros_frame,text='6',
                              bg='#29f2de', activebackground = '#51db7b',height=1,width=3,font=("Arial Black",14))
    boton_6.grid(row=1,column=2,padx=3,pady=3)
    ###########################################
    boton_7 =  tk.Button(numeros_frame,text='7',
                              bg='#29f2de', activebackground = '#51db7b',height=1,width=3,font=("Arial Black",14))
    boton_7.grid(row=2,column=0,padx=3,pady=3)

    boton_8 =  tk.Button(numeros_frame,text='8',
                              bg='#29f2de', activebackground = '#51db7b',height=1,width=3,font=("Arial Black",14))
    boton_8.grid(row=2,column=1,padx=3,pady=3)

    boton_9 =  tk.Button(numeros_frame,text='9',
                              bg='#29f2de', activebackground = '#51db7b',height=1,width=3,font=("Arial Black",14))
    boton_9.grid(row=2,column=2,padx=3,pady=3)
    ###########################################



    #BOTONES DE JUEGO
    
    #CRONOMETRO Y TIMER
    
    #BOTONES DE GUARDAR Y CARGAR















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
