import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="elgranpoeta"
)

cursor = db.cursor()

def crear_empleado():
    cursor = db.cursor()
    nombre_empleado = input("Nombre del empleado: ")
    id_cargo = int(input("ID del cargo: "))
    id_bodega = int(input("ID de la bodega: "))

    try:
        query = "INSERT INTO empleado (nombre_empleado, id_cargo, id_bodega) VALUES (%s, %s, %s)"
        values = (nombre_empleado, id_cargo, id_bodega)
        cursor.execute(query, values)
        db.commit()
        print("Empleado creado exitosamente.")
    except mysql.connector.Error as error:
        print("Error al crear el empleado:", error)
    finally:
        cursor.close()



def listar_empleados():
    try:
        cursor = db.cursor()
        query = "SELECT e.id_empleado, e.nombre_empleado, c.nombre_cargo, b.nombre_bodega FROM empleado e JOIN cargo c ON e.id_cargo = c.id_cargo JOIN bodega b ON e.id_bodega = b.id_bodega"
        cursor.execute(query)
        empleados = cursor.fetchall()

        if len(empleados) > 0:
            print("--- EMPLEADOS ---")
            for empleado in empleados:
                print("ID:", empleado[0])
                print("Nombre:", empleado[1])
                print("Cargo:", empleado[2])
                print("Bodega:", empleado[3])
                print("-----------------")
        else:
            print("No hay empleados en la base de datos.")
    except mysql.connector.Error as error:
        print("Error al leer los empleados:", error)
    finally:
        cursor.close()



def actualizar_empleado():
    cursor = db.cursor()
    id_empleado = int(input("ID del empleado a actualizar: "))
    nombre_empleado = input("Nombre del empleado: ")
    id_cargo = int(input("ID del cargo: "))
    id_bodega = int(input("ID de la bodega: "))

    try:
        query = "UPDATE empleado SET nombre_empleado = %s, id_cargo = %s, id_bodega = %s WHERE id_empleado = %s"
        values = (nombre_empleado, id_cargo, id_bodega, id_empleado)
        cursor.execute(query, values)
        db.commit()
        print("Empleado actualizado exitosamente.")
    except mysql.connector.Error as error:
        print("Error al actualizar el empleado:", error)
    finally:
        cursor.close()

def mostrar_menu():
    while True:
        print("--- EMPLEADO ---")
        print("1. Crear empleado")
        print("2. Listar empleados")
        print("3. Actualizar empleado")
        print("4. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            crear_empleado()
        elif opcion == "2":
            listar_empleados()
        elif opcion == "3":
            actualizar_empleado()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

