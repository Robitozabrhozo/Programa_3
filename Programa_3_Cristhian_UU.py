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
#config
#              reloj   tiempo en timer  dificutad  topx   tipo_numeral
configuracion=[1,       (0,0,0),        1,         0,     ['1','2','3','4','5','6','7','8','9'] ]
datos_timer=(0,0,0)
tipo_numeral=['1','2','3','4','5','6','7','8','9']
topx=0
#nombre
nombre=''
#tiempo
tiempo=(0,0,0)
h=0
m=0
s=0
#lista actual de numeros
lista=[ [ [[0,1,0],[0,0,0],[0,1,0]], [[0,1,0],[0,0,0],[0,1,0]], [[0,0,0],[0,0,0],[0,0,0]] ],
        [ [[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]] ],
        [ [[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,1]] ]  ]
#Numeral
numero_actual=0
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

    titulo_frame = tk.Frame(juego,height=128,width=540,bg='#5f6160')
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
    cronometro_frame = tk.Frame(juego,bg="#c105ff",height=115,width=540)
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
    

    boton_1 =  tk.Button(numeros_frame,text='1',
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero1(),state='disabled')
    boton_1.grid(row=0,column=0,padx=3,pady=3)

    boton_2 =  tk.Button(numeros_frame,text='2',
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero2(),state='disabled')
    boton_2.grid(row=0,column=1,padx=3,pady=3)

    boton_3 =  tk.Button(numeros_frame,text='3',
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero3(),state='disabled')
    boton_3.grid(row=0,column=2,padx=3,pady=3)
    ###########################################
    boton_4 =  tk.Button(numeros_frame,text='4',
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero4(),state='disabled')
    boton_4.grid(row=1,column=0,padx=3,pady=3)

    boton_5 =  tk.Button(numeros_frame,text='5',
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero5(),state='disabled')
    boton_5.grid(row=1,column=1,padx=3,pady=3)

    boton_6 =  tk.Button(numeros_frame,text='6',
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero6(),state='disabled')
    boton_6.grid(row=1,column=2,padx=3,pady=3)
    ###########################################
    boton_7 =  tk.Button(numeros_frame,text='7',
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero7(),state='disabled')
    boton_7.grid(row=2,column=0,padx=3,pady=3)

    boton_8 =  tk.Button(numeros_frame,text='8',
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero8(),state='disabled')
    boton_8.grid(row=2,column=1,padx=3,pady=3)

    boton_9 =  tk.Button(numeros_frame,text='9',
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero9(),state='disabled')
    boton_9.grid(row=2,column=2,padx=3,pady=3)

    def numero1():
        global numero_actual
        numero_actual==1
        boton_1 =  tk.Button(numeros_frame,text='1',
                              bg='#51db7b', activebackground = '#bac2bd',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero1(),state='disabled')
        boton_1.grid(row=0,column=0,padx=3,pady=3)

        boton_2 =  tk.Button(numeros_frame,text='2',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero2())
        boton_2.grid(row=0,column=1,padx=3,pady=3)

        boton_3 =  tk.Button(numeros_frame,text='3',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero3())
        boton_3.grid(row=0,column=2,padx=3,pady=3)
        ###########################################
        boton_4 =  tk.Button(numeros_frame,text='4',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero4())
        boton_4.grid(row=1,column=0,padx=3,pady=3)

        boton_5 =  tk.Button(numeros_frame,text='5',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero5())
        boton_5.grid(row=1,column=1,padx=3,pady=3)

        boton_6 =  tk.Button(numeros_frame,text='6',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero6())
        boton_6.grid(row=1,column=2,padx=3,pady=3)
        ###########################################
        boton_7 =  tk.Button(numeros_frame,text='7',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero7())
        boton_7.grid(row=2,column=0,padx=3,pady=3)

        boton_8 =  tk.Button(numeros_frame,text='8',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero8())
        boton_8.grid(row=2,column=1,padx=3,pady=3)

        boton_9 =  tk.Button(numeros_frame,text='9',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero9())
        boton_9.grid(row=2,column=2,padx=3,pady=3)
        
        
    ###########################################
    def numero2():
        global numero_actual
        numero_actual==2
        boton_1 =  tk.Button(numeros_frame,text='1',
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero1())
        boton_1.grid(row=0,column=0,padx=3,pady=3)

        boton_2 =  tk.Button(numeros_frame,text='2',
                                  bg='#51db7b', activebackground = '#bac2bd',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero2(),state='disabled')
        boton_2.grid(row=0,column=1,padx=3,pady=3)

        boton_3 =  tk.Button(numeros_frame,text='3',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero3())
        boton_3.grid(row=0,column=2,padx=3,pady=3)
        ###########################################
        boton_4 =  tk.Button(numeros_frame,text='4',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero4())
        boton_4.grid(row=1,column=0,padx=3,pady=3)

        boton_5 =  tk.Button(numeros_frame,text='5',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero5())
        boton_5.grid(row=1,column=1,padx=3,pady=3)

        boton_6 =  tk.Button(numeros_frame,text='6',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero6())
        boton_6.grid(row=1,column=2,padx=3,pady=3)
        ###########################################
        boton_7 =  tk.Button(numeros_frame,text='7',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero7())
        boton_7.grid(row=2,column=0,padx=3,pady=3)

        boton_8 =  tk.Button(numeros_frame,text='8',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero8())
        boton_8.grid(row=2,column=1,padx=3,pady=3)

        boton_9 =  tk.Button(numeros_frame,text='9',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero9())
        boton_9.grid(row=2,column=2,padx=3,pady=3)

    def numero3():
        global numero_actual
        numero_actual==3
        boton_1 =  tk.Button(numeros_frame,text='1',
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero1())
        boton_1.grid(row=0,column=0,padx=3,pady=3)

        boton_2 =  tk.Button(numeros_frame,text='2',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero2())
        boton_2.grid(row=0,column=1,padx=3,pady=3)

        boton_3 =  tk.Button(numeros_frame,text='3',
                                  bg='#51db7b', activebackground = '#bac2bd',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero3(),state='disabled')
        boton_3.grid(row=0,column=2,padx=3,pady=3)
        ###########################################
        boton_4 =  tk.Button(numeros_frame,text='4',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero4())
        boton_4.grid(row=1,column=0,padx=3,pady=3)

        boton_5 =  tk.Button(numeros_frame,text='5',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero5())
        boton_5.grid(row=1,column=1,padx=3,pady=3)

        boton_6 =  tk.Button(numeros_frame,text='6',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero6())
        boton_6.grid(row=1,column=2,padx=3,pady=3)
        ###########################################
        boton_7 =  tk.Button(numeros_frame,text='7',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero7())
        boton_7.grid(row=2,column=0,padx=3,pady=3)

        boton_8 =  tk.Button(numeros_frame,text='8',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero8())
        boton_8.grid(row=2,column=1,padx=3,pady=3)

        boton_9 =  tk.Button(numeros_frame,text='9',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero9())
        boton_9.grid(row=2,column=2,padx=3,pady=3)

    def numero4():
        global numero_actual
        numero_actual==4
        boton_1 =  tk.Button(numeros_frame,text='1',
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero1())
        boton_1.grid(row=0,column=0,padx=3,pady=3)

        boton_2 =  tk.Button(numeros_frame,text='2',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero2())
        boton_2.grid(row=0,column=1,padx=3,pady=3)

        boton_3 =  tk.Button(numeros_frame,text='3',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero3())
        boton_3.grid(row=0,column=2,padx=3,pady=3)
        ###########################################
        boton_4 =  tk.Button(numeros_frame,text='4',
                                  bg='#51db7b', activebackground = '#bac2bd',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero4(),state='disabled')
        boton_4.grid(row=1,column=0,padx=3,pady=3)

        boton_5 =  tk.Button(numeros_frame,text='5',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero5())
        boton_5.grid(row=1,column=1,padx=3,pady=3)

        boton_6 =  tk.Button(numeros_frame,text='6',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero6())
        boton_6.grid(row=1,column=2,padx=3,pady=3)
        ###########################################
        boton_7 =  tk.Button(numeros_frame,text='7',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero7())
        boton_7.grid(row=2,column=0,padx=3,pady=3)

        boton_8 =  tk.Button(numeros_frame,text='8',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero8())
        boton_8.grid(row=2,column=1,padx=3,pady=3)

        boton_9 =  tk.Button(numeros_frame,text='9',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero9())
        boton_9.grid(row=2,column=2,padx=3,pady=3)
    def numero5():
        global numero_actual
        numero_actual==5
        boton_1 =  tk.Button(numeros_frame,text='1',
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero1())
        boton_1.grid(row=0,column=0,padx=3,pady=3)

        boton_2 =  tk.Button(numeros_frame,text='2',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero2())
        boton_2.grid(row=0,column=1,padx=3,pady=3)

        boton_3 =  tk.Button(numeros_frame,text='3',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero3())
        boton_3.grid(row=0,column=2,padx=3,pady=3)
        ###########################################
        boton_4 =  tk.Button(numeros_frame,text='4',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero4())
        boton_4.grid(row=1,column=0,padx=3,pady=3)

        boton_5 =  tk.Button(numeros_frame,text='5',
                                  bg='#51db7b', activebackground = '#bac2bd',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero5(),state='disabled')
        boton_5.grid(row=1,column=1,padx=3,pady=3)

        boton_6 =  tk.Button(numeros_frame,text='6',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero6())
        boton_6.grid(row=1,column=2,padx=3,pady=3)
        ###########################################
        boton_7 =  tk.Button(numeros_frame,text='7',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero7())
        boton_7.grid(row=2,column=0,padx=3,pady=3)

        boton_8 =  tk.Button(numeros_frame,text='8',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero8())
        boton_8.grid(row=2,column=1,padx=3,pady=3)

        boton_9 =  tk.Button(numeros_frame,text='9',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero9())
        boton_9.grid(row=2,column=2,padx=3,pady=3)
    def numero6():
        global numero_actual
        numero_actual==6
        boton_1 =  tk.Button(numeros_frame,text='1',
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero1())
        boton_1.grid(row=0,column=0,padx=3,pady=3)

        boton_2 =  tk.Button(numeros_frame,text='2',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero2())
        boton_2.grid(row=0,column=1,padx=3,pady=3)

        boton_3 =  tk.Button(numeros_frame,text='3',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero3())
        boton_3.grid(row=0,column=2,padx=3,pady=3)
        ###########################################
        boton_4 =  tk.Button(numeros_frame,text='4',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero4())
        boton_4.grid(row=1,column=0,padx=3,pady=3)

        boton_5 =  tk.Button(numeros_frame,text='5',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero5())
        boton_5.grid(row=1,column=1,padx=3,pady=3)

        boton_6 =  tk.Button(numeros_frame,text='6',
                                  bg='#51db7b', activebackground = '#bac2bd',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero6(),state='disabled')
        boton_6.grid(row=1,column=2,padx=3,pady=3)
        ###########################################
        boton_7 =  tk.Button(numeros_frame,text='7',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero7())
        boton_7.grid(row=2,column=0,padx=3,pady=3)

        boton_8 =  tk.Button(numeros_frame,text='8',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero8())
        boton_8.grid(row=2,column=1,padx=3,pady=3)

        boton_9 =  tk.Button(numeros_frame,text='9',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero9())
        boton_9.grid(row=2,column=2,padx=3,pady=3)
    def numero7():
        global numero_actual
        numero_actual==7
        boton_1 =  tk.Button(numeros_frame,text='1',
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero1())
        boton_1.grid(row=0,column=0,padx=3,pady=3)

        boton_2 =  tk.Button(numeros_frame,text='2',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero2())
        boton_2.grid(row=0,column=1,padx=3,pady=3)

        boton_3 =  tk.Button(numeros_frame,text='3',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero3())
        boton_3.grid(row=0,column=2,padx=3,pady=3)
        ###########################################
        boton_4 =  tk.Button(numeros_frame,text='4',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero4())
        boton_4.grid(row=1,column=0,padx=3,pady=3)

        boton_5 =  tk.Button(numeros_frame,text='5',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero5())
        boton_5.grid(row=1,column=1,padx=3,pady=3)

        boton_6 =  tk.Button(numeros_frame,text='6',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero6())
        boton_6.grid(row=1,column=2,padx=3,pady=3)
        ###########################################
        boton_7 =  tk.Button(numeros_frame,text='7',
                                  bg='#51db7b', activebackground = '#bac2bd',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero7(),state='disabled')
        boton_7.grid(row=2,column=0,padx=3,pady=3)

        boton_8 =  tk.Button(numeros_frame,text='8',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero8())
        boton_8.grid(row=2,column=1,padx=3,pady=3)

        boton_9 =  tk.Button(numeros_frame,text='9',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero9())
        boton_9.grid(row=2,column=2,padx=3,pady=3)
    def numero8():
        global numero_actual
        numero_actual==8
        boton_1 =  tk.Button(numeros_frame,text='1',
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero1())
        boton_1.grid(row=0,column=0,padx=3,pady=3)

        boton_2 =  tk.Button(numeros_frame,text='2',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero2())
        boton_2.grid(row=0,column=1,padx=3,pady=3)

        boton_3 =  tk.Button(numeros_frame,text='3',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero3())
        boton_3.grid(row=0,column=2,padx=3,pady=3)
        ###########################################
        boton_4 =  tk.Button(numeros_frame,text='4',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero4())
        boton_4.grid(row=1,column=0,padx=3,pady=3)

        boton_5 =  tk.Button(numeros_frame,text='5',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero5())
        boton_5.grid(row=1,column=1,padx=3,pady=3)

        boton_6 =  tk.Button(numeros_frame,text='6',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero6())
        boton_6.grid(row=1,column=2,padx=3,pady=3)
        ###########################################
        boton_7 =  tk.Button(numeros_frame,text='7',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero7())
        boton_7.grid(row=2,column=0,padx=3,pady=3)

        boton_8 =  tk.Button(numeros_frame,text='8',
                                  bg='#51db7b', activebackground = '#bac2bd',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero8(),state='disabled')
        boton_8.grid(row=2,column=1,padx=3,pady=3)

        boton_9 =  tk.Button(numeros_frame,text='9',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero9())
        boton_9.grid(row=2,column=2,padx=3,pady=3)
    def numero9():
        global numero_actual
        numero_actual==9
        boton_1 =  tk.Button(numeros_frame,text='1',
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero1())
        boton_1.grid(row=0,column=0,padx=3,pady=3)

        boton_2 =  tk.Button(numeros_frame,text='2',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero2())
        boton_2.grid(row=0,column=1,padx=3,pady=3)

        boton_3 =  tk.Button(numeros_frame,text='3',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero3())
        boton_3.grid(row=0,column=2,padx=3,pady=3)
        ###########################################
        boton_4 =  tk.Button(numeros_frame,text='4',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero4())
        boton_4.grid(row=1,column=0,padx=3,pady=3)

        boton_5 =  tk.Button(numeros_frame,text='5',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero5())
        boton_5.grid(row=1,column=1,padx=3,pady=3)

        boton_6 =  tk.Button(numeros_frame,text='6',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero6())
        boton_6.grid(row=1,column=2,padx=3,pady=3)
        ###########################################
        boton_7 =  tk.Button(numeros_frame,text='7',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero7())
        boton_7.grid(row=2,column=0,padx=3,pady=3)

        boton_8 =  tk.Button(numeros_frame,text='8',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero8())
        boton_8.grid(row=2,column=1,padx=3,pady=3)

        boton_9 =  tk.Button(numeros_frame,text='9',
                                  bg='#51db7b', activebackground = '#bac2bd',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero9(),state='disabled')
        boton_9.grid(row=2,column=2,padx=3,pady=3)
    def resetear_numeral():
        boton_1 =  tk.Button(numeros_frame,text='1',
                              bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                         font=("Arial Black",14),command=lambda:numero1())
        boton_1.grid(row=0,column=0,padx=3,pady=3)

        boton_2 =  tk.Button(numeros_frame,text='2',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero2())
        boton_2.grid(row=0,column=1,padx=3,pady=3)

        boton_3 =  tk.Button(numeros_frame,text='3',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero3())
        boton_3.grid(row=0,column=2,padx=3,pady=3)
        ###########################################
        boton_4 =  tk.Button(numeros_frame,text='4',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero4())
        boton_4.grid(row=1,column=0,padx=3,pady=3)

        boton_5 =  tk.Button(numeros_frame,text='5',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero5())
        boton_5.grid(row=1,column=1,padx=3,pady=3)

        boton_6 =  tk.Button(numeros_frame,text='6',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero6())
        boton_6.grid(row=1,column=2,padx=3,pady=3)
        ###########################################
        boton_7 =  tk.Button(numeros_frame,text='7',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero7())
        boton_7.grid(row=2,column=0,padx=3,pady=3)

        boton_8 =  tk.Button(numeros_frame,text='8',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero8())
        boton_8.grid(row=2,column=1,padx=3,pady=3)

        boton_9 =  tk.Button(numeros_frame,text='9',
                                  bg='#bac2bd', activebackground = '#51db7b',height=1,width=3,
                             font=("Arial Black",14),command=lambda:numero9())
        boton_9.grid(row=2,column=2,padx=3,pady=3)
        


    #BOTONES DE JUEGO
    iniciar_boton= tk.Button(botones_frame,text=' Iniciar \n Juego ',
                              bg='#0b851b', activebackground = '#646e65',height=2,width=8,
                             font=("Arial Black",12), command=lambda:iniciar_partida() )
    iniciar_boton.grid(row=0,column=0,pady=5,padx=5)

    borrar_boton= tk.Button(botones_frame,text=' Borrar \n Juego ',
                              bg='#d40f26', activebackground = '#646e65',height=2,width=8,font=("Arial Black",12))
    borrar_boton.grid(row=0,column=1,pady=5,padx=5)

    terminar_boton= tk.Button(botones_frame,text=' Terminar \n Juego ',
                              bg='#ba4e18', activebackground = '#646e65',height=2,width=8,font=("Arial Black",12))
    terminar_boton.grid(row=0,column=3,pady=5,padx=5)

    deshacer_boton= tk.Button(botones_frame,text=' Deshacer \n Jugada ',
                              bg='#148bb3', activebackground = '#646e65',height=2,width=8,font=("Arial Black",12) )
    deshacer_boton.grid(row=1,column=0,pady=5,padx=5)

    rehacer_boton= tk.Button(botones_frame,text=' Rehacer \n Jugada  ',
                              bg='#148bb3', activebackground = '#646e65',height=2,width=8,font=("Arial Black",12) )
    rehacer_boton.grid(row=1,column=1,pady=5,padx=5)

    top_boton= tk.Button(botones_frame,text=' Top \n 10 ',
                              bg='#f5c507', activebackground = '#646e65',height=2,width=8,font=("Arial Black",12) )
    top_boton.grid(row=1,column=3,pady=5,padx=5)
    
    
    #CRONOMETRO Y TIMER

    
    
    #BOTONES DE GUARDAR Y CARGAR
    cargar_boton= tk.Button(botones2_frame,text=' Cargar \n Partida ',
                              bg='#148bb3', activebackground = '#646e65',height=2,width=8,font=("Arial Black",12) )
    cargar_boton.grid(row=0,column=0,pady=1,padx=5)

    guardar_boton= tk.Button(botones2_frame,text=' Guardar \n Partida  ',
                              bg='#148bb3', activebackground = '#646e65',height=2,width=8,font=("Arial Black",12) )
    guardar_boton.grid(row=0,column=1,pady=1,padx=5)

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
                                              bg='#e4e9f2', activebackground = '#a5a9b0',height=2,width=6 )
                            cuadro.grid(row=i,column=j,padx=2,pady=2)
                        else:
                            cuadro =  tk.Button(partida2_frame,text=lista[x][y][i][j],
                                              bg='#d4a763', activebackground = '#a5a9b0',height=2,width=6,state='disabled' )
                            cuadro.grid(row=i,column=j,padx=2,pady=2)

        
        
    def guardar_nombre():
        global nombre
        f=nombre_entry.get()
        if len(f)>30:
            showmessage('Error','El nombre no puede exeder los 30 caracteres')
            return
        nombre=f
        showmessage('Éxito',"El nombre se guardo correctamente")
        
        
    def iniciar_partida():
        #se arreglan aspectos respecto al nombre y se valida
        global nombre,lista
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
        imprimir(lista)
        if configuracion[3]=='dificil':
            
            pass
        if configuracion[3]=='facil':
            pass

        if configuracion[3]=='normal':
            pass

