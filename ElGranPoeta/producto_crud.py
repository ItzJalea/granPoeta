import mysql.connector

# Conexión a la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="elgranpoeta"
)
config = {
  'user': 'root',
  'password': '',
  'host': 'localhost',
  'database': 'elgranpoeta',
  'raise_on_warnings': True
}
# Crear un cursor para ejecutar consultas
cursor = db.cursor()


# Función para crear un producto
def crear_producto():
    autor = input("Autor: ")
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    mostrar_categorias()
    id_categoria = int(input("Ingrese el número de la categoría: "))
    id_editorial = int(input("ID de editorial: "))

    try:
        # Insertar el nuevo producto en la base de datos
        query = "INSERT INTO producto (autor, nombre, descripcion, id_categoria, id_editorial) VALUES (%s, %s, %s, %s, %s)"
        values = (autor, nombre, descripcion, id_categoria, id_editorial)
        cursor.execute(query, values)
        db.commit()
        print("Producto creado exitosamente.")
    except mysql.connector.Error as error:
        print("Error al crear el producto:", error)
    finally:
        cursor.close()
        db.close()
        

# Función para leer productos
def leer_productos():
    try:
        # Obtener todos los productos de la base de datos
        query = "SELECT p.id_producto, p.autor, p.nombre, p.descripcion, c.nombre_categoria, e.nombre_editorial FROM producto p JOIN categoria c ON p.id_categoria = c.id_categoria JOIN editorial e ON p.id_editorial = e.id_editorial"
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute(query)
        productos = cursor.fetchall()
        print("--- PRODUCTOS ---")
        for producto in productos:
            print("ID:", producto[0])
            print("Autor:", producto[1])
            print("Nombre:", producto[2])
            print("Descripción:", producto[3])
            print("Categoría:", producto[4])
            print("Editorial:", producto[5])
            print("-----------------")
        cursor.close()
    except mysql.connector.Error as error:
        print("Error al leer los productos:", error)
        cursor.close()
        conn.close()
    finally:
        conn.close()

        

# Función para filtrar productos por editorial
def filtrar_por_editorial():
    id_editorial = int(input("ID de la editorial a filtrar: "))

    try:
        # Obtener los productos con la misma editorial
        query = "SELECT p.id_producto, p.autor, p.nombre, p.descripcion, c.nombre_categoria, e.nombre_editorial FROM producto p JOIN categoria c ON p.id_categoria = c.id_categoria JOIN editorial e ON p.id_editorial = e.id_editorial WHERE e.id_editorial = %s"
        values = (id_editorial,)
        cursor.execute(query, values)
        productos = cursor.fetchall()

        if len(productos) > 0:
            print(f"=== PRODUCTOS DE LA EDITORIAL {id_editorial} ===")
            for producto in productos:
                print("ID:", producto[0])
                print("Autor:", producto[1])
                print("Nombre:", producto[2])
                print("Descripción:", producto[3])
                print("Categoría:", producto[4])
                print("Editorial:", producto[5])
                print("-----------------")
        else:
            print(f"No hay productos de la editorial {id_editorial}.")
    except mysql.connector.Error as error:
        print("Error al filtrar los productos por editorial:", error)
    finally:
        cursor.close()
        db.close()

# Función para filtrar productos por categoría
def filtrar_por_categoria():
    id_categoria = int(input("ID de la categoría a filtrar: "))

    try:
        # Obtener los productos de la misma categoría
        query = "SELECT p.id_producto, p.autor, p.nombre, p.descripcion, c.nombre_categoria, e.nombre_editorial FROM producto p JOIN categoria c ON p.id_categoria = c.id_categoria JOIN editorial e ON p.id_editorial = e.id_editorial WHERE c.id_categoria = %s"
        values = (id_categoria,)
        cursor.execute(query, values)
        productos = cursor.fetchall()

        if len(productos) > 0:
            print(f"=== PRODUCTOS DE LA CATEGORÍA {id_categoria} ===")
            for producto in productos:
                print("ID:", producto[0])
                print("Autor:", producto[1])
                print("Nombre:", producto[2])
                print("Descripción:", producto[3])
                print("Categoría:", producto[4])
                print("Editorial:", producto[5])
                print("-----------------")
        else:
            print(f"No hay productos de la categoría {id_categoria}.")
    except mysql.connector.Error as error:
        print("Error al filtrar los productos por categoría:", error)
    finally:
        cursor.close()
        db.close()

# Función para actualizar un producto
def actualizar_producto():
    id_producto = int(input("ID del producto a actualizar: "))
    autor = input("Autor: ")
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    mostrar_categorias()
    id_categoria = int(input("Ingrese el número de la categoría: "))
    id_editorial = int(input("ID de editorial: "))

    try:
        # Actualizar el producto en la base de datos
        query = "UPDATE producto SET autor = %s, nombre = %s, descripcion = %s, id_categoria = %s, id_editorial = %s WHERE id_producto = %s"
        values = (autor, nombre, descripcion, id_categoria, id_editorial, id_producto)
        cursor.execute(query, values)
        db.commit()
        print("Producto actualizado exitosamente.")
    except mysql.connector.Error as error:
        print("Error al actualizar el producto:", error)
    finally:
        cursor.close()
        db.close()

# Función para eliminar un producto
def eliminar_producto():
    id_producto = int(input("ID del producto a eliminar: "))

    try:
        # Verificar si el producto está en uso
        query = "SELECT * FROM producto WHERE id_producto = %s"
        values = (id_producto,)
        cursor.execute(query, values)
        producto = cursor.fetchone()

        if producto is None:
            print("El producto no existe.")
            return

        # Eliminar el producto de la base de datos
        query = "DELETE FROM producto WHERE id_producto = %s"
        cursor.execute(query, values)
        db.commit()
        print("Producto eliminado exitosamente.")
    except mysql.connector.Error as error:
        print("Error al eliminar el producto:", error)
    finally:
        cursor.close()
        db.close()

# Función para mostrar las categorías disponibles
def mostrar_categorias():
    try:
        # Obtener las categorías de la base de datos
        query = "SELECT * FROM categoria"
        cursor.execute(query)
        categorias = cursor.fetchall()

        if len(categorias) > 0:
            print("Categorías disponibles:")
            for categoria in categorias:
                print(f"{categoria[0]}. {categoria[1]}")
        else:
            print("No hay categorías en la base de datos.")
    except mysql.connector.Error as error:
        print("Error al obtener las categorías:", error)
    finally:
        cursor.close()
        db.close()

def mostrar_menu():
    while True:
        print("--- Producto ---")
        print("1. Crear producto")
        print("2. Leer productos")
        print("3. Filtrar productos por editorial")
        print("4. Filtrar productos por categoría")
        print("5. Actualizar producto")
        print("6. Eliminar producto")
        print("7. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            crear_producto()
        elif opcion == "2":
            leer_productos()
        elif opcion == "3":
            filtrar_por_editorial()
        elif opcion == "4":
            filtrar_por_categoria()
        elif opcion == "5":
            actualizar_producto()
        elif opcion == "6":
            eliminar_producto()
        elif opcion == "7":
            break
        else:
            print("Opción inválida. Intente nuevamente.")
