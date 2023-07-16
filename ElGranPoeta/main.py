import mysql.connector

# Establecer los detalles de conexión
config = {
  'user': 'root',
  'password': '',
  'host': 'localhost',
  'database': 'elgranpoeta',
  'raise_on_warnings': True
}


def login(user, password):
    print("Estas Ingresando como ",user)
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cargo WHERE nombre_cargo = %s AND contrasenia= %s", (user,password))
    resultado = cursor.fetchone()[0]
    if resultado > 0:
        print("Contraseña ingresada correctamente")
        cursor.close()
        conn.close()
        return True
    else:
        return False
        
    
def passChange(usuario, newpass):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("UPDATE cargo SET contrasenia = %s WHERE nombre_cargo = %s", (newpass,usuario))
        conn.commit()
    except mysql.connector.Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()



