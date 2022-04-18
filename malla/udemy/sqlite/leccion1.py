import sqlite3

conexion = sqlite3.connect("./ejemplo.db")

cursor = conexion.cursor()

# cursor.execute("CREATE TABLE usuarios(nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")
# cursor.execute("INSERT INTO usuarios(nombre, edad, email) values('Miguel', 22, 'miguelh1299@gmail.com')")
# cursor.execute("DELETE FROM usuarios WHERE nombre='Miguel'")
# cursor.execute("SELECT * FROM usuarios")
# usuario = cursor.fetchall()
# print(usuario)

# usuarios = [
#     ('Luisa',51, 'luisa@gmail.com'),
#     ('mercedes', 38, 'mercedes@gmail.com'),
#     ('juan', 18, 'juan@gmail.com')
# ]

# cursor.executemany("INSERT INTO usuarios VALUES(?, ?, ?)",usuarios)


conexion.commit()
conexion.close()