import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="elgranpoeta"
)

cursor = db.cursor()

def mover_productos():
    id_bodega_origen = int(input("ID de la bodega de origen: "))
    id_bodega_destino = int(input("ID de la bodega de destino: "))
    id_producto = int(input("ID del producto: "))
    cantidad_a_mover = int(input("Cantidad a mover: "))
    id_empleado = int(input("ID del empleado que realiza el movimiento: "))

    try:
        cursor = db.cursor()
        # Verificar si hay suficiente stock en la bodega de origen
        query_stock_origen = "SELECT cantidad_stock FROM stock WHERE id_bodega = %s AND id_producto = %s"
        values_stock_origen = (id_bodega_origen, id_producto)
        cursor.execute(query_stock_origen, values_stock_origen)
        stock_origen = cursor.fetchone()

        if not stock_origen or stock_origen[0] < cantidad_a_mover:
            print("No hay suficiente stock en la bodega de origen.")
            return

        # Actualizar el stock en la bodega de origen
        query_update_origen = "UPDATE stock SET cantidad_stock = cantidad_stock - %s WHERE id_bodega = %s AND id_producto = %s"
        values_update_origen = (cantidad_a_mover, id_bodega_origen, id_producto)
        cursor.execute(query_update_origen, values_update_origen)
        db.commit()
        print("Productos movidos exitosamente desde la bodega de origen.")

        # Actualizar el stock en la bodega de destino
        query_update_destino = "UPDATE stock SET cantidad_stock = cantidad_stock + %s WHERE id_bodega = %s AND id_producto = %s"
        values_update_destino = (cantidad_a_mover, id_bodega_destino, id_producto)
        cursor.execute(query_update_destino, values_update_destino)
        db.commit()
        print("Productos movidos exitosamente a la bodega de destino.")

        # Insertar el registro de movimiento
        query_insert_movimiento = "INSERT INTO movimiento (fecha_movimiento, id_bodega_origen, id_bodega_destino, id_empleado, id_detalle) VALUES (CURDATE(), %s, %s, %s, %s)"
        values_insert_movimiento = (id_bodega_origen, id_bodega_destino, id_empleado, id_producto)
        cursor.execute(query_insert_movimiento, values_insert_movimiento)
        db.commit()
        print("Documento de movimiento generado exitosamente.")
    except mysql.connector.Error as error:
        print("Error al mover los productos o generar el documento de movimiento:", error)
    finally:
        cursor.close()

def generar_documento_movimiento():
    try:
        cursor = db.cursor()
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
    finally:
        cursor.close()


def mostrar_menu():
    while True:
        print("--- MOVIMIENTO DE PRODUCTOS ---")
        print("1. Mover productos entre bodegas")
        print("2. Generar documento de movimiento")
        print("3. Salir")

        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            mover_productos()
        elif opcion == "2":
            generar_documento_movimiento()
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Intente nuevamente.")



