

# ESTO CUMPLE CON EL PUNTO 12 DE "DETALLE DE PROYECTOS"
# LA FUNCION ESTA HECHA --TEXTUAL-- A LO QUE SE SOLICITA.

# 12.	El jefe de bodega podrá generar un informe en donde se indique:
# a.	Cantidad de productos por bodega
# b.	Tipos de productos (revistas, libros o enciclopedias)
# c.	Listar solo los productos de una bodega por una editorial específica.

# INCLUSO SE AGREGO EL CONTADOR DE TIPO DE PRODUCTOS PARA QUE FUESE DE
# UTILIDAD TENER ESA INFORMACION



# EJEMPLO DE COMO SE VE EN CONSOLA

# Cantidad de productos por bodega:
# Bodega:     Temuco
# Cantidad:   2 productos.

# Bodega:     Pucon
# Cantidad:   1 productos.
# --------------------
# Bodega:    Temuco

# Total Libros:           1
# Total Enciclopedias:    1
# Total Revistas:         0

# Bodega:    Pucon

# Total Libros:           1
# Total Enciclopedias:    0
# Total Revistas:         0
# --------------------
# Ingrese el nombre de la bodega: Temuco
# Ingrese el nombre de la editorial: otraprueba 

# Bodega: Temuco      Editorial: otraprueba:

# carrie
# verity




import mysql.connector
midb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="elgranpoeta"
)


def getnombreeditorial():
    try:
        query = "SELECT nombre_editorial FROM editorial"
        cursor = midb.cursor()
        cursor.execute(query)
        editoriales = cursor.fetchall()
        for editorial in editoriales:
            print("Editorial = ",editorial[0])
    except mysql.connector.Error as error:
        print(error)
    finally:
        cursor.close()

def cantidad_productos_por_bodega():
    cursor = midb.cursor()

    try:
        query = "SELECT b.nombre_bodega, COUNT(s.id_stock) FROM bodega b LEFT JOIN stock s ON b.id_bodega = s.id_bodega GROUP BY b.id_bodega"
        cursor.execute(query)
        resultados = cursor.fetchall()

        print("Cantidad de productos por bodega:\n")
        for resultado in resultados:
            nombre_bodega = resultado[0]
            cantidad_productos = resultado[1]
            print(f"Bodega:     {nombre_bodega}\nCantidad:   {cantidad_productos} productos.\n")

    except mysql.connector.Error as error:
        print(error)

    finally:
        cursor.close()


# Tipos de productos (revistas, libros o enciclopedias)
def tipos_de_productos():
    cursor = midb.cursor()
    try:
        query = """
        SELECT b.nombre_bodega,
            COUNT(CASE WHEN p.id_categoria = 1 THEN 1 END) AS total_libros,
            COUNT(CASE WHEN p.id_categoria = 2 THEN 1 END) AS total_enciclopedias,
            COUNT(CASE WHEN p.id_categoria = 3 THEN 1 END) AS total_revistas
        FROM bodega b
        INNER JOIN stock s ON b.id_bodega = s.id_bodega
        INNER JOIN producto p ON s.id_producto = p.id_producto
        GROUP BY b.nombre_bodega
        """
        cursor.execute(query)
        resultados = cursor.fetchall()

        print("Tipos de productos por bodega:")
        for resultado in resultados:
            nombre_bodega = resultado[0]
            total_libros = resultado[1]
            total_enciclopedias = resultado[2]
            total_revistas = resultado[3]
            print(f"Bodega:    {nombre_bodega}\n")
            print(f"Total Libros:           {total_libros}")
            print(f"Total Enciclopedias:    {total_enciclopedias}")
            print(f"Total Revistas:         {total_revistas}")
            print()

    except mysql.connector.Error as error:
        print(error)

    finally:
        cursor.close()


# Listar solo los productos de una bodega por una editorial específica
def productos_por_bodega_y_editorial():
    cursor = midb.cursor()
    try:
        # Obtener la bodega seleccionada por el usuario
        bodega = input("Ingrese el nombre de la bodega: ")

        # Obtener la editorial seleccionada por el usuario
        getnombreeditorial()
        editorial = input("Ingrese el nombre de la editorial: ")

        query = """
        SELECT p.nombre
        FROM producto p
        INNER JOIN stock s ON p.id_producto = s.id_producto
        INNER JOIN bodega b ON s.id_bodega = b.id_bodega
        INNER JOIN editorial e ON p.id_editorial = e.id_editorial
        WHERE b.nombre_bodega = %s AND e.nombre_editorial = %s
        """
        values = (bodega, editorial)
        cursor.execute(query, values)
        resultados = cursor.fetchall()

        print(f"\nBodega: {bodega}      Editorial: {editorial}:\n")
        for resultado in resultados:
            nombre_producto = resultado[0]
            print(nombre_producto)

    except mysql.connector.Error as error:
        print(error)

    finally:
        cursor.close()

def menuBodFiltro():
    cantidad_productos_por_bodega()
    print("--------------------")
    tipos_de_productos()
    print("-------------------")
    productos_por_bodega_y_editorial()
