# Generador de CV Profesional con Flask + Vite + Tailwind

## Estructura del Proyecto

```
.
├── app.py
├── requirements.txt
├── templates/
│   └── form.html
├── static/
│   └── dist/         # Aquí Vite compilará los assets finales
├── frontend/         # Carpeta para el frontend con Vite
│   ├── index.html
│   ├── main.js
│   └── style.css
└── ...
```

## Instalación y uso

### 1. Instala dependencias de Python
```bash
pip install -r requirements.txt
```

### 2. Instala dependencias de Node/Vite/Tailwind
```bash
cd frontend
npm install
npm run build
cd ..
```

### 3. Ejecuta Flask
```bash
python app.py
```

### 4. Accede a la app
Abre [http://localhost:5000](http://localhost:5000)

---

## Notas
- Los archivos estáticos generados por Vite (CSS/JS) se sirven desde `static/dist/`.
- Puedes modificar el diseño en `frontend/style.css` y `frontend/index.html` y luego volver a correr `npm run build`. 