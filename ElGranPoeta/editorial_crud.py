import mysql.connector

midb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="elgranpoeta"
)

cursor = midb.cursor()

def crear_editorial():
    try:
        cursor = midb.cursor()
        nombre_editorial = input("Ingrese el nombre de la editorial: \n")
        query = "INSERT INTO editorial (nombre_editorial) VALUES (%s)"
        values = (nombre_editorial,)
        cursor.execute(query, values)
        midb.commit()
        print("Editorial creada exitosamente.")
    except mysql.connector.Error as error:
        print(error)
    finally:
        cursor.close()



def listar_editorial():
    try:
        cursor = midb.cursor()
        query = "SELECT * FROM editorial"
        cursor.execute(query)
        result = cursor.fetchall()
        for editorial in result:
            print(f"Nombre: {editorial[1]}")
    except mysql.connector.Error as error:
        print(error)
    finally:
        cursor.close()



def actualizar_editorial():
    try:
        cursor = midb.cursor()
        id_editorial = input("Ingrese el ID de la editorial que desea actualizar: ")
        nuevo_nombre = input("Ingrese el nuevo nombre de la editorial: ")
        query = "UPDATE editorial SET nombre_editorial = %s WHERE id_editorial = %s"
        values = (nuevo_nombre, id_editorial)
        cursor.execute(query, values)
        midb.commit()
        print("Editorial actualizada exitosamente.")
    except mysql.connector.Error as error:
        print(error)
    finally:
        cursor.close()



def eliminar_editorial():
    try:
        cursor = midb.cursor()
        id_editorial = input("Ingrese el ID de la editorial que desea eliminar: ")
        query = "SELECT COUNT(*) FROM producto WHERE id_editorial = %s"
        values = (id_editorial,)
        cursor.execute(query, values)
        result = cursor.fetchone()

        if result[0] > 0:
            print("No se puede eliminar la editorial. Está en uso por uno o más productos.")
        else:
            query_delete = "DELETE FROM editorial WHERE id_editorial = %s"
            values_delete = (id_editorial,)
            cursor.execute(query_delete, values_delete)
            midb.commit()
            print("Editorial eliminada exitosamente.")
    except mysql.connector.Error as error:
        print(error)
    finally:
        cursor.close()

def mostrar_menu():
    while True:
        print("\n----- EDITORIAL -----")
        print("1. Crear editorial")
        print("2. Leer editoriales")
        print("3. Actualizar editorial")
        print("4. Eliminar editorial")
        print("0. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            crear_editorial()
        elif opcion == "2":
            listar_editorial()
        elif opcion == "3":
            actualizar_editorial()
        elif opcion == "4":
            eliminar_editorial()
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intente nuevamente.")
