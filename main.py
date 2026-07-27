from flask import Flask, render_template, jsonify
import random

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
    return render_template("index.html", lights="/lights")

@app.route("/lights/<opcion>")
def lights(opcion):
    instrucciones = {
        "3": "Reciclaje básico: retira las pilas, guárdalas en un frasco cerrado y lleva los aparatos pequeños a un punto de acopio en supermercados o universidades.",
        "5": "Reciclaje básico: retira las pilas, guárdalas en un frasco cerrado y lleva los aparatos pequeños a un punto de acopio en supermercados o universidades.",
        "6": "Reciclaje intermedio: usa una caja resistente, etiqueta como 'Residuos electrónicos con pilas', cubre los polos con cinta y entrégala en centros especializados.",
        "8": "Reciclaje intermedio: usa una caja resistente, etiqueta como 'Residuos electrónicos con pilas', cubre los polos con cinta y entrégala en centros especializados.",
        "10": "Reciclaje avanzado: organiza una entrega comunitaria, contacta programas ecológicos locales y entrega los aparatos en campañas de reciclaje masivo.",
        "12": "Reciclaje avanzado: organiza una entrega comunitaria, contacta programas ecológicos locales y entrega los aparatos en campañas de reciclaje masivo."
    }
    instruccion = instrucciones.get(opcion, "Opción no válida. Por favor selecciona un número de electrodomésticos válido.")
    return render_template("lights.html", opcion=opcion, instruccion=instruccion)

@app.route("/random_fact")
def dato_aleatorio():
    seleccion = random.choice(datos)
    return render_template("random_fact.html", seleccion=seleccion)

@app.route("/api/dato_aleatorio")
def api_dato_aleatorio():
    seleccion = random.choice(datos)
    colores = ["#5988ff", "#fd98fb", "#d6ff6b", "#ff6b6b", "#6bffd6"]
    color = random.choice(colores)
    return jsonify(dato=seleccion, color=color)

@app.route("/secreto")
def pagina_secreta():
    adivinanza = random.choice(adivinanzas)
    return render_template("secreto.html", adivinanza=adivinanza)

if __name__ == "__main__":
    app.run(debug=True)