#funcion configuracion

def configuracion_sudoku():

    configuracionv=tk.Toplevel(ventana)
    configuracionv.title('2048 config')
    configuracionv.geometry('700x700')
    configuracionv.config(bg='#096eba')
    configuracionv.resizable(False,False)

    def set_timer():
        
        h = tk.Entry(conframe,bg="#defdff",width=2)
        h.grid(row=2,column=1,pady=1)
        m= tk.Entry(conframe,bg="#defdff",width=2)
        m.grid(row=2,column=2,pady=1)
        s= tk.Entry(conframe,bg="#defdff",width=2)
        s.grid(row=2,column=3,pady=1)
        set_time=tk.Button(conframe,text='Aceptar', bg='#3091db', activebackground = '#00d9fa',height=1,width=6,command=lambda :fijar_timer(h,m,s))
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
                showmessage('Error!','Timer vacio')
                return
            elif horas>4 or horas<0:
                showmessage('Error!','El formato ingresado es incorrecto')
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
                showmessage('Error!','El formato ingresado es incorrecto')
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
                showmessage('Error!','El formato ingresado es incorrecto')
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
            showmessage('Timer agregado','Pulse fijar configuración para guardar los datos de configuración')
            return
        except:
            showmessage('Error!','El formato ingresado es incorrecto')
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
        
                
                
            
            
        
    def fijar_config(reloj,dificultad):

        global configuracion,datos_timer,tipo_numeral,topx
        if datos_timer == (0,0,0) and reloj ==2:
           showmessage('Error!','Si desea usar la opcion Timer debe configurar '
                       'el tiempo deseado, antes de guardar los datos.')
           return
        if reloj==1 or reloj==3:
            datos_timer=(0,0,0)
            configuracion=(reloj,(0,0,0),dificultad,topx,tipo_numeral)
            messagebox.showinfo('Lo tenemos!','Informacion Guardada Correctamente!',parent=configuracionv)
            configuracionv.destroy()
        else:
            configuracion=(reloj,datos_timer,dificultad,topx,tipo_numeral)
            showmessage('Lo tenemos!','Informacion Guardada Correctamente!')
            configuracionv.destroy()
        
    #frame1
    conframe=tk.Frame(configuracionv,bg="#29d1ff",height=130,width=150)
    conframe.grid(row=0,column=0,padx=10,pady=10)
    #frame2
    conframe2=tk.Frame(configuracionv,bg="#29d1ff",height=130,width=150)
    conframe2.grid(row=1,column=0,padx=1,pady=1)
    #frame3
    conframe3=tk.Frame(configuracionv,bg="#b703ff",height=130,width=250)
    conframe3.grid(row=0,column=1,padx=1,pady=1)
    #opcion tiempo
    
    opcion=tk.IntVar()
    reloj=Radiobutton(conframe, text = "Cronómetro", value = 1,variable=opcion,width=12,
                      bg="#29d1ff",command=lambda:no_timer(),justify='left')
    reloj.select()
    reloj.grid(row=1,column=0)
    timer=Radiobutton(conframe, text = "Timer            ", value = 2,variable=opcion,width=12,
                      bg='#29d1ff',command=lambda:set_timer(),justify='left')
    timer.deselect()
    timer.grid(row=2,column=0)
    no=Radiobutton(conframe, text =    "Sin tiempo   ", value = 3,variable=opcion,width=12,
                   bg="#29d1ff",command=lambda:no_timer(),justify='left')
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
                       height=1,width=15,command=lambda :fijar_config(opcion.get(),opcion2.get())) 
    set_time.grid(row=4,column=0,padx=10,pady=10)
    
    
    cuadro = tk.Label(conframe2,bg="#2494b3",height=1,width=20,text='Dificultad',font=("Arial Black",13))
    cuadro.grid(row=0,column=0,padx=1,pady=1)
    opcion2=tk.IntVar()
    dificultad_facil=Radiobutton(conframe2, text = "Fácil", value = 1,variable=opcion2,width=5,bg="#2494b3")
    dificultad_facil.select()
    dificultad_facil.grid(row=1,column=0)
    
    dificultad_normal=Radiobutton(conframe2, text = "Normal", value = 2,variable=opcion2,width=5,bg="#2494b3")
    dificultad_normal.grid(row=2,column=0)
    
    dificultad_dificil=Radiobutton(conframe2, text = "Díficil", value = 3,variable=opcion2,width=5,bg="#2494b3")
    dificultad_dificil.grid(row=3,column=0)

   
#funcion ayuda
'''
Entradas: un click en la interfaz
Salidas: un pdf
Funcion: abre un pdf con el manual de usuario
'''
def ayuda():

    os.startfile('manual_de_usuario_sudoku.pdf')



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
