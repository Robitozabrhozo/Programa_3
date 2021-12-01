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
from functools import partial
from copy import deepcopy
inicio_juego=0
#config
#              reloj   tiempo en timer  dificutad  topx   tipo_numeral
configuracion=[1,       (0,0,0),        1,         0,     ['1','2','3','4','5','6','7','8','9'] ]
datos_timer=(0,0,0)
tipo_numeral=['1','2','3','4','5','6','7','8','9']
topx=0
#nombre
nombre=''
#tiempo
time_out=0
tiempo=(0,0,0)
h=0
m=0
s=0
#lista actual de numeros
lista=[ [ [[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]] ],
        [ [[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]] ],
        [ [[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]] ]  ]
lista_inicial=[]
#Numeral
numero_actual=0
#jugadas
jugadas=[]
jugadas_eliminadas=[]
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
                              bg='#00d9fa', activebackground = '#3091db',height=2,width=10 ,command= lambda:configuracion_sudoku())
configurar_boton.grid(row=2,column=0,pady=5)

ayuda_boton= tk.Button(ventana,text='Ayuda',
                              bg='#00d9fa', activebackground = '#3091db',height=2,width=10,command= lambda:ayuda() )
ayuda_boton.grid(row=3,column=0,pady=5)
    
Acerca_de_boton= tk.Button(ventana,text='Acerca de',
                              bg='#00d9fa', activebackground = '#3091db',height=2,width=10 ,command= lambda:messagebox.showinfo('Acerca del Programa ',
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

    #funcion showmessage
    '''
    Entradas: dos string
    Salidas: interfaz estilo cuandro de texto
    Funcion: proyecta un cuadro de texto con el titulo y el mensaje indicado
    '''
    def showmessage(titulo, mensaje):
        messagebox.showinfo(titulo,mensaje,parent=juego)
        
    #se crean los frames a utilizar:

    titulo_frame = tk.Frame(juego,height=128,width=540,bg='#04b020')
    titulo_frame.grid(row=0,column=0,padx=1,pady=1)
    
    nombre_frame = tk.Frame(juego,bg='#b2ff17',height=128,width=350)
    nombre_frame.grid(row=0,column=1,padx=1,pady=1)

    partida_frame = tk.Frame(juego,bg="#b2ff17",height=450,width=540)
    partida_frame.grid(row=1,column=0,padx=1,pady=1)

    numeral_frame = tk.Frame(juego,bg="#b2ff17",height=450,width=350)
    numeral_frame.grid(row=1,column=1,padx=1,pady=1)
    #se hace un frame dentro del frame de numeral
    numeros_frame = tk.Frame(numeral_frame,bg="#b2ff17",height=225,width=350)
    numeros_frame.grid(row=0,column=0,padx=1,pady=1)
    
    botones_frame = tk.Frame(numeral_frame,bg="#b2ff17",height=225,width=350)
    botones_frame.grid(row=1,column=0,padx=1,pady=1)
    ################################################
    cronometro_frame = tk.Frame(juego,bg="#b2ff17",height=115,width=540)
    cronometro_frame.grid(row=2,column=0,padx=1,pady=1)

    botones2_frame = tk.Frame(juego,bg="#b2ff17",height=115,width=350)
    botones2_frame.grid(row=2,column=1,padx=1,pady=1)

    #se crean los botones e interfaz Gráfica

    #TITULO
    titulo = tk.Label(titulo_frame,text='     Sudoku     ',font=("Arial Black",54),bg='#b2ff17')
    titulo.grid(row=0,column=0,pady=3,padx=3)

    #NOMBRE
    nombre_label=tk.Label(nombre_frame,text='Nombre del jugador',font=("Arial Black",12),bg='#b2ff17')
    nombre_label.grid(row=0,column=0)
    
    nombre_entry=tk.Entry(nombre_frame,bg='#ffffff',width=40) 
    nombre_entry.grid(row=1,column=0)

    nombre_boton= tk.Button(nombre_frame,text=' Guardar \n Nombre',
                              bg='#00d9fa', activebackground = '#3091db',height=2,width=10,command=lambda:guardar_nombre() )
    nombre_boton.grid(row=2,column=0,pady=2)
    

    #CUADRO DE JUEGO
    
    def resetear_juego():
        for x in range (3):
            for y in range (3):
                partida2_frame = tk.Frame(partida_frame,bg="#b2ff17")
                partida2_frame.grid(row=x,column=y,padx=5,pady=5)
                for i in range(3):
                    for j in range(3):
                        cuadro =  tk.Button(partida2_frame,text='',
                                          bg='#e4e9f2', activebackground = '#a5a9b0',height=2,width=6,state='disabled' )
                        cuadro.grid(row=i,column=j,padx=2,pady=2)
    resetear_juego()
                
    

    #NUMEROS
    #se hace una funcion para cada numero la cual despliega todos lo demas numeros y se selecciona a si mismo

    boton_1 =  tk.Button(numeros_frame,text=configuracion[4][0],
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero1(),state='disabled')
    boton_1.grid(row=0,column=0,padx=3,pady=3)

    boton_2 =  tk.Button(numeros_frame,text=configuracion[4][1],
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero2(),state='disabled')
    boton_2.grid(row=0,column=1,padx=3,pady=3)

    boton_3 =  tk.Button(numeros_frame,text=configuracion[4][2],
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero3(),state='disabled')
    boton_3.grid(row=0,column=2,padx=3,pady=3)
    ###########################################
    boton_4 =  tk.Button(numeros_frame,text=configuracion[4][3],
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero4(),state='disabled')
    boton_4.grid(row=1,column=0,padx=3,pady=3)

    boton_5 =  tk.Button(numeros_frame,text=configuracion[4][4],
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero5(),state='disabled')
    boton_5.grid(row=1,column=1,padx=3,pady=3)

    boton_6 =  tk.Button(numeros_frame,text=configuracion[4][5],
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero6(),state='disabled')
    boton_6.grid(row=1,column=2,padx=3,pady=3)
    ###########################################
    boton_7 =  tk.Button(numeros_frame,text=configuracion[4][6],
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero7(),state='disabled')
    boton_7.grid(row=2,column=0,padx=3,pady=3)

    boton_8 =  tk.Button(numeros_frame,text=configuracion[4][7],
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero8(),state='disabled')
    boton_8.grid(row=2,column=1,padx=3,pady=3)

    boton_9 =  tk.Button(numeros_frame,text=configuracion[4][8],
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero9(),state='disabled')
    boton_9.grid(row=2,column=2,padx=3,pady=3)

    def numero1():
        global numero_actual 
        numero_actual=1
        boton_1 =  tk.Button(numeros_frame,text=configuracion[4][0],
                              bg='#51db7b', activebackground = '#bac2bd',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero1(),state='disabled')
        boton_1.grid(row=0,column=0,padx=3,pady=3)

        boton_2 =  tk.Button(numeros_frame,text=configuracion[4][1],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero2())
        boton_2.grid(row=0,column=1,padx=3,pady=3)

        boton_3 =  tk.Button(numeros_frame,text=configuracion[4][2],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero3())
        boton_3.grid(row=0,column=2,padx=3,pady=3)
        ###########################################
        boton_4 =  tk.Button(numeros_frame,text=configuracion[4][3],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero4())
        boton_4.grid(row=1,column=0,padx=3,pady=3)

        boton_5 =  tk.Button(numeros_frame,text=configuracion[4][4],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero5())
        boton_5.grid(row=1,column=1,padx=3,pady=3)

        boton_6 =  tk.Button(numeros_frame,text=configuracion[4][5],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero6())
        boton_6.grid(row=1,column=2,padx=3,pady=3)
        ###########################################
        boton_7 =  tk.Button(numeros_frame,text=configuracion[4][6],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero7())
        boton_7.grid(row=2,column=0,padx=3,pady=3)

        boton_8 =  tk.Button(numeros_frame,text=configuracion[4][7],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero8())
        boton_8.grid(row=2,column=1,padx=3,pady=3)

        boton_9 =  tk.Button(numeros_frame,text=configuracion[4][8],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero9())
        boton_9.grid(row=2,column=2,padx=3,pady=3)
        
        
    ###########################################
    def numero2():
        global numero_actual 
        numero_actual=2
        boton_1 =  tk.Button(numeros_frame,text=configuracion[4][0],
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero1())
        boton_1.grid(row=0,column=0,padx=3,pady=3)

        boton_2 =  tk.Button(numeros_frame,text=configuracion[4][1],
                                  bg='#51db7b', activebackground = '#bac2bd',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero2(),state='disabled')
        boton_2.grid(row=0,column=1,padx=3,pady=3)

        boton_3 =  tk.Button(numeros_frame,text=configuracion[4][2],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero3())
        boton_3.grid(row=0,column=2,padx=3,pady=3)
        ###########################################
        boton_4 =  tk.Button(numeros_frame,text=configuracion[4][3],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero4())
        boton_4.grid(row=1,column=0,padx=3,pady=3)

        boton_5 =  tk.Button(numeros_frame,text=configuracion[4][4],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero5())
        boton_5.grid(row=1,column=1,padx=3,pady=3)

        boton_6 =  tk.Button(numeros_frame,text=configuracion[4][5],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero6())
        boton_6.grid(row=1,column=2,padx=3,pady=3)
        ###########################################
        boton_7 =  tk.Button(numeros_frame,text=configuracion[4][6],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero7())
        boton_7.grid(row=2,column=0,padx=3,pady=3)

        boton_8 =  tk.Button(numeros_frame,text=configuracion[4][7],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero8())
        boton_8.grid(row=2,column=1,padx=3,pady=3)

        boton_9 =  tk.Button(numeros_frame,text=configuracion[4][8],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero9())
        boton_9.grid(row=2,column=2,padx=3,pady=3)

    def numero3():
        global numero_actual
        numero_actual=3
        boton_1 =  tk.Button(numeros_frame,text=configuracion[4][0],
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero1())
        boton_1.grid(row=0,column=0,padx=3,pady=3)

        boton_2 =  tk.Button(numeros_frame,text=configuracion[4][1],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero2())
        boton_2.grid(row=0,column=1,padx=3,pady=3)

        boton_3 =  tk.Button(numeros_frame,text=configuracion[4][2],
                                  bg='#51db7b', activebackground = '#bac2bd',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero3(),state='disabled')
        boton_3.grid(row=0,column=2,padx=3,pady=3)
        ###########################################
        boton_4 =  tk.Button(numeros_frame,text=configuracion[4][3],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero4())
        boton_4.grid(row=1,column=0,padx=3,pady=3)

        boton_5 =  tk.Button(numeros_frame,text=configuracion[4][4],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero5())
        boton_5.grid(row=1,column=1,padx=3,pady=3)

        boton_6 =  tk.Button(numeros_frame,text=configuracion[4][5],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero6())
        boton_6.grid(row=1,column=2,padx=3,pady=3)
        ###########################################
        boton_7 =  tk.Button(numeros_frame,text=configuracion[4][6],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero7())
        boton_7.grid(row=2,column=0,padx=3,pady=3)

        boton_8 =  tk.Button(numeros_frame,text=configuracion[4][7],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero8())
        boton_8.grid(row=2,column=1,padx=3,pady=3)

        boton_9 =  tk.Button(numeros_frame,text=configuracion[4][8],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero9())
        boton_9.grid(row=2,column=2,padx=3,pady=3)

    def numero4():
        global numero_actual
        numero_actual=4
       
        
        boton_1 =  tk.Button(numeros_frame,text=configuracion[4][0],
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero1())
        boton_1.grid(row=0,column=0,padx=3,pady=3)

        boton_2 =  tk.Button(numeros_frame,text=configuracion[4][1],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero2())
        boton_2.grid(row=0,column=1,padx=3,pady=3)

        boton_3 =  tk.Button(numeros_frame,text=configuracion[4][2],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero3())
        boton_3.grid(row=0,column=2,padx=3,pady=3)
        ###########################################
        boton_4 =  tk.Button(numeros_frame,text=configuracion[4][3],
                                  bg='#51db7b', activebackground = '#bac2bd',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero4(),state='disabled')
        boton_4.grid(row=1,column=0,padx=3,pady=3)

        boton_5 =  tk.Button(numeros_frame,text=configuracion[4][4],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero5())
        boton_5.grid(row=1,column=1,padx=3,pady=3)

        boton_6 =  tk.Button(numeros_frame,text=configuracion[4][5],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero6())
        boton_6.grid(row=1,column=2,padx=3,pady=3)
        ###########################################
        boton_7 =  tk.Button(numeros_frame,text=configuracion[4][6],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero7())
        boton_7.grid(row=2,column=0,padx=3,pady=3)

        boton_8 =  tk.Button(numeros_frame,text=configuracion[4][7],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero8())
        boton_8.grid(row=2,column=1,padx=3,pady=3)

        boton_9 =  tk.Button(numeros_frame,text=configuracion[4][8],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero9())
        boton_9.grid(row=2,column=2,padx=3,pady=3)
        
    def numero5():
        global numero_actual
        numero_actual=5
        boton_1 =  tk.Button(numeros_frame,text=configuracion[4][0],
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero1())
        boton_1.grid(row=0,column=0,padx=3,pady=3)

        boton_2 =  tk.Button(numeros_frame,text=configuracion[4][1],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero2())
        boton_2.grid(row=0,column=1,padx=3,pady=3)

        boton_3 =  tk.Button(numeros_frame,text=configuracion[4][2],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero3())
        boton_3.grid(row=0,column=2,padx=3,pady=3)
        ###########################################
        boton_4 =  tk.Button(numeros_frame,text=configuracion[4][3],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero4())
        boton_4.grid(row=1,column=0,padx=3,pady=3)

        boton_5 =  tk.Button(numeros_frame,text=configuracion[4][4],
                                  bg='#51db7b', activebackground = '#bac2bd',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero5(),state='disabled')
        boton_5.grid(row=1,column=1,padx=3,pady=3)

        boton_6 =  tk.Button(numeros_frame,text=configuracion[4][5],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero6())
        boton_6.grid(row=1,column=2,padx=3,pady=3)
        ###########################################
        boton_7 =  tk.Button(numeros_frame,text=configuracion[4][6],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero7())
        boton_7.grid(row=2,column=0,padx=3,pady=3)

        boton_8 =  tk.Button(numeros_frame,text=configuracion[4][7],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero8())
        boton_8.grid(row=2,column=1,padx=3,pady=3)

        boton_9 =  tk.Button(numeros_frame,text=configuracion[4][8],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero9())
        boton_9.grid(row=2,column=2,padx=3,pady=3)

        
    def numero6():
        global numero_actual 
        numero_actual=6
       
        boton_1 =  tk.Button(numeros_frame,text=configuracion[4][0],
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero1())
        boton_1.grid(row=0,column=0,padx=3,pady=3)

        boton_2 =  tk.Button(numeros_frame,text=configuracion[4][1],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero2())
        boton_2.grid(row=0,column=1,padx=3,pady=3)

        boton_3 =  tk.Button(numeros_frame,text=configuracion[4][2],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero3())
        boton_3.grid(row=0,column=2,padx=3,pady=3)
        ###########################################
        boton_4 =  tk.Button(numeros_frame,text=configuracion[4][3],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero4())
        boton_4.grid(row=1,column=0,padx=3,pady=3)

        boton_5 =  tk.Button(numeros_frame,text=configuracion[4][4],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero5())
        boton_5.grid(row=1,column=1,padx=3,pady=3)

        boton_6 =  tk.Button(numeros_frame,text=configuracion[4][5],
                                  bg='#51db7b', activebackground = '#bac2bd',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero6(),state='disabled')
        ###########################################
        boton_7 =  tk.Button(numeros_frame,text=configuracion[4][6],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero7())
        boton_7.grid(row=2,column=0,padx=3,pady=3)

        boton_8 =  tk.Button(numeros_frame,text=configuracion[4][7],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero8())
        boton_8.grid(row=2,column=1,padx=3,pady=3)

        boton_9 =  tk.Button(numeros_frame,text=configuracion[4][8],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero9())
        boton_9.grid(row=2,column=2,padx=3,pady=3)
        
    def numero7():
        global numero_actual 
        numero_actual=7

        boton_1 =  tk.Button(numeros_frame,text=configuracion[4][0],
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero1())
        boton_1.grid(row=0,column=0,padx=3,pady=3)

        boton_2 =  tk.Button(numeros_frame,text=configuracion[4][1],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero2())
        boton_2.grid(row=0,column=1,padx=3,pady=3)

        boton_3 =  tk.Button(numeros_frame,text=configuracion[4][2],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero3())
        boton_3.grid(row=0,column=2,padx=3,pady=3)
        ###########################################
        boton_4 =  tk.Button(numeros_frame,text=configuracion[4][3],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero4())
        boton_4.grid(row=1,column=0,padx=3,pady=3)

        boton_5 =  tk.Button(numeros_frame,text=configuracion[4][4],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero5())
        boton_5.grid(row=1,column=1,padx=3,pady=3)

        boton_6 =  tk.Button(numeros_frame,text=configuracion[4][5],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero6())
        boton_6.grid(row=1,column=2,padx=3,pady=3)
        ###########################################
        boton_7 =  tk.Button(numeros_frame,text=configuracion[4][6],
                                  bg='#51db7b', activebackground = '#bac2bd',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero7(),state='disabled')
        boton_7.grid(row=2,column=0,padx=3,pady=3)

        boton_8 =  tk.Button(numeros_frame,text=configuracion[4][7],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero8())
        boton_8.grid(row=2,column=1,padx=3,pady=3)

        boton_9 =  tk.Button(numeros_frame,text=configuracion[4][8],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero9())
        boton_9.grid(row=2,column=2,padx=3,pady=3)
    def numero8():
        global numero_actual
        numero_actual=8

        boton_1 =  tk.Button(numeros_frame,text=configuracion[4][0],
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero1())
        boton_1.grid(row=0,column=0,padx=3,pady=3)

        boton_2 =  tk.Button(numeros_frame,text=configuracion[4][1],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero2())
        boton_2.grid(row=0,column=1,padx=3,pady=3)

        boton_3 =  tk.Button(numeros_frame,text=configuracion[4][2],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero3())
        boton_3.grid(row=0,column=2,padx=3,pady=3)
        ###########################################
        boton_4 =  tk.Button(numeros_frame,text=configuracion[4][3],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero4())
        boton_4.grid(row=1,column=0,padx=3,pady=3)

        boton_5 =  tk.Button(numeros_frame,text=configuracion[4][4],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero5())
        boton_5.grid(row=1,column=1,padx=3,pady=3)

        boton_6 =  tk.Button(numeros_frame,text=configuracion[4][5],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero6())
        boton_6.grid(row=1,column=2,padx=3,pady=3)
        ###########################################
        boton_7 =  tk.Button(numeros_frame,text=configuracion[4][6],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero7())
        boton_7.grid(row=2,column=0,padx=3,pady=3)

        boton_8 =  tk.Button(numeros_frame,text=configuracion[4][7],
                                  bg='#51db7b', activebackground = '#bac2bd',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero8(),state='disabled')
        boton_8.grid(row=2,column=1,padx=3,pady=3)

        boton_9 =  tk.Button(numeros_frame,text=configuracion[4][8],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero9())
        boton_9.grid(row=2,column=2,padx=3,pady=3)
    def numero9():
        global numero_actual
        numero_actual=9
        boton_1 =  tk.Button(numeros_frame,text=configuracion[4][0],
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero1())
        boton_1.grid(row=0,column=0,padx=3,pady=3)

        boton_2 =  tk.Button(numeros_frame,text=configuracion[4][1],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero2())
        boton_2.grid(row=0,column=1,padx=3,pady=3)

        boton_3 =  tk.Button(numeros_frame,text=configuracion[4][2],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero3())
        boton_3.grid(row=0,column=2,padx=3,pady=3)
        ###########################################
        boton_4 =  tk.Button(numeros_frame,text=configuracion[4][3],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero4())
        boton_4.grid(row=1,column=0,padx=3,pady=3)

        boton_5 =  tk.Button(numeros_frame,text=configuracion[4][4],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero5())
        boton_5.grid(row=1,column=1,padx=3,pady=3)

        boton_6 =  tk.Button(numeros_frame,text=configuracion[4][5],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero6())
        boton_6.grid(row=1,column=2,padx=3,pady=3)
        ###########################################
        boton_7 =  tk.Button(numeros_frame,text=configuracion[4][6],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero7())
        boton_7.grid(row=2,column=0,padx=3,pady=3)

        boton_8 =  tk.Button(numeros_frame,text=configuracion[4][7],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero8())
        boton_8.grid(row=2,column=1,padx=3,pady=3)

        boton_9 =  tk.Button(numeros_frame,text=configuracion[4][8],
                                  bg='#51db7b', activebackground = '#bac2bd',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero9(),state='disabled')
        boton_9.grid(row=2,column=2,padx=3,pady=3)
    def resetear_numeral():
        boton_1 =  tk.Button(numeros_frame,text=configuracion[4][0],
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero1())
        boton_1.grid(row=0,column=0,padx=3,pady=3)

        boton_2 =  tk.Button(numeros_frame,text=configuracion[4][1],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero2())
        boton_2.grid(row=0,column=1,padx=3,pady=3)

        boton_3 =  tk.Button(numeros_frame,text=configuracion[4][2],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero3())
        boton_3.grid(row=0,column=2,padx=3,pady=3)
        ###########################################
        boton_4 =  tk.Button(numeros_frame,text=configuracion[4][3],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero4())
        boton_4.grid(row=1,column=0,padx=3,pady=3)

        boton_5 =  tk.Button(numeros_frame,text=configuracion[4][4],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero5())
        boton_5.grid(row=1,column=1,padx=3,pady=3)

        boton_6 =  tk.Button(numeros_frame,text=configuracion[4][5],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero6())
        boton_6.grid(row=1,column=2,padx=3,pady=3)
        ###########################################
        boton_7 =  tk.Button(numeros_frame,text=configuracion[4][6],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero7())
        boton_7.grid(row=2,column=0,padx=3,pady=3)

        boton_8 =  tk.Button(numeros_frame,text=configuracion[4][7],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero8())
        boton_8.grid(row=2,column=1,padx=3,pady=3)

        boton_9 =  tk.Button(numeros_frame,text=configuracion[4][8],
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero9())
        boton_9.grid(row=2,column=2,padx=3,pady=3)
        


    #BOTONES DE JUEGO
    iniciar_boton= tk.Button(botones_frame,text=' Iniciar \n Juego ',
                              bg='#0b851b', activebackground = '#646e65',height=2,width=8,
                             font=("Arial Black",12), command=lambda:iniciar_partida() )
    iniciar_boton.grid(row=0,column=0,pady=5,padx=5)

    borrar_boton= tk.Button(botones_frame,text=' Borrar \n Juego ',
                              bg='#d40f26', activebackground = '#646e65',height=2,width=8,
                            command=lambda :boton_borrar(),font=("Arial Black",12))
    borrar_boton.grid(row=0,column=1,pady=5,padx=5)

    terminar_boton= tk.Button(botones_frame,text=' Terminar \n Juego ',
                              bg='#ba4e18', activebackground = '#646e65',height=2,width=8,
                              command=lambda: boton_terminar(),font=("Arial Black",12))
    terminar_boton.grid(row=0,column=3,pady=5,padx=5)

    deshacer_boton= tk.Button(botones_frame,text=' Deshacer \n Jugada ',
                              bg='#148bb3', activebackground = '#646e65',height=2,width=8,
                              command=lambda :boton_deshacer(),font=("Arial Black",12) )
    deshacer_boton.grid(row=1,column=0,pady=5,padx=5)

    rehacer_boton= tk.Button(botones_frame,text=' Rehacer \n Jugada  ',
                              bg='#148bb3', activebackground = '#646e65',height=2,width=8,
                             command=lambda :boton_rehacer(),font=("Arial Black",12) )
    rehacer_boton.grid(row=1,column=1,pady=5,padx=5)

    top_boton= tk.Button(botones_frame,text=' Top \n 10 ',
                              bg='#f5c507', activebackground = '#646e65',height=2,width=8,font=("Arial Black",12) )
    top_boton.grid(row=1,column=3,pady=5,padx=5)
    
    
    #CRONOMETRO Y TIMER

    if configuracion[0]==1:
        Cronometro_frame2 = tk.Frame(cronometro_frame,bg='#04b020',height=20,width=20)
        Cronometro_frame2.grid(row=0,column=0)
        cronol = tk.Label(Cronometro_frame2,text='Horas  ',bg="#04b020")    
        cronol.grid(row=0,column=0)
        cronol = tk.Label(Cronometro_frame2,text='Minutos ',bg="#04b020")    
        cronol.grid(row=0,column=1)
        cronol = tk.Label(Cronometro_frame2,text='Segundos',bg="#04b020")    
        cronol.grid(row=0,column=2)

        cronoh = tk.Label(Cronometro_frame2,text='00',bg="#04b020",font=("Arial Black",22) )    
        cronoh.grid(row=1,column=0)
        cronom = tk.Label(Cronometro_frame2,text='00',bg="#04b020",font=("Arial Black",22) )    
        cronom.grid(row=1,column=1)
        cronos = tk.Label(Cronometro_frame2,text='00',bg="#04b020",font=("Arial Black",22) )    
        cronos.grid(row=1,column=2)
    elif configuracion[0]==2:
        Cronometro_frame2 = tk.Frame(cronometro_frame,bg='#04b020',height=20,width=20)
        Cronometro_frame2.grid(row=0,column=0)
        cronol = tk.Label(Cronometro_frame2,text='Horas  ',bg="#04b020")    
        cronol.grid(row=0,column=0)
        cronol = tk.Label(Cronometro_frame2,text='Minutos ',bg="#04b020")    
        cronol.grid(row=0,column=1)
        cronol = tk.Label(Cronometro_frame2,text='Segundos',bg="#04b020")    
        cronol.grid(row=0,column=2)

        cronoh = tk.Label(Cronometro_frame2,text=str(configuracion[1][0]),bg="#04b020",font=("Arial Black",22) )    
        cronoh.grid(row=1,column=0)
        cronom = tk.Label(Cronometro_frame2,text=str(configuracion[1][1]),bg="#04b020",font=("Arial Black",22) )    
        cronom.grid(row=1,column=1)
        cronos = tk.Label(Cronometro_frame2,text=str(configuracion[1][2]),bg="#04b020",font=("Arial Black",22) )    
        cronos.grid(row=1,column=2)
    #dificultad label
    if configuracion[2] ==3:
        dificultad_label = tk.Label(cronometro_frame,text='Dificultad: Dificil ',font=("Arial Black",17),bg='#b2ff17')
        dificultad_label.grid(row=0,column=1,pady=3,padx=3)
    if configuracion[2] ==2:
        dificultad_label = tk.Label(cronometro_frame,text='Dificultad: Normal ',font=("Arial Black",17),bg='#b2ff17')
        dificultad_label.grid(row=0,column=1,pady=3,padx=3)
    if configuracion[2] ==1:
        dificultad_label = tk.Label(cronometro_frame,text='Dificultad: Fácil ',font=("Arial Black",17),bg='#b2ff17')
        dificultad_label.grid(row=0,column=1,pady=3,padx=3)
 
    #BOTONES DE GUARDAR Y CARGAR
    cargar_boton= tk.Button(botones2_frame,text=' Cargar \n Partida ',
                              bg='#148bb3', activebackground = '#646e65',height=2,width=8,font=("Arial Black",12) )
    cargar_boton.grid(row=0,column=0,pady=1,padx=5)

    guardar_boton= tk.Button(botones2_frame,text=' Guardar \n Partida  ',
                              bg='#148bb3', activebackground = '#646e65',height=2,width=8,font=("Arial Black",12) )
    guardar_boton.grid(row=0,column=1,pady=1,padx=5)
    #funcion para verificar victoria
    def verifica_victoria(lista):
        global time_out
        for x in lista:
            for y in x:
                for i in y:
                    for j in i:
                        if j==0:
                            return
        #despues de verificar que no hay espacios vacios procede a indicar la victoria
        time_out=1
        e=showmessage('Victoria!','Felicitaciones, gano el juego, ¿desea jugar otra partida?')
        if e==yes:
            terminar_partida()
        else:
            lista=deepcopy(lista_inicial)
            inicio_juego=0
            jugadas=[]
            jugadas_eliminadas=[]
            resetear_numeral()
            juego.destroy()
            jugar()
        
    #funcion para imprimir

    def imprimir(lista):

         for x in range (3):
            for y in range (3):
                partida2_frame = tk.Frame(partida_frame,bg="#b2ff17")
                partida2_frame.grid(row=x,column=y,padx=5,pady=5)
                for i in range(3):
                    for j in range(3):
                        if lista[x][y][i][j]==0:
                            cuadro =  tk.Button(partida2_frame,text='',
                                              bg='#e4e9f2', activebackground = '#a5a9b0',height=2,
                                                width=6, command=partial(marca_casilla_actual,x,y,i,j) )
                            cuadro.grid(row=i,column=j,padx=2,pady=2)
                        else:
                            signo=lista[x][y][i][j]
                            cuadro =  tk.Button(partida2_frame,text=configuracion[4][signo-1],
                                              bg='#d4a763', activebackground = '#a5a9b0',height=2,
                                                width=6,command=partial(marca_casilla_actual,x,y,i,j))
                            cuadro.grid(row=i,column=j,padx=2,pady=2)
         
         
    def sacar_fila(lista,x,y,i,j):
        respuesta=[]
        respuesta=respuesta+lista[x][0][i] 
        respuesta=respuesta+lista[x][1][i]  
        respuesta=respuesta+lista[x][2][i]  
        return respuesta
    def sacar_columna(lista,x,y,i,j):
        respuesta=[]
        respuesta.append(  lista[0][y][0][j]  )
        respuesta.append(  lista[0][y][1][j]  )
        respuesta.append(  lista[0][y][2][j]  )
        respuesta.append(  lista[1][y][0][j]  )
        respuesta.append(  lista[1][y][1][j]  )
        respuesta.append(  lista[1][y][2][j]  )
        respuesta.append(  lista[2][y][0][j]  )
        respuesta.append(  lista[2][y][1][j]  )
        respuesta.append(  lista[2][y][2][j]  )
        return respuesta
    def sacar_recuadro(lista,x,y):
        respuesta=[]
        respuesta=respuesta+lista[x][y][0]
        respuesta=respuesta+lista[x][y][1]
        respuesta=respuesta+lista[x][y][2]
        return respuesta
    def marca_casilla_actual (x,y,i,j):
        global lista, numero_actual , lista_inicial,time_out
        #sacamos las diferentes listas para hacer las validaciones
        fila=sacar_fila(lista,x,y,i,j)
        columna=sacar_columna(lista,x,y,i,j)
        recuadro=sacar_recuadro(lista,x,y)
        #valida que el numero no sea el mismo
        if lista[x][y][i][j]==numero_actual:
            return
        #validamos que el cuadro a editar no pertenezca a la disposicion inicial
        if lista_inicial[x][y][i][j]!=0:
            showmessage('Error!','No se puede sustituir este elemento por que Pertenece al cuadro inicial')
            #prueba
            '''
            lista=[ [ [[1,1,1],[1,1,1],[1,1,1]], [[1,1,1],[1,1,1],[1,1,1]], [[1,1,1],[1,1,1],[1,1,1]] ],
        [ [[1,1,1],[1,1,1],[1,1,1]], [[1,1,1],[1,1,1],[1,1,1]], [[1,1,1],[1,1,1],[1,1,1]] ],
        [ [[1,1,1],[1,1,1],[1,1,1]], [[1,1,1],[1,1,1],[1,1,1]], [[1,1,1],[1,1,1],[1,1,1]] ]  ]'''
            
        
            
        #validamos
        if numero_actual ==0:
            showmessage('Error!','Debe elegir algo para agregar de la barra lateral')
            return
        if numero_actual in fila:
            showmessage('Error!','No se puede agregrar este elemento por que ya esta en la fila')
            return
        elif numero_actual in columna:
            showmessage('Error!','No se puede agregrar este elemento por que ya esta en la columna')
            return
        elif numero_actual in recuadro:
            showmessage('Error!','No se puede agregrar este elemento por que ya esta en el recuadro')
            return
        
        #una vez que pasa las validaciones la jugada es posible por lo que se agrega
        
        lista[x][y][i][j]=numero_actual
        numero_actual=0
        imprimir(lista)
        resetear_numeral()

        #se verifica victoria y se agrega la jugada
        jugada_actual=deepcopy(lista)
        jugadas.append(jugada_actual)
        
        verifica_victoria(lista)
        
    def guardar_nombre():
        global nombre
        f=nombre_entry.get()
        if len(f)>30:
            showmessage('Error','El nombre no puede exeder los 30 caracteres')
            return
        nombre=f
        showmessage('Éxito',"El nombre se guardo correctamente")
    def boton_deshacer():
        global jugadas,jugadas_eliminadas,lista,inicio_juego
        if inicio_juego==0:
            showmessage('Error','Aun no se ha iniciado el juego')
        try:
            jugada_actual=jugadas.pop()
            jugadas_eliminadas.append(jugada_actual)
            lista=deepcopy(jugada_actual)
            imprimir(lista)
            resetear_numeral()
        except:
            showmessage('Error','No hay jugadas para deshacer')
    def boton_rehacer():
        global jugadas,jugadas_eliminadas,lista,inicio_juego
        if inicio_juego==0:
            showmessage('Error','Aun no se ha iniciado el juego')
        try:
            jugada_actual=jugadas_eliminadas.pop()
            lista=deepcopy(jugada_actual)
            imprimir(lista)
            resetear_numeral()
        except:
            showmessage('Error','No hay jugadas para rehacer')
    def boton_borrar():
        global lista,lista_inicial,jugadas,jugadas_eliminadas,inicio_juego
        if inicio_juego==0:
            showmessage('Error','Aun no se ha iniciado el juego')
            
        c=messagebox.askquestion('Borrar','Desea borrar el juego?',parent=juego)
        if c=='yes':
            lista=deepcopy(lista_inicial)
            jugadas=[]
            jugadas_eliminadas=[]
            imprimir (lista)
            resetear_numeral()
        else:
            return
    def boton_terminar():
        global lista,lista_inicial,jugadas,jugadas_eliminadas,inicio_juego,configuracion,h,m,s
        if inicio_juego==0:
            showmessage('Error','Aun no se ha iniciado el juego')

        c=messagebox.askquestion('Terminar','Desea Terminar el juego?',parent=juego)
        if c=='yes':
            lista=deepcopy(lista_inicial)
            jugadas=[]
            jugadas_eliminadas=[]
            resetear_numeral()
            inicio_juego=0
            #imprime el cuadro inicial
            f= open('sudoku2021partidas.dat','rb')
            info=pickle.load(f)
            f.close()
            h=configuracion[1][0]
            m=configuracion[1][1]
            s=configuracion[1][2]
            if configuracion[2]==3:
                num=random.randint(6,8)
                imprimir(info[num])
                lista=info[num]
                lista_inicial=deepcopy(info[num])
                jugadas.append(deepcopy(info[num]))
            elif configuracion[2]==1:
                num=random.randint(0,2)
                imprimir(info[num])
                lista=info[num]
                lista_inicial=deepcopy(info[num])
                jugadas.append(deepcopy(info[num]))
            elif configuracion[2]==2:
                num=random.randint(3,5)
                imprimir(info[num])
                lista=info[num]
                lista_inicial=deepcopy(info[num])
                jugadas.append(deepcopy(info[num]))
        else:
            return
    def iniciar_partida():
        #se arreglan aspectos respecto al nombre y se valida
        global nombre,lista,lista_inicial,h,m,s,inicio_juego,jugadas
        inicio_juego=1
        if nombre=='':
            showmessage('Error','Debe ingresar su nombre antes de empezar a jugar')
            
            return
            
        nombre_entry=tk.Label(nombre_frame,bg='#b2ff17',
                              width=30,text=nombre,font=("Arial Black",12) ) 
        nombre_entry.grid(row=1,column=0)

        nombre_boton= tk.Button(nombre_frame,text='',
                              bg='#b2ff17', activebackground = '#3091db',
                                height=2,width=10,state='disabled' ,relief='flat')
        nombre_boton.grid(row=2,column=0)
        
        #####################################################        
        #se deshabilita el boton de jugar

        iniciar_boton= tk.Button(botones_frame,text=' Iniciar \n Juego ',
                              bg='#0b851b', activebackground = '#c9c9c9',height=2,width=8,
                             font=("Arial Black",12), state='disabled')
        iniciar_boton.grid(row=0,column=0,pady=5,padx=5)

        ####################################################
        #se habilita el numeral
        resetear_numeral()
        #imprime el cuadro inicial
        f= open('sudoku2021partidas.dat','rb')
        info=pickle.load(f)
        f.close()

        if configuracion[2]==3:
            num=random.randint(6,8)
            imprimir(info[num])
            lista=info[num]
            lista_inicial=deepcopy(info[num])
            jugadas.append(deepcopy(info[num]))
        elif configuracion[2]==1:
            num=random.randint(0,2)
            imprimir(info[num])
            lista=info[num]
            lista_inicial=deepcopy(info[num])
            jugadas.append(deepcopy(info[num]))
        elif configuracion[2]==2:
            num=random.randint(3,5)
            imprimir(info[num])
            lista=info[num]
            lista_inicial=deepcopy(info[num])
            jugadas.append(deepcopy(info[num]))
        #inicia el cronometro o temporizar
        #cronometro y temporizador:

        def tiempo_agotado():
            global h,m,s,lista,lista_inicial,jugadas,jugadas_eliminadas,inicio_juego
            f=messagebox.askquestion('Tiempo Agotado!','¿Desea seguir jugando?',parent=juego)
        
            if f== 'yes' :
                h=configuracion[1][0]
                m=configuracion[1][1]
                s=configuracion[1][2]
                cronometro()
            if f=='no':
                lista=deepcopy(lista_inicial)
                inicio_juego=0
                jugadas=[]
                jugadas_eliminadas=[]
                resetear_numeral()
                juego.destroy()
                jugar()
                

            
            
        def cronometro():
            global m,h,s, time_out
            if time_out==1:
                cronoh = tk.Label(Cronometro_frame2,bg="#04b020" ,height=1,width=6)    
                cronoh.grid(row=1,column=0)
                cronom = tk.Label(Cronometro_frame2,bg="#04b020",height=1,width=6)    
                cronom.grid(row=1,column=1)
                cronos = tk.Label(Cronometro_frame2,bg="#04b020",height=1,width=6)    
                cronos.grid(row=1,column=2)
                cronoh = tk.Label(Cronometro_frame2,text=str(h),bg="#04b020",font=("Arial Black",22) )    
                cronoh.grid(row=1,column=0)
                cronom = tk.Label(Cronometro_frame2,text=str(m),bg="#04b020",font=("Arial Black",22) )    
                cronom.grid(row=1,column=1)
                cronos = tk.Label(Cronometro_frame2,text=str(s),bg="#04b020",font=("Arial Black",22) )
                cronos.grid(row=1,column=2)
                cronos.after(1000,cronometro)
               
            else:
                
                if h == 99:
                    return
                if m== 59:
                    m=0
                    h=h+1
                if s == 59:
                    s=0
                    m=m+1
                cronoh = tk.Label(Cronometro_frame2,bg="#04b020" ,height=1,width=6)    
                cronoh.grid(row=1,column=0)
                cronom = tk.Label(Cronometro_frame2,bg="#04b020",height=1,width=6)    
                cronom.grid(row=1,column=1)
                cronos = tk.Label(Cronometro_frame2,bg="#04b020",height=1,width=6)    
                cronos.grid(row=1,column=2)
                cronoh = tk.Label(Cronometro_frame2,text=str(h),bg="#04b020",font=("Arial Black",22) )    
                cronoh.grid(row=1,column=0)
                cronom = tk.Label(Cronometro_frame2,text=str(m),bg="#04b020",font=("Arial Black",22) )    
                cronom.grid(row=1,column=1)
                cronos = tk.Label(Cronometro_frame2,text=str(s),bg="#04b020",font=("Arial Black",22) )
                s=s+1
                cronos.grid(row=1,column=2)
                cronos.after(1000,cronometro)
            
        def timer():
            
            global h,m,s,time_out
            
            if time_out==1:
                cronoh = tk.Label(Cronometro_frame2,bg="#04b020" ,height=1,width=6)    
                cronoh.grid(row=1,column=0)
                cronom = tk.Label(Cronometro_frame2,bg="#04b020",height=1,width=6)    
                cronom.grid(row=1,column=1)
                cronos = tk.Label(Cronometro_frame2,bg="#04b020",height=1,width=6)    
                cronos.grid(row=1,column=2)
                cronoh = tk.Label(Cronometro_frame2,text=str(h),bg="#04b020",font=("Arial Black",22) )    
                cronoh.grid(row=1,column=0)
                cronom = tk.Label(Cronometro_frame2,text=str(m),bg="#04b020",font=("Arial Black",22) )    
                cronom.grid(row=1,column=1)
                cronos = tk.Label(Cronometro_frame2,text=str(s),bg="#04b020",font=("Arial Black",22) )    
                cronos.grid(row=1,column=2)
                cronos.after(1000,timer)
                
            else:
                
                if m==0:
                    if h>=1:
                        h=h-1
                        m=59
                if s==0:
                    if m==0:
                        if h==0:
                            tiempo_agotado()
                            return
                    else:
                        if m==0:
                            h=h-1
                            m=59
                            s=59
                        else:   
                            s=59
                            m=m-1
                            
                cronoh = tk.Label(Cronometro_frame2,bg="#04b020" ,height=1,width=6)    
                cronoh.grid(row=1,column=0)
                cronom = tk.Label(Cronometro_frame2,bg="#04b020",height=1,width=6)    
                cronom.grid(row=1,column=1)
                cronos = tk.Label(Cronometro_frame2,bg="#04b020",height=1,width=6)    
                cronos.grid(row=1,column=2)
                cronoh = tk.Label(Cronometro_frame2,text=str(h),bg="#04b020",font=("Arial Black",22) )    
                cronoh.grid(row=1,column=0)
                cronom = tk.Label(Cronometro_frame2,text=str(m),bg="#04b020",font=("Arial Black",22) )    
                cronom.grid(row=1,column=1)
                cronos = tk.Label(Cronometro_frame2,text=str(s),bg="#04b020",font=("Arial Black",22) )    
                cronos.grid(row=1,column=2)
                s=s-1
                cronos.after(1000,timer)
            
        if configuracion[0]==1:
            h=0
            m=0
            s=0
            
            cronometro()
            
        elif configuracion[0]==2:
            h=configuracion[1][0]
            m=configuracion[1][1]
            s=configuracion[1][2]
            timer()
        
######################################################################################################################################
######################################################################################################################################        
######################################################################################################################################
#funcion configuracion

def configuracion_sudoku():

    configuracionv=tk.Toplevel(ventana)
    configuracionv.title('Configuracion Sudoku')
    configuracionv.geometry('630x350')
    configuracionv.config(bg='#096eba')
    configuracionv.resizable(False,False)

    def set_timer(dificultad):
        
        if dificultad==1:
            
            h = tk.Entry(conframe,bg="#defdff",width=2)
            h.insert(0,'0')
            h.grid(row=2,column=1,pady=1)
            m= tk.Entry(conframe,bg="#defdff",width=2)
            m.insert(0,'30')
            m.grid(row=2,column=2,pady=1)
            s= tk.Entry(conframe,bg="#defdff",width=2)
            s.insert(0,'0')
            s.grid(row=2,column=3,pady=1)
            set_time=tk.Button(conframe,text='Aceptar', bg='#3091db', activebackground = '#00d9fa',height=1,
                               width=6,command=lambda :fijar_timer(h,m,s))
            set_time.grid(row=3,column=3,padx=10,pady=20)
        if dificultad==2:
            h = tk.Entry(conframe,bg="#defdff",width=2)
            h.insert(0,'1')
            h.grid(row=2,column=1,pady=1)
            m= tk.Entry(conframe,bg="#defdff",width=2)
            m.insert(0,'0')
            m.grid(row=2,column=2,pady=1)
            s= tk.Entry(conframe,bg="#defdff",width=2)
            s.insert(0,'0')
            s.grid(row=2,column=3,pady=1)
            set_time=tk.Button(conframe,text='Aceptar', bg='#3091db', activebackground = '#00d9fa',height=1,
                               width=6,command=lambda :fijar_timer(h,m,s))
            set_time.grid(row=3,column=3,padx=10,pady=20)
        if dificultad==3:
            h = tk.Entry(conframe,bg="#defdff",width=2)
            h.insert(0,'2')
            h.grid(row=2,column=1,pady=1)
            m= tk.Entry(conframe,bg="#defdff",width=2)
            m.insert(0,'0')
            m.grid(row=2,column=2,pady=1)
            s= tk.Entry(conframe,bg="#defdff",width=2)
            s.insert(0,'0')
            s.grid(row=2,column=3,pady=1)
            set_time=tk.Button(conframe,text='Aceptar', bg='#3091db', activebackground = '#00d9fa',height=1,
                               width=6,command=lambda :fijar_timer(h,m,s))
            set_time.grid(row=3,column=3,padx=10,pady=20)
    def no_timer():
        h = tk.Entry(conframe,bg="#defdff",width=2,state='disabled')
        h.grid(row=2,column=1)
        m= tk.Entry(conframe,bg="#defdff",width=2,state='disabled')
        m.grid(row=2,column=2)
        s= tk.Entry(conframe,bg="#defdff",width=2,state='disabled')
        s.grid(row=2,column=3)
        
        #boton fijar timer
        set_time=tk.Button(conframe,text='Aceptar', bg='#3091db', activebackground = '#00d9fa',height=1,width=6,
                           state='disabled',command=lambda :fijar_timer(h,m,s)) 
        set_time.grid(row=3,column=3,padx=10,pady=20)



        
    def fijar_timer(h,m,s):
        global datos_timer
        horas=h.get()
        minutos=m.get()
        segundos=s.get()
        if horas=='':
            horas=0
        if minutos=='':
            minutos=0
        if segundos=='':
            segundos=0
        
        try:
            horas=int (horas)
            minutos=int (minutos)
            segundos=int (segundos)
            #confirma que los valores de cada dato sean los correctos
            if  horas==0 and minutos==0 and segundos==0:
                messagebox.showinfo('Error!','Timer vacio',parent=configuracionv)
                return
            elif horas>4 or horas<0:
                messagebox.showinfo('Error!','El formato ingresado es incorrecto',parent=configuracionv)
                h = tk.Entry(conframe,bg="#defdff",width=2)
                h.grid(row=2,column=1,pady=1)
                m= tk.Entry(conframe,bg="#defdff",width=2)
                m.grid(row=2,column=2,pady=1)
                s= tk.Entry(conframe,bg="#defdff",width=2)
                s.grid(row=2,column=3,pady=1)
                set_time=tk.Button(conframe,text='Aceptar', bg='#3091db', activebackground = '#00d9fa',
                                   height=1,width=6,command=lambda :fijar_timer(h,m,s))
                set_time.grid(row=3,column=3,padx=10,pady=20)
                return
            elif minutos>59 or minutos<0:
                messagebox.showinfo('Error!','El formato ingresado es incorrecto',parent=configuracionv)
                h = tk.Entry(conframe,bg="#defdff",width=2)
                h.grid(row=2,column=1,pady=1)
                m= tk.Entry(conframe,bg="#defdff",width=2)
                m.grid(row=2,column=2,pady=1)
                s= tk.Entry(conframe,bg="#defdff",width=2)
                s.grid(row=2,column=3,pady=1)
                set_time=tk.Button(conframe,text='Aceptar', bg='#3091db', activebackground = '#00d9fa',height=1,
                                   width=6,command=lambda :fijar_timer(h,m,s))
                set_time.grid(row=3,column=3,padx=10,pady=20)
                return
            elif segundos>59 or segundos<0:
                messagebox.showinfo('Error!','El formato ingresado es incorrecto',parent=configuracionv)
                h = tk.Entry(conframe,bg="#defdff",width=2)
                h.grid(row=2,column=1,pady=1)
                m= tk.Entry(conframe,bg="#defdff",width=2)
                m.grid(row=2,column=2,pady=1)
                s= tk.Entry(conframe,bg="#defdff",width=2)
                s.grid(row=2,column=3,pady=1)
                set_time=tk.Button(conframe,text='Aceptar', bg='#3091db', activebackground = '#00d9fa',height=1,
                                   width=6,command=lambda :fijar_timer(h,m,s))
                set_time.grid(row=3,column=3,padx=10,pady=20)
                return
            
            datos_timer=(horas,minutos,segundos)
            messagebox.showinfo('Timer agregado','Pulse fijar configuración para guardar los datos de configuración',parent=configuracionv)
            return
        except:
            messagebox.showinfo('Error!','El formato ingresado es incorrecto',parent=configuracionv)
            h = tk.Entry(conframe,bg="#defdff",width=2)
            h.grid(row=2,column=1,pady=1)
            m= tk.Entry(conframe,bg="#defdff",width=2)
            m.grid(row=2,column=2,pady=1)
            s= tk.Entry(conframe,bg="#defdff",width=2)
            s.grid(row=2,column=3,pady=1)
            set_time=tk.Button(conframe,text='Aceptar', bg='#3091db', activebackground = '#00d9fa',height=1,
                               width=6,command=lambda :fijar_timer(h,m,s))
            set_time.grid(row=3,column=3,padx=10,pady=20)
            return
        
                
                
            
            
        
    def fijar_config(reloj,dificultad,numeral):

        global configuracion,datos_timer,tipo_numeral,topx
        if numeral==1:
            tipo_numeral=['1','2','3','4','5','6','7','8','9']
        if numeral==2:
            tipo_numeral=['A','B','C','D','E','F','G','H','I']
        
        if numeral==3 and tipo_numeral==['1','2','3','4','5','6','7','8','9']:
            messagebox.showinfo('Error!','Si desea usar la opcion Personalizar debe configurar '
                       'los caracteres deseados y guardarlos, antes de guardar los datos.',parent=configuracionv)
            return
            
        if datos_timer == (0,0,0) and reloj ==2:
           messagebox.showinfo('Error!','Si desea usar la opcion Timer debe configurar '
                       'el tiempo deseado, antes de guardar los datos.',parent=configuracionv)
           return
        if reloj==1 or reloj==3:
            datos_timer=(0,0,0)
            configuracion=(reloj,(0,0,0),dificultad,topx,tipo_numeral)
            messagebox.showinfo('Lo tenemos!','Informacion Guardada Correctamente!',parent=configuracionv)
            configuracionv.destroy()
            
        else:
            configuracion=(reloj,datos_timer,dificultad,topx,tipo_numeral)
            messagebox.showinfo('Lo tenemos!','Informacion Guardada Correctamente!',parent=configuracionv)
            configuracionv.destroy()
        
    #frame1
    conframe=tk.Frame(configuracionv,bg="#29d1ff",height=130,width=150)
    conframe.grid(row=0,column=0,padx=10,pady=10)
    #frame2
    conframe2=tk.Frame(configuracionv,bg="#29d1ff",height=130,width=150)
    conframe2.grid(row=1,column=0,padx=1,pady=1)
    
    #opcion tiempo
    
    opcion=tk.IntVar()
    reloj=Radiobutton(conframe, text = "Cronómetro", value = 1,variable=opcion,width=12,
                      bg="#29d1ff",command=lambda:no_timer())
    reloj.select()
    reloj.grid(row=1,column=0)
    timer=Radiobutton(conframe, text = "Timer            ", value = 2,variable=opcion,width=12,
                      bg='#29d1ff',command=lambda:set_timer(opcion2.get() ))
    timer.deselect()
    timer.grid(row=2,column=0)
    no=Radiobutton(conframe, text =    "Sin tiempo   ", value = 3,variable=opcion,width=12,
                   bg="#29d1ff",command=lambda:no_timer())
    no.grid(row=3,column=0)

    #reloj configurable
    
    cuadro = tk.Label(conframe,bg="#2494b3",height=1,width=10,text='Tiempo',font=("Arial Black",13))
    cuadro.grid(row=0,column=0,padx=1,pady=1)
    
    cuadro = tk.Label(conframe,bg="#2494b3",height=1,width=6,text='Horas')
    cuadro.grid(row=1,column=1,padx=1,pady=2)
    cuadro = tk.Label(conframe,bg="#2494b3",height=1,width=6,text='Minutos')
    cuadro.grid(row=1,column=2,padx=1,pady=2)
    cuadro = tk.Label(conframe,bg="#2494b3",height=1,width=9,text='Segundos')
    cuadro.grid(row=1,column=3,padx=1,pady=2)
           
    h = tk.Entry(conframe,bg="#defdff",width=2,state='disabled')
    h.grid(row=2,column=1)
    m= tk.Entry(conframe,bg="#defdff",width=2,state='disabled')
    m.grid(row=2,column=2)
    s= tk.Entry(conframe,bg="#defdff",width=2,state='disabled')
    s.grid(row=2,column=3)
    
    #boton fijar timer
    set_time=tk.Button(conframe,text='Aceptar', bg='#3091db', activebackground = '#00d9fa',height=1,width=6,
                       state='disabled',command=lambda :fijar_timer(h,m,s)) 
    set_time.grid(row=3,column=3,padx=10,pady=20)
    #boton fijar conf
    set_time=tk.Button(conframe2,text='Fijar Configuracion', bg='#1ee373', activebackground = '#00d9fa',
                       height=1,width=15,command=lambda :fijar_config(opcion.get(),opcion2.get(),opcion3.get())) 
    set_time.grid(row=4,column=0,padx=10,pady=10)
    
    
    cuadro = tk.Label(conframe2,bg="#2494b3",height=1,width=24,text='Dificultad',font=("Arial Black",13))
    cuadro.grid(row=0,column=0,padx=1,pady=1)
    opcion2=tk.IntVar()
    dificultad_facil=Radiobutton(conframe2, text = "Fácil", value = 1,variable=opcion2,width=5,bg="#2494b3")
    dificultad_facil.select()
    dificultad_facil.grid(row=1,column=0)
    
    dificultad_normal=Radiobutton(conframe2, text = "Medio", value = 2,variable=opcion2,width=5,bg="#2494b3")
    dificultad_normal.grid(row=2,column=0)
    
    dificultad_dificil=Radiobutton(conframe2, text = "Díficil", value = 3,variable=opcion2,width=5,bg="#2494b3")
    dificultad_dificil.grid(row=3,column=0)

    #Cantidad de jugadas topx
    #frame3
    conframe3=tk.Frame(configuracionv,bg="#29d1ff",height=130,width=250)
    conframe3.grid(row=0,column=1,padx=1,pady=1)
    cuadro = tk.Label(conframe3,bg="#2494b3",height=1,width=24,text=' Cantidad de jugadas top ',font=("Arial Black",13))
    cuadro.grid(row=0,column=0,padx=1,pady=1)
    h = tk.Entry(conframe3,bg="#defdff",width=3)
    h.grid(row=1,column=0,pady=20)
    set_topx=tk.Button(conframe3,text='Aceptar', bg='#3091db', activebackground = '#00d9fa',
                                   height=1,width=6,command=lambda :guardar_topx(h.get() ))
    set_topx.grid(row=2,column=0,padx=1,pady=13)
    def guardar_topx(valor):
        global topx
        try:
            valor=int(valor)
            if valor>100:
                messagebox.showinfo('Error!',' Dato ingresado incorrecto ',parent=configuracionv)
                return
            if valor<0:
                messagbox.showinfo('Error!',' Dato ingresado incorrecto ',parent=configuracionv)
                return
            
            topx=valor
            messagebox.showinfo('Valor Agregado!',' Pulse en Guardar Configuracion para registrar todos los datos'
                                ,parent=configuracionv)


        except:
            messagebox.showinfo('Error!',' Dato ingresado incorrecto ',parent=configuracionv)
    #frame4
    conframe4=tk.Frame(configuracionv,bg="#29d1ff",height=151,width=250)
    conframe4.grid(row=1,column=1,padx=1,pady=1)

    cuadro = tk.Label(conframe4,bg="#2494b3",height=1,width=24,text='Elementos del juego',font=("Arial Black",13))
    cuadro.grid(row=0,column=0,padx=1,pady=1)
    opcion3=tk.IntVar()
    numeros=Radiobutton(conframe4, text = "1 2 3 4 5 6 7 8 9  ", value = 1,variable=opcion3,
                        width=15,bg="#29d1ff",command=lambda:personalizar_no())
    numeros.select()
    numeros.grid(row=1,column=0)
    
    letras=Radiobutton(conframe4, text = "A B C D E F G H I", value = 2,variable=opcion3,
                       width=15,bg="#29d1ff",command=lambda:personalizar_no())
    letras.grid(row=2,column=0)
    
    personalizado=Radiobutton(conframe4, text = "Personalizar        ", value = 3,variable=opcion3,
                              width=15,bg="#29d1ff",command=lambda:personalizar_si())
    personalizado.grid(row=3,column=0)
    #frame 5 para los entrys
    conframe5=tk.Frame(conframe4,bg="#29d1ff",height=4,width=250)
    conframe5.grid(row=4,column=0,padx=1,pady=1)
    def guardar_valores(lista):
        global tipo_numeral

        for a in lista:
            if a =='' or len(a)!= 1:
                messagebox.showinfo('Error','Los datos ingresados no son validos, exeden un caracter o estan incompletos',parent=configuracionv)
                personalizar_si()
                return
        tipo_numeral=lista
        messagebox.showinfo('Valores Agregados!',' Pulse en Guardar Configuracion para registrar todos los datos de configuracion'
                                ,parent=configuracionv)
        
                
    def personalizar_no():
        primer_valor = tk.Entry(conframe5,bg="#defdff",width=1,state='disabled')
        primer_valor.grid(row=0,column=0,padx=3)
        
        segundo_valor = tk.Entry(conframe5,bg="#defdff",width=1,state='disabled')
        segundo_valor.grid(row=0,column=1,padx=3)
        
        tercer_valor = tk.Entry(conframe5,bg="#defdff",width=1,state='disabled')
        tercer_valor.grid(row=0,column=2,padx=3)
        
        cuarto_valor = tk.Entry(conframe5,bg="#defdff",width=1,state='disabled')
        cuarto_valor.grid(row=0,column=3,padx=3)
        
        quinto_valor = tk.Entry(conframe5,bg="#defdff",width=1,state='disabled')
        quinto_valor.grid(row=0,column=4,padx=3)
        
        sexto_valor = tk.Entry(conframe5,bg="#defdff",width=1,state='disabled')
        sexto_valor.grid(row=0,column=5,padx=3)
        
        septimo_valor = tk.Entry(conframe5,bg="#defdff",width=1,state='disabled')
        septimo_valor.grid(row=0,column=6,padx=3)
        
        octavo_valor = tk.Entry(conframe5,bg="#defdff",width=1,state='disabled')
        octavo_valor.grid(row=0,column=7,padx=3)
        
        noveno_valor = tk.Entry(conframe5,bg="#defdff",width=1,state='disabled')
        noveno_valor.grid(row=0,column=8,padx=3)
        
        set_valor=tk.Button(conframe4,text='Aceptar', bg='#3091db', activebackground = '#00d9fa',
                                       height=1,width=6 ,state='disabled')
        set_valor.grid(row=5,column=0,padx=1,pady=1)
    personalizar_no()

    def personalizar_si():
        primer_valor = tk.Entry(conframe5,bg="#defdff",width=1)
        primer_valor.grid(row=0,column=0,padx=3)
        
        segundo_valor = tk.Entry(conframe5,bg="#defdff",width=1)
        segundo_valor.grid(row=0,column=1,padx=3)
        
        tercer_valor = tk.Entry(conframe5,bg="#defdff",width=1)
        tercer_valor.grid(row=0,column=2,padx=3)
        
        cuarto_valor = tk.Entry(conframe5,bg="#defdff",width=1)
        cuarto_valor.grid(row=0,column=3,padx=3)
        
        quinto_valor = tk.Entry(conframe5,bg="#defdff",width=1)
        quinto_valor.grid(row=0,column=4,padx=3)
        
        sexto_valor = tk.Entry(conframe5,bg="#defdff",width=1)
        sexto_valor.grid(row=0,column=5,padx=3)
        
        septimo_valor = tk.Entry(conframe5,bg="#defdff",width=1)
        septimo_valor.grid(row=0,column=6,padx=3)
        
        octavo_valor = tk.Entry(conframe5,bg="#defdff",width=1)
        octavo_valor.grid(row=0,column=7,padx=3)
        
        noveno_valor = tk.Entry(conframe5,bg="#defdff",width=1)
        noveno_valor.grid(row=0,column=8,padx=3)
        
        set_valor=tk.Button(conframe4,text='Aceptar', bg='#3091db', activebackground = '#00d9fa',
                                       height=1,width=6,
                            command=lambda :guardar_valores( [ primer_valor.get(),segundo_valor.get(),tercer_valor.get(),
                                                               cuarto_valor.get(),quinto_valor.get(),sexto_valor.get(),
                                                               septimo_valor.get(),octavo_valor.get(),noveno_valor.get()]     ) )
        set_valor.grid(row=5,column=0,padx=1,pady=1)
            
    
   
#funcion ayuda
'''
Entradas: un click en la interfaz
Salidas: un pdf
Funcion: abre un pdf con el manual de usuario
'''
def ayuda():

    os.startfile('manual_de_usuario_sudoku.pdf')




#funcion salir
'''
Entradas: un click en la interfaz
Salidas: nada 
Funcion: cierra el programa cuando se activa
'''

def salir():

    ventana.destroy()

















ventana.mainloop()
