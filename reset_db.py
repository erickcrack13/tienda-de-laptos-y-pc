import sqlite3

def resetear():
    conn = sqlite3.connect('tienda.db')
    cursor = conn.cursor()

    # 1. Borramos la tabla si ya existe para empezar de cero
    cursor.execute("DROP TABLE IF EXISTS productos")

    # 2. Creamos la tabla con los nombres exactos que pide tu JS y Admin
    cursor.execute('''
        CREATE TABLE productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            category TEXT NOT NULL,
            specs TEXT,
            img TEXT
        )
    ''')

    conn.commit()
    conn.close()
    print("✅ Base de datos reseteada y lista para TechStore.")

if __name__ == '__main__':
    resetear()