import sqlite3

def llenar_tienda():
    productos = [
        ('Laptop Pro X14', 1299.99, 'Laptops', 'M3 Chip, 16GB RAM, 512GB SSD', 'https://images.unsplash.com/photo-1517336714467-59b521c353c1?q=80&w=800&auto=format&fit=crop'),
        ('Teclado Mecánico RGB', 85.50, 'Accesorios', 'Switches Blue, Retroiluminación, USB-C', 'https://images.unsplash.com/photo-1511467687858-23d96c32e4ae?q=80&w=800&auto=format&fit=crop'),
        ('Monitor 4K UltraWide', 450.00, 'Componentes', '34 pulgadas, 144Hz, IPS Panel', 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?q=80&w=800&auto=format&fit=crop'),
        ('Mouse Gamer Pro', 59.99, 'Accesorios', '25000 DPI, Inalámbrico, 80h batería', 'https://images.unsplash.com/photo-1527814732934-76a16aa87ed5?q=80&w=800&auto=format&fit=crop'),
        ('Tarjeta Gráfica RTX 4080', 1100.00, 'Componentes', '16GB GDDR6X, Ray Tracing, Triple Fan', 'https://images.unsplash.com/photo-1591488320449-011701bb6704?q=80&w=800&auto=format&fit=crop')
    ]

    conn = sqlite3.connect('tienda.db')
    cursor = conn.cursor()
    
    # Limpiamos la tabla para que no se repitan
    cursor.execute("DELETE FROM productos")
    
    # Insertamos los 5 productos
    cursor.executemany("INSERT INTO productos (name, price, category, specs, img) VALUES (?,?,?,?,?)", productos)
    
    conn.commit()
    conn.close()
    print("✅ ¡Base de datos llena con 5 productos estrella!")

if __name__ == "__main__":
    llenar_tienda()