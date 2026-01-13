import sqlite3

def preparar():
    conn = sqlite3.connect('tienda.db')
    cursor = conn.cursor()

    # Borrar y crear tabla
    cursor.execute("DROP TABLE IF EXISTS productos")
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

    # INSERTAR PRODUCTOS DE PRUEBA (Imágenes profesionales)
    productos_iniciales = [
        ('Asus ROG Zephyrus', 1450.00, 'Laptops', 'RTX 4060 | 16GB RAM | 1TB SSD', 'https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=600'),
        ('Teclado Mecánico RGB', 85.50, 'Accesorios', 'Switches Blue | Keycaps PBT', 'https://images.unsplash.com/photo-1511467687858-23d96c32e4ae?w=600'),
        ('Monitor Gamer 144Hz', 299.99, 'Componentes', '27" IPS | 1ms | QHD', 'https://images.unsplash.com/photo-1527443154391-507e9dc6c5cc?w=600'),
        ('Mouse Pro Wireless', 120.00, 'Accesorios', '25K DPI | Ultraligero', 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=600')
    ]

    cursor.executemany('''
        INSERT INTO productos (name, price, category, specs, img) 
        VALUES (?, ?, ?, ?, ?)
    ''', productos_iniciales)

    conn.commit()
    conn.close()
    print("✅ Base de datos lista con productos e imágenes profesionales.")

if __name__ == '__main__':
    preparar()