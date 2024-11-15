import sqlite3 

def creartabla():
    conexion = sqlite3.connect('ejmplo_base.db')
    sql = conexion.cursor()

    sql.execute(''' 
        CREATE TABLE IF NOT EXISTS empresas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(50) NOT NULL
        )
    ''')
    #Cuando se quiere crear un valor incrementable tiene que tener el valor INTEGER

    conexion.commit()
    conexion.close()

def ingresoDatos():
    conexion = sqlite3.connect('ejmplo_base.db')
    sql = conexion.cursor()

    sql.execute(''' 
        INSERT INTO empresas(nombre)
        VALUES(?)
    ''',('Gelanova',))
    #depues de las comillas va una coma y se crea una tupla para pasar los datos a la base de datos
    conexion.commit()
    conexion.close()


def verDatos():
    conexion = sqlite3.connect('ejmplo_base.db')
    sql = conexion.cursor()

    sql.execute('SELECT * FROM empresas')

    #fechall sirve para devolver las filas de sql, pero el resultado lo devuelte en una tupla 
    #por lo cual genera multiples tuplas
    datos = sql.fetchall()
    for fila in datos:
        print(fila)
    conexion.close()

#creartabla()
#ingresoDatos()
verDatos()