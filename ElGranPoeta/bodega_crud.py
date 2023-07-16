import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nS3cR3t",
    database="ELGRANPOETA"
)

cursor = db.cursor()


def mostrar_menu():
    print("--- BODEGA ---")
    print("1. Crear bodega")
    print("2. Listar bodegas")
    print("3. Actualizar bodega")
    print("4. Eliminar bodega")
    print("5. Salir")


def crear_bodega():
    nombre_bodega = input("Nombre de la bodega: ")
    ubicacion = input("Ubicación de la bodega: ")

    try:
        query = "INSERT INTO bodega (nombre_bodega, ubicacion) VALUES (%s, %s)"
        values = (nombre_bodega, ubicacion)
        cursor.execute(query, values)
        db.commit()
        print("Bodega creada exitosamente.")
    except mysql.connector.Error as error:
        print("Error al crear la bodega:", error)


def listar_bodegas():
    try:
        query = "SELECT * FROM bodega"
        cursor.execute(query)
        bodegas = cursor.fetchall()

        if len(bodegas) > 0:
            print("--- BODEGAS ---")
            for bodega in bodegas:
                print("ID:", bodega[0])
                print("Nombre:", bodega[1])
                print("Ubicación:", bodega[2])
                print("-----------------")
        else:
            print("No hay bodegas en la base de datos.")
    except mysql.connector.Error as error:
        print("Error al leer las bodegas:", error)


def actualizar_bodega():
    id_bodega = int(input("ID de la bodega a actualizar: "))
    nombre_bodega = input("Nuevo nombre de la bodega: ")
    ubicacion = input("Nueva ubicación de la bodega: ")

    try:
        query = "UPDATE bodega SET nombre_bodega = %s, ubicacion = %s WHERE id_bodega = %s"
        values = (nombre_bodega, ubicacion, id_bodega)
        cursor.execute(query, values)
        db.commit()
        print("Bodega actualizada exitosamente.")
    except mysql.connector.Error as error:
        print("Error al actualizar la bodega:", error)


def eliminar_bodega():
    id_bodega = int(input("ID de la bodega a eliminar: "))

    try:
        query = "DELETE FROM bodega WHERE id_bodega = %s"
        value = (id_bodega,)
        cursor.execute(query, value)
        db.commit()
        print("Bodega eliminada exitosamente.")
    except mysql.connector.Error as error:
        print("Error al eliminar la bodega:", error)


while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        crear_bodega()
    elif opcion == "2":
        listar_bodegas()
    elif opcion == "3":
        actualizar_bodega()
    elif opcion == "4":
        eliminar_bodega()
    elif opcion == "5":
        break
    else:
        print("Opción inválida. Intente nuevamente.")


cursor.close()
db.close()
