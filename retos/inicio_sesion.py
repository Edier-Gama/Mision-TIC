#Se incia el programa dando una bienvenida

print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

#Se generan las variables predefinidas de inicio de sesión, el nombre corresponde al codigo del grupo y la contraseña al codigo del programa

name = "51"
password = "60"
captcha = "6"

#El sistema pide los datos de ingreso y los valida

user = input(("Ingrese su nombre de usuario: "))

if (user==name):
   
  password_1= input(("Digite su contraseña: "))
  
  if (password_1 == password):
    
    captcha_solution = input(("CAPTCHA:¿Cuál es el resultado de 1 + 5? "))
    if (captcha_solution == captcha):
      from menu import menu
      menu()  
    else:
      print("Error")
      exit()
  else:
    print("Error")
    exit()

else:
  print("Error")
  exit()

#Fin del programa