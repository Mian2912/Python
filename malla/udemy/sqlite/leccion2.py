import sqlite3

conexion = sqlite3.connect("./usuarios.db")
cursor = conexion.cursor()

# cursor.execute('''
#     CREATE TABLE usuario(
#         dni INTEGER PRIMARY KEY AUTOINCREMENT,
#         nombre VARCHAR(100),
#         edad INTEGER,
#         email VARCHAR(100)
#     )
# ''')

# usuarios = [
#     ('Luisa',51, 'luisa@gmail.com'),
#     ('mercedes', 38, 'mercedes@gmail.com'),
#     ('juan', 18, 'juan@gmail.com')
# ]

# cursor.executemany("INSERT INTO usuario (nombre, edad, email) VALUES(?, ?, ?)", usuarios)

cursor.execute("SELECT * FROM usuario")
usuarios = cursor.fetchall()

for usuairo in usuarios :
    print(usuairo)

conexion.commit()
conexion.close()