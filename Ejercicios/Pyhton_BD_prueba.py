import pydobc

db_file = r'C:\Users\angel.blajim\OneDrive - Educacyl\Documentos\Database1'
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb.*.accdb)};'
    f'DBQ={db_file};'
)

#conexion a la B.D.
conn = pydobc.connect(conn_str)
cursor = conn.cursor()

#hacemos la consulta en SQL
cursor.execute("SELECT * FROM clientes")
for row in cursor.fetchall():
    print(row)

#cerrar el cursor y la conexion
cursor.close()
conn.close()