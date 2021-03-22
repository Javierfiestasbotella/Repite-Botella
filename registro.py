from bbdd import *


def usuario():
  global usser
  usser=input("Introduce un usuario : ")
  if len(usser)<5 or len(usser)>15:
    print("El usuario debe tener entre 5 y 15 caracteres")
    usuario()
  elif usser.isalnum()==False:
    print("Los valores del usurio deben ser únicamente letras o números")
    usuario()
  else:
    print(True)



def contraseña():
  global passw
  passw=input("Introduce contraseña: ")
  if len(passw)<=9:
    print("La contraseña debe tener al menos 10 caractéres")
    contraseña()
  elif passw.isalnum()==True:
    print ("La contraseña debe tener al menos un carácter no alfanumérico")
    contraseña()
  elif passw.lower() == passw:
    print("Debe haber por lo menos una mayúscula")
    contraseña()
  elif passw.upper()==passw:
    print("Debe haber por lo menos una minúscula")
    contraseña()

  for i in passw:
    if i==" ":
      print("La contraseña no debe tener espacios en blanco")
      contraseña()
  print(True)
