# -*- coding: utf-8 -*-
from random import randrange, choice
import random
from playsound import playsound
import sys
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
#from tkinter import ttk, font
import time as t
from data import * 

class Saimon():
    def __init__(self):
        self.memoria=[]
        self.acumulado=""
        self.aya=playsound('Repite Botella/aya.mp3')
        self.oyo=playsound('Repite Botella/oyo.mp3')
        self.pi=playsound('Repite Botella/pi.mp3')
        self.itimiti=playsound('Repite Botella/itimiti.mp3')
        self.udupapa=playsound('Repite Botella/udupapa.mp3')
        self.sonidos=["aya","oyo","pi","udupapa","itimiti"]
        self.aglomerado=[]
        self.r=[]   
        
    def convertir_a_sonido(self,string):#convierte los string de sonodos en SONIDOS
        for i in string:
            if i=="aya":
              playsound('Repite Botella/aya.mp3')
            elif i=="oyo":
              playsound("Repite Botella/oyo.mp3")
            elif i=="pi":
              playsound("Repite Botella/pi.mp3")
            elif i=="udupapa":
              playsound("Repite Botella/udupapa.mp3")
            elif i=="itimiti":
              playsound("Repite Botella/itimiti.mp3")
            
    def comprobar_nivel(self,nivel):
      self.contador=len(self.aglomerado)+1
      while nivel!=self.contador:
        secuencia=random.choice(self.sonidos)
        self.aglomerado.append(secuencia)
        self.contador=self.contador+1
      #s.convertir_a_sonido(self.aglomerado)
      print(self.aglomerado)
      #return self.aglomerado


    def rafaga(self):#rafaga hay autocompleta el 4 con la variable nivel
        print(database.passw)
        database.select_user(e1.get()) 
        print("--------------")
        print(database.passw)
        global user     
        self.texto2.set("")
        s.comprobar_nivel(database.passw)
        #s.convertir_a_sonido(self.aglomerado)   
        secuencia=random.choice(self.sonidos)
        self.aglomerado.append(secuencia)
        s.convertir_a_sonido(self.aglomerado)
        self.boton7=Button(self.raiz,text="Start",bg="#1846FF", activebackground="#FA2821",relief="raised", borderwidth=3,width=8, height=2,command=s.rafaga,state=DISABLED).place(x=210,y=50)
        nivel=len(self.aglomerado)
        self.texto.set("NIVEL "+str(nivel),)
        
    def off_on(self):#dá vida a los botones

      self.boton7=Button(self.raiz,text="Start",bg="#1846FF", activebackground="#FA2821",relief="raised", borderwidth=3,width=8, height=2,command=s.rafaga).place(x=210,y=50)
      self.boton8=Button(self.raiz,text="Comprobar",bg="#fce493", activebackground="#FA2821",relief="raised", borderwidth=3,width=8, height=2,command=s.paso_nivel).place(x=210,y=100)
      self.boton9=Button(self.raiz,text="Repetir",bg="#F50505", activebackground="#FA2821",relief="raised", borderwidth=3,width=8, height=2,command=s.oportunidad).place(x=210,y=200)
      self.boton10=Button(self.raiz,text="Reiniciar",bg="#FD0F42", activebackground="#FA2821",relief="raised", borderwidth=3,width=8, height=2,command=s.reinicio).place(x=210,y=150)
      self.tronco.destroy()

    def inicio_sesion(self):#inicia sesion introduciondo datos en data.py
      database.inicio_de_sesion(e1.get(),e2.get())
      self.boton7=Button(self.raiz,text="Start",bg="#1846FF", activebackground="#FA2821",relief="raised", borderwidth=3,width=8, height=2,command=s.rafaga).place(x=210,y=50)
      self.boton8=Button(self.raiz,text="Comprobar",bg="#fce493", activebackground="#FA2821",relief="raised", borderwidth=3,width=8, height=2,command=s.paso_nivel).place(x=210,y=100)
      self.boton9=Button(self.raiz,text="Repetir",bg="#F50505", activebackground="#FA2821",relief="raised", borderwidth=3,width=8, height=2,command=s.oportunidad).place(x=210,y=200)
      self.boton10=Button(self.raiz,text="Reiniciar",bg="#FD0F42", activebackground="#FA2821",relief="raised", borderwidth=3,width=8, height=2,command=s.reinicio).place(x=210,y=150)
      self.nombre_usuario=database.nombre_escrito
      self.tronco.destroy()
      self.rama1.destroy()

    def registrarse(self):#conecta con data.py para registrar los datos en mysql
      database.registrar(e1.get(),e2.get())
      self.tronco.destroy()
    
    def paso_nivel(self):#comprueba si has acertado la secuencia
      if self.r==self.aglomerado:
        self.texto2.set("ACERTASTE!!!")
        playsound("Repite Botella/awaka.mp3")
        self.boton7=Button(self.raiz,text="Start",bg="#1846FF", activebackground="#FA2821",relief="raised", borderwidth=3,width=8, height=2,command=s.rafaga).place(x=210,y=50)
        database.update_user(len(self.aglomerado),e1.get())
        self.r=[]
      else:
        #messagebox.showinfo(message="Lo siento, vuelve a intentarlo", title="Título")
        playsound("Repite Botella/fallo.mp3")

        self.r=[]     
        
    def suena(self,a,b):#crea sonido y lo añade a una lista
        a
        self.r.append(b)   
        #print(self.r)

    def reinicio(self):#reiniciar a nivel 1
      p=messagebox.askyesno(message="¿Seguro que quiere reiniciar al nivel 1?", title="Alerta!!!")
      
      if p==True:
        print("funciona")
        database.update_user(1,e1.get())
        self.aglomerado=[]
        self.r=[]
        self.boton7=Button(self.raiz,text="Start",bg="#1846FF", activebackground="#FA2821",relief="raised", borderwidth=3,width=8, height=2,command=s.rafaga).place(x=210,y=50)

    def oportunidad(self):#repetir secuencia
      s.convertir_a_sonido(self.aglomerado)

    def interfaz(self):#pantalla interfaz principal
      self.raiz=Tk()
      self.nombre_usuario="Bienvenido!!!"
      self.raiz.geometry("280x290+0+0")
      self.raiz.iconbitmap("rubik.ico")
      self.raiz.title(self.nombre_usuario)
      self.texto=StringVar()
      self.texto2=StringVar()
      self.texto.set("NIVEL")

      self.fondo=PhotoImage(file="Repite Botella/myAvatari (1).gif",width=203,height=248)
      self.lblFondo=Label(self.raiz,image=self.fondo).place(x=0,y=0)

      Label(self.raiz,text="BOTELLA",bg="black",fg="white",font="arcade").place(x=70,y=5)
      self.boton1=Button(self.raiz,text="",bg="#f0c4b0", height=0 ,activebackground="#FA2821",relief="flat",command=lambda:s.suena(playsound("Repite Botella/udupapa.mp3"),"udupapa")).place(x=97,y=180)

      self.boton2=Button(self.raiz,text="",bg="#f0c4b0",height=0 ,activebackground="#FA2821",relief="flat",command=lambda:s.suena(playsound("Repite Botella/itimiti.mp3"),"itimiti")).place(x=97,y=61)

      self.boton3=Button(self.raiz,text="",bg="#f0c4b0", activebackground="#FA2821",relief="flat",command=lambda:s.suena(playsound("Repite Botella/pi.mp3"),"pi")).place(x=97,y=121)
      self.boton4=Button(self.raiz,text="",bg="#f0c4b0",activebackground="#FA2821",relief="flat",command=lambda:s.suena(playsound("Repite Botella/oyo.mp3"),"oyo")).place(x=35,y=111)
      self.boton5=Button(self.raiz,text="",bg="#f0c4b0",activebackground="#FA2821",relief="flat",command=lambda:s.suena(playsound("Repite Botella/aya.mp3"),"aya")).place(x=160,y=111)

      self.nombre_usuario=Label(self.raiz).place(x=210,y=5)
      self.boton7a=Button(self.raiz,text="Iniciar Sesión",bg="black",fg="white", activebackground="#FA2821",relief="raised", borderwidth=3,width=12, height=2,command=s.usuario).place(x=175,y=5)

      self.boton7=Button(self.raiz,text="Start",bg="#1846FF", activebackground="#FA2821",relief="raised", borderwidth=3,width=8, height=2,command=s.rafaga,state=DISABLED).place(x=210,y=50)
      self.boton8=Button(self.raiz,text="Comprobar",bg="#fce493", activebackground="#FA2821",relief="raised", borderwidth=3,width=8, height=2,command=s.paso_nivel,state=DISABLED).place(x=210,y=100)
      self.boton9=Button(self.raiz,text="Repetir",bg="#F50505", activebackground="#FA2821",relief="raised", borderwidth=3,width=8, height=2,command=s.oportunidad,state=DISABLED).place(x=210,y=200)
      self.boton10=Button(self.raiz,text="Reiniciar",bg="#FD0F42", activebackground="#FA2821",relief="raised", borderwidth=3,width=8, height=2,command=s.reinicio,state=DISABLED).place(x=210,y=150)
      self.mensaje=Label(self.raiz,textvariable=self.texto2,font="arcade 10",fg="blue").place(x=50,y=230)
      self.posicion=Label(self.raiz,textvariable=self.texto,font="arcade 20",bg="#31677B",fg="white").place(x=50,y=250)
      self.raiz.mainloop()

    def poner_nombre(self):
      self.raiz.title(self.nombre_usuario)
      self.nombre_usuario=database.nombre_escrito
      
    
    def usuario(self):#pantalla a elegir usuario o registrarse
      self.tronco=Toplevel(self.raiz)
      self.tronco.geometry("280x290+0+0")
      self.tronco.title("iniciar o registrarse")
      self.tronco.iconbitmap("rubik.ico")


      self.etiqueta=Label(self.tronco,text="Inicie Sesión o Regístrese:",bg="blue",fg="white",width="300",height="2",font=("calibri",12)).pack()
      Label(self.tronco,text="").pack()
      self.boton_inicio=Button(self.tronco,text="Iniciar Sesion",height="3",width="30",bg="green",fg="white",font=("calibri",10),command=s.pantalla_inicio).pack()
      Label(self.tronco,text="").pack()
      self.boton_registrarse=Button(self.tronco,text="Registrarse",height="3",width="30",bg="green",fg="white",font=("calibri",10),command=s.pantalla_registro).pack()

      self.tronco.mainloop()

    def pantalla_inicio(self):#aquí hay que crear interfaz de ingrese datos
     
      global e1
      global e2
      e1=StringVar()
      e2=StringVar()
      self.rama1=Toplevel(self.tronco)
      self.rama1.geometry("280x290+0+0")
      self.rama1.title("iniciar Sesión")
      self.rama1.configure(bg="gray93")
      self.rama1.iconbitmap("rubik.ico")

      Label(self.rama1, text="Por favor ingrese los siguientes datos",bg="blue",fg="white",width="300",height="2",font=("calibri",12)).pack()
      Label(self.rama1, text="").pack()
      #self.prueba=database.select_user(self.usuario_usu)
      self.etiqueta_usuario=Label(self.rama1,text="Usuario",font='helvetica').pack()
      self.espacio1=Entry(self.rama1,textvariable=e1).pack()
      self.etiqueta_contraseña=Label(self.rama1,text="Contraseña",font='italic').pack()
      self.espacio2=Entry(self.rama1,show="*" ,textvariable=e2)
      self.espacio2.pack()
      Label(self.rama1).pack()
      self.boton_enviar_datos=Button(self.rama1,text="Enviar", relief="raised", borderwidth=5,height="1",width="8",bg="beige",fg="green",font=("calibri",20),command=s.inicio_sesion).pack()
      self.rama1.mainloop()

    def comprobar_contraseña(self):#comprueba que las dos contraseñas son iguales en el registro de nuevo usuario
      if e2.get()!=e3.get():
        messagebox.showinfo(message="Las contraseñas no coinciden, compruebelas", title="Contraseña errónea")
        #self.boton_enviar_datos=Button(self.rama2,text="Enviar", relief="raised", borderwidth=5,height="1",width="8",bg="beige",fg="green",font=("calibri",20),command=s.registrarse,state=DISABLED).pack()
      else:
        self.boton_enviar_datos=Button(self.rama2,text="Enviar", relief="raised", borderwidth=5,height="1",width="8",bg="beige",fg="green",font=("calibri",20),command=s.registrarse).pack()

    def pantalla_registro(self):#registrar un usuario nuevo
      global e1
      global e2
      global e3
      e1=StringVar()
      e2=StringVar()
      e3=StringVar()
      self.rama2=Toplevel(self.tronco)
      self.rama2.geometry("280x380+0+0")
      self.rama2.title("Registrar Usuario")
      self.rama2.configure(bg="gray93")
      self.rama2.iconbitmap("rubik.ico")

      Label(self.rama2, text="Por favor ingrese los siguientes datos",bg="blue",fg="white",width="300",height="2",font=("calibri",12)).pack()
      Label(self.rama2, text="").pack()
      #self.prueba=database.select_user(self.usuario_usu)
      self.etiqueta_usuario=Label(self.rama2,text="Usuario",font='helvetica').pack()
      self.espacio1=Entry(self.rama2,textvariable=e1).pack()
      
      self.etiqueta_contraseña=Label(self.rama2,text="Contraseña",font='italic').pack()
      self.espacio2=Entry(self.rama2,show="*" ,textvariable=e2)
      self.espacio2.pack()
      Label(self.rama2).pack()
      
      self.etiqueta_contraseña2=Label(self.rama2,text="Vuelve a escribir la contraseña",font='italic').pack()
      self.espacio3=Entry(self.rama2,show="*" ,textvariable=e3)
      self.espacio3.pack()
      Label(self.rama2).pack()
      self.boton_enviar_contraseña=Button(self.rama2,text="Comprobar Contraseña", relief="raised", borderwidth=5,width="20",bg="beige",fg="green",font=("calibri",20),command=s.comprobar_contraseña).pack()
      Label(self.rama2).pack()
      #self.boton_enviar_datos=Button(self.rama2,text="Enviar", relief="raised", borderwidth=5,height="1",width="8",bg="beige",fg="green",font=("calibri",20),command=s.registrarse,state=DISABLED).pack()
      self.rama2.mainloop()
     

      

s = Saimon()

s.interfaz()
#s.comprobar_nivel(1)


   
   

     