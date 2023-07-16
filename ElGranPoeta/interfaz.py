import main
import categoria_crud
import editorial_crud
import producto_crud

print("""
Selecciona el numero de usuario que ingresara
1.- Supervisor
2.- Jefe Bodegas
3.- Bodeguero
""")

while True:
    userSelect = int(input("Selecciona= "))
    if userSelect == 1:
        usuario = "Supervisor"
        break
    elif userSelect == 2:
        usuario = "JefeBodegueros"
        break
    elif userSelect == 3:
        usuario = "Bodeguero"
        break
    else:
         print("asegurate de seleccionar el numero correcto")


while True:
    password = input("Ingrese contraseña= ")
    try:  
        main.login(usuario,password)
        break
    except:
        print("Intente una contrasena diferente")

if userSelect == 1:
    print("""
Operaciones para realizar =
1.- Cambiar contrasena de usuario
    """)

    operacionRealizar = int(input("Selecciona= "))
    if operacionRealizar == 1:
        print("""La lista de usuarios es= 
1.- Supervisor
2.- Jefe Bodegueros
3.- Bodeguero                                 
        """)
        while True:
            selectUser = int(input("Seleccionar Usuario= "))
            if selectUser == 1 or selectUser == 2 or selectUser == 3:
                if selectUser == 1:
                    selectUser = "Supervisor"
                elif selectUser == 2:
                    selectUser = "JefeBodegueros"
                elif selectUser == 3:
                    selectUser = "Bodeguero"
                newpass = input("nueva contrasena= ")
                main.passChange(selectUser, newpass)
                print("Contrasena cambiada con exito")
                break
            else:
                print("Selecciona el numero de un usuario existente")

elif userSelect == 2:
    print("""
Operaciones para realizar =
1.- Modificar Categorias
2.- Modificar Editoriales
3.- Modificar Productos
    """)
    operacionRealizar = int(input("Selecciona= "))
    if operacionRealizar == 1:
        categoria_crud.mostrar_menu()
    elif operacionRealizar == 2:
        editorial_crud.mostrar_menu()
    elif operacionRealizar == 3:
        producto_crud.mostrar_menu()

