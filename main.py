from flask import Flask, render_template
import random

# Configuración: Busca las plantillas en la carpeta 'template' (singular)
app = Flask(__name__, template_folder='template')

datos = [
    "el promedio de uso de celulares es de 4 horas diarias",
    "el primer celular pesaba 1 kilo",
    "la pantalla azul afecta tu sueño",
    "el 90% revisa el celular al despertar",
    "la tecnología puede causar ansiedad"
]

adivinanzas = [
    {"p": "tengo agujas pero no sé coser, tengo números pero no sé leer", "r": "un reloj", "c": "#5988ff"},
    {"p": "cuanto más le quitas, más grande se hace", "r": "un agujero", "c": "#fd98fb"},
    {"p": "salty pero no salado, duro pero no piedra", "r": "una roca de sal", "c": "#d6ff6b"}
]

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/random_fact")
def dato_aleatorio():
    seleccion = random.choice(datos)
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>dato aleatorio</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    </head>
    <body>
        <div class="menu">
            <a href="/">inicio</a>
            <a href="/random_fact">dato aleatorio</a>
            <a href="/secreto">secreto</a>
        </div>
        <h1>dato del día</h1>
        <div class="caja">
            <p>{seleccion}</p>
        </div>
        <br>
        <a href="/" class="btn-volver">volver al inicio</a>
    </body>
    </html>
    """

@app.route("/api/dato_aleatorio")
def api_dato_aleatorio():
    import json
    seleccion = random.choice(datos)
    colores = ["#5988ff", "#fd98fb", "#d6ff6b", "#ff6b6b", "#6bffd6"]
    color = random.choice(colores)
    return json.dumps({"dato": seleccion, "color": color})

@app.route("/secreto")
def pagina_secreta():
    adivinanza = random.choice(adivinanzas)
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>secreto</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
        <style>
            .caja-secreta {{
                background: #f9f9f9;
                border: 3px dashed {adivinanza['c']};
                padding: 30px;
                border-radius: 15px;
                max-width: 400px;
                margin: 30px auto;
                text-align: center;
            }}
            .btn-volver {{
                background: #5988ff;
                color: white;
                padding: 10px 20px;
                text-decoration: none;
                border-radius: 8px;
                display: inline-block;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="menu">
            <a href="/">inicio</a>
            <a href="/random_fact">dato aleatorio</a>
            <a href="/secreto">secreto</a>
        </div>
        <h1>zona secreta</h1>
        <div class="caja-secreta">
            <h2 style="color: {adivinanza['c']}">adivinanza</h2>
            <p>{adivinanza['p']}</p>
            <p>respuesta: <strong>{adivinanza['r']}</strong></p>
        </div>
        <br>
        <a href="/" class="btn-volver">volver al inicio</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
