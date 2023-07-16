import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="elgranpoeta"
)

cursor = db.cursor()

def crear_categoria():
    try:
        nombre_categoria = input("Ingrese el nombre de la categoria: ")
        query = "INSERT INTO categoria (nombre_categoria) VALUES (%s)"
        values = (nombre_categoria,)
        cursor.execute(query, values)
        db.commit()
        print("Categoria creada exitosamente.")
    except mysql.connector.Error as error:
        print(error)
    finally:
        cursor.close()
        db.close()



def listar_categoria():
    try:
        query = "SELECT nombre_categoria FROM categoria"
        cursor.execute(query)
        result = cursor.fetchall()
        for categoria in result:
            print(f"\nNombre: {categoria[0]}")
    except mysql.connector.Error as error:
        print(error)
    finally:
        cursor.close()
        db.close()


def actualizar_categoria():
    try:
        id_categoria = input("Ingrese el ID de la categoria que desea actualizar: ")
        nuevo_nombre = input("Ingrese el nuevo nombre de la categoria: ")
        query = "UPDATE categoria SET nombre_categoria = %s WHERE id_categoria = %s"
        values = (nuevo_nombre, id_categoria)
        cursor.execute(query, values)
        db.commit()
        print("Categoria actualizada exitosamente.")
    except mysql.connector.Error as error:
        print(error)
    finally:
        cursor.close()
        db.close()



def eliminar_categoria():
    try:
        id_categoria = input("Ingrese el ID de la categoria que desea eliminar: ")
        
        # Verificar si la categoria está en uso
        query_check = "SELECT COUNT(*) FROM producto WHERE id_categoria = %s"
        values_check = (id_categoria,)
        cursor.execute(query_check, values_check)
        result_check = cursor.fetchone()

        if result_check[0] > 0:
            print("No se puede eliminar la categoria. Está en uso por uno o más productos.")
        else:
            query_delete = "DELETE FROM categoria WHERE id_categoria = %s"
            values_delete = (id_categoria,)
            cursor.execute(query_delete, values_delete)
            db.commit()
            print("Categoria eliminada exitosamente.")
    except mysql.connector.Error as error:
        print(error)
    finally:
        cursor.close()
        db.close()



def mostrar_menu():
    while True:
        print("\n----- CATEGORIA -----")
        print("1. Crear categoria")
        print("2. Mostrar categorias")
        print("3. Actualizar categoria")
        print("4. Eliminar categoria")
        print("0. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            crear_categoria()
        elif opcion == "2":
            listar_categoria()
        elif opcion == "3":
            actualizar_categoria()
        elif opcion == "4":
            eliminar_categoria()
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intente nuevamente.")
