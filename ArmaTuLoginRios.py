"""Para tu primera entrega, te proponemos que crees un programa que permita emular el registro y almacenamiento de usuarios en una base de datos. Hazlo utilizando el concepto de funciones, diccionarios, bucles y condicionales.

Objetivos
Practicar el concepto de funciones.

Desarrollar la parte lógica para el registro de usuarios.

Requisitos
Diccionarios (guardado de datos)

Input (solicitud de datos)

Variables

If (chequeo de datos)

While (iteración para el programa, sea para agregar, loguear o mostrar)

For (recorrer datos y para búsqueda)

Print

Funciones separadas para registro, almacenamiento y muestra

Recomendaciones
El formato de registro es: Nombre de usuario y Contraseña.

Utilizar una función para almacenar la información y otra función para mostrar la información.

Utilizar un diccionario para almacenar dicha información, con el par usuario-contraseña (clave-valor).

Utilizar otra función para el login de usuarios, comprobando que la contraseña coincida con el usuario.

Formato
El proyecto debe compartirse utilizando Colab bajo el nombre “ArmaTuLogin+Apellido”, por ejemplo “ArmaTuLogin+Fernandez”"""

usuarios = {
    "Micu" : "1234",
    "Zeus" : "7894",
    "Daisy" : "4567"
}

def alta_usuario ():
    print("Alta de usuario")
    nombre = input("Ingrese el nombre del usuario: ")
    contrasenia = input("Ingrese la contraseña del usuario: ")
    usuarios[nombre] = contrasenia
    
def mostrar_usuarios ():
    print(usuarios.keys())
    
def login (usuario, contrasenia):
    for clave, valor in usuarios.items():
        if usuario == clave and contrasenia == valor:
            print("Ha ingresado sesion exitosamente")
            break
        else: 
            print("Usuario y/o contraseña incorrectos") 
                  
def main ():
    opcion = 1
    while opcion > 0:
        print("1- Alta de usuario\n"
            "2- Ver usuarios\n"
            "3- Login\n"
            "0- Salir")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            alta_usuario()
        elif opcion == 2:
            mostrar_usuarios()
        elif opcion == 3:
            usuario = input("Ingrese su usuario: ")
            contrasenia = input("Ingrese su contraseña: ")
            login(usuario, contrasenia)

main()