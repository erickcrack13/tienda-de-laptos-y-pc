import sqlite3

def poblar():
    # Lista de productos profesionales
    productos = [
        ('MacBook Pro M3', 1599.00, 'Laptops', '14", Chip M3 Pro, 18GB RAM, 512GB SSD', 'https://images.unsplash.com/photo-1517336714467-59b521c353c1?auto=format&fit=crop&q=80&w=800'),
        ('Monitor Gaming OLED', 899.99, 'Componentes', '34" Curvo, 240Hz, 0.03ms, HDR10', 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?auto=format&fit=crop&q=80&w=800'),
        ('Teclado Custom RGB', 120.50, 'Accesorios', 'Mecánico, Switches Brown, Inalámbrico', 'https://images.unsplash.com/photo-1511467687858-23d96c32e4ae?auto=format&fit=crop&q=80&w=800'),
        ('RTX 4090 OC', 1999.00, 'Componentes', '24GB GDDR6X, Ray Tracing Gen 3', 'https://images.unsplash.com/photo-1591488320449-011701bb6704?auto=format&fit=crop&q=80&w=800'),
        ('Auriculares Hi-Fi', 250.00, 'Accesorios', 'Cancelación de ruido, Audio 3D espacial', 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&q=80&w=800')
    ]

    try:
        conn = sqlite3.connect('tienda.db')
        cursor = conn.cursor()
        
        # Limpiar tabla anterior
        cursor.execute("DELETE FROM productos")
        
        # Insertar los nuevos
        cursor.executemany(
            "INSERT INTO productos (name, price, category, specs, img) VALUES (?,?,?,?,?)", 
            productos
        )
        
        conn.commit()
        conn.close()
        print("✅ Base de datos actualizada con 5 productos estrella.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    poblar()