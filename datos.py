from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
# Configuración de CORS para permitir conexiones desde tu frontend local
CORS(app)

def conectar_db():
    conn = sqlite3.connect('tienda.db')
    conn.row_factory = sqlite3.Row
    return conn

# Inicialización de la base de datos
with conectar_db() as conn:
    conn.execute('''CREATE TABLE IF NOT EXISTS productos 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                     name TEXT, 
                     price REAL, 
                     category TEXT, 
                     specs TEXT, 
                     img TEXT)''')

@app.route('/api/productos', methods=['GET'])
def obtener_productos():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = [dict(ix) for ix in cursor.fetchall()]
    conn.close()
    return jsonify(productos)

@app.route('/api/productos', methods=['POST'])
def agregar_producto():
    d = request.json
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos (name, price, category, specs, img) VALUES (?,?,?,?,?)",
                   (d['name'], d['price'], d['category'], d['specs'], d['img']))
    conn.commit()
    conn.close()
    return jsonify({"mensaje": "¡Guardado!"}), 201

# --- NUEVA RUTA PARA ELIMINAR ---
@app.route('/api/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    try:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        return jsonify({"mensaje": "Producto eliminado con éxito"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)