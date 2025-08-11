import mysql.connector

# Conectar a la base de datos
conexion = mysql.connector.connect(user='root', password='Pudu37pelado#',
                              host='127.0.0.1',
                              port="3306"
                              database='oc_drevo')
print(conexion)



# Crear un cursor
cursor = conexion.cursor()

# Ejecutar una consulta
cursor.execute("SELECT * FROM MATERIALES")

# Obtener resultados
resultados = cursor.fetchall()

# Mostrar resultados
for fila in resultados:
    print(fila)

# Cerrar conexión
cursor.close()
conexion.close()
