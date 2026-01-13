const API_URL = 'http://127.0.0.1:5000/api/productos';
let todosLosProductos = [];
let carrito = JSON.parse(localStorage.getItem('tech_cart')) || [];

async function cargarProductos() {
    try {
        const res = await fetch(API_URL);
        todosLosProductos = await res.json();
        renderizarProductos(todosLosProductos);
        actualizarUI();
    } catch (e) {
        console.error("Error cargando productos:", e);
    }
}

function renderizarProductos(lista) {
    const grid = document.getElementById('products-grid');
    if (!grid) return;

    // Si la lista está vacía, mostrará este mensaje
    if (lista.length === 0) {
        grid.innerHTML = '<p>No hay productos disponibles en este momento.</p>';
        return;
    }

    // Esto "escribe" el HTML de cada producto dinámicamente
    grid.innerHTML = lista.map(p => `
        <div class="card">
            <img src="${p.img}" alt="${p.name}">
            <div class="card-info">
                <span class="category-tag">${p.category}</span>
                <h3>${p.name}</h3>
                <p class="price">$${p.price}</p>
                <button class="buy-btn" onclick="agregarAlCarrito(${p.id})">Agregar</button>
            </div>
        </div>
    `).join('');
}

function filtrarCategoria(cat) {
    const botones = document.querySelectorAll('.chip');
    botones.forEach(b => b.classList.toggle('active', b.innerText === cat));
    
    const filtrados = cat === 'Todos' ? todosLosProductos : todosLosProductos.filter(p => p.category === cat);
    renderizarProductos(filtrados);
}

function ejecutarBusqueda() {
    const term = document.getElementById('mainSearch').value.toLowerCase();
    const filtrados = todosLosProductos.filter(p => p.name.toLowerCase().includes(term));
    renderizarProductos(filtrados);
}

function agregarAlCarrito(id) {
    const prod = todosLosProductos.find(p => p.id === id);
    carrito.push(prod);
    actualizarUI();
}

function vaciarCarrito() {
    carrito = [];
    actualizarUI();
}

function actualizarUI() {
    localStorage.setItem('tech_cart', JSON.stringify(carrito));
    document.getElementById('cartCount').innerText = carrito.length;
    
    const itemsCont = document.getElementById('cartItems');
    if (itemsCont) {
        itemsCont.innerHTML = carrito.map(i => `<div style="display:flex; justify-content:space-between; margin-bottom:10px;">
            <span>${i.name}</span> <b>$${i.price}</b>
        </div>`).join('');
    }
}

function abrirCarrito() { document.getElementById('cartModal').style.display = 'block'; }
function cerrarCarrito() { document.getElementById('cartModal').style.display = 'none'; }

function irAWhatsApp() {
    let msg = "Hola TechStore, quiero: " + carrito.map(i => i.name).join(", ");
    window.open(`https://wa.me/123456789?text=${encodeURIComponent(msg)}`);
}

window.onload = cargarProductos;