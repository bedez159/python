import pyodbc

db_file = r'C:\Users\angel.blajim\OneDrive - Educacyl\Documentos\Database1.accdb'

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    f'DBQ={db_file};'
)

# conexión a la B.D.
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
def menu():
    print("")
#pedimos el nombre de la ciudad
respuesta = input("Dame una letra: ").upper()

# hacemos las diferentes consultas en SQL
match respuesta:
    case "A":
        print("Has eleegido por ID")
        ID_usuario=int(input("Dame un ID: "))
        cursor.execute("SELECT * FROM clientes WHERE Nombre = ?", (ID_usuario,))

    case "B":
        print("Has eleegido por nombre")
        nombre_usuario=input("Dame un nombre: ")
        cursor.execute(f"SELECT * FROM clientes WHERE Nombre = '{nombre_usuario}'")
    case "C":
        print("Has eleegido por Apellido")
        Apellido=input("Dame un Apellido: ")
        cursor.execute(f"SELECT * FROM clientes WHERE Apellido = '{Apellido}'")
    case "D":
        print("Has eleegido por edad")
        Edad=int(input("Dame un Edad: "))
        cursor.execute("SELECT * FROM clientes WHERE Nombre = ?", (Edad,))
    case "E":
        print("Has eleegido por Email")
        email=input("Dame un Email: ")
        cursor.execute(f"SELECT * FROM clientes WHERE Email = '{email}'")
    case "F":
        print("Has eleegido por Ciudad")
        ciudad_usuario=input("Dame un Ciudad: ")
        cursor.execute(f"SELECT * FROM clientes WHERE Ciudad = '{ciudad_usuario}'")
        


for row in cursor.fetchall():
    print(row)

# cerrar el cursor y la conexión
cursor.close()
conn.close()
