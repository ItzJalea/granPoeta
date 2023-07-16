import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="elgranpoeta"
)

cursor = db.cursor()


def mostrar_menu():
    print("--- MOVIMIENTO DE PRODUCTOS ---")
    print("1. Agregar productos a una bodega")
    print("2. Sacar productos de una bodega")
    print("3. Generar documento de movimiento")
    print("4. Salir")


def agregar_productos():
    id_bodega_origen = int(input("ID de la bodega de origen: "))
    id_bodega_destino = int(input("ID de la bodega de destino: "))
    id_producto = int(input("ID del producto: "))
    cantidad = int(input("Cantidad a agregar: "))
    id_empleado = int(input("ID del empleado que realiza el movimiento: "))

    try:
        query = "UPDATE stock SET cantidad_stock = cantidad_stock + %s WHERE id_bodega = %s AND id_producto = %s"
        values = (cantidad, id_bodega_destino, id_producto)
        cursor.execute(query, values)
        db.commit()
        print("Productos agregados exitosamente a la bodega de destino.")

        query = "INSERT INTO movimiento (fecha_movimiento, id_bodega_origen, id_bodega_destino, id_empleado, id_detalle) VALUES (CURDATE(), %s, %s, %s, %s)"
        values = (id_bodega_origen, id_bodega_destino, id_empleado, id_producto)
        cursor.execute(query, values)
        db.commit()
        print("Documento de movimiento generado exitosamente.")
    except mysql.connector.Error as error:
        print("Error al agregar los productos o generar el documento de movimiento:", error)


def sacar_productos():
    id_bodega = int(input("ID de la bodega: "))
    id_producto = int(input("ID del producto: "))
    cantidad = int(input("Cantidad a sacar: "))
    id_empleado = int(input("ID del empleado que realiza el movimiento: "))

    try:
        query = "UPDATE stock SET cantidad_stock = cantidad_stock - %s WHERE id_bodega = %s AND id_producto = %s"
        values = (cantidad, id_bodega, id_producto)
        cursor.execute(query, values)
        db.commit()
        print("Productos sacados exitosamente de la bodega.")

        query = "INSERT INTO movimiento (fecha_movimiento, id_bodega_origen, id_bodega_destino, id_empleado, id_detalle) VALUES (CURDATE(), %s, %s, %s, %s)"
        values = (id_bodega, id_bodega, id_empleado, id_producto)
        cursor.execute(query, values)
        db.commit()
        print("Documento de movimiento generado exitosamente.")
    except mysql.connector.Error as error:
        print("Error al sacar los productos o generar el documento de movimiento:", error)


def generar_documento_movimiento():
    try:
        query = "SELECT m.id_movimiento, m.fecha_movimiento, b1.nombre_bodega AS bodega_origen, b2.nombre_bodega AS bodega_destino, d.cantidad, p.nombre AS nombre_producto, e.nombre_empleado FROM movimiento m JOIN bodega b1 ON m.id_bodega_origen = b1.id_bodega JOIN bodega b2 ON m.id_bodega_destino = b2.id_bodega JOIN detalle d ON m.id_detalle = d.id_detalle JOIN producto p ON d.id_producto = p.id_producto JOIN empleado e ON m.id_empleado = e.id_empleado ORDER BY m.id_movimiento DESC LIMIT 1"
        cursor.execute(query)
        movimiento = cursor.fetchone()

        if movimiento:
            print("--- Último movimiento realizado ---")
            print("ID de movimiento:", movimiento[0])
            print("Fecha de movimiento:", movimiento[1])
            print("Bodega de origen:", movimiento[2])
            print("Bodega de destino:", movimiento[3])
            print("Cantidad de productos:", movimiento[4])
            print("Nombre del producto:", movimiento[5])
            print("Empleado que realizó el movimiento:", movimiento[6])
            print("----------------------------------")
        else:
            print("No se encontró información del último movimiento.")
    except mysql.connector.Error as error:
        print("Error al generar el documento de movimiento:", error)



while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        agregar_productos()
    elif opcion == "2":
        sacar_productos()
    elif opcion == "3":
        generar_documento_movimiento()
    elif opcion == "4":
        break
    else:
        print("Opción inválida. Intente nuevamente.")


cursor.close()
db.close()
