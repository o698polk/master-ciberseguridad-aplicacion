from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    # Cambiado para que sea un diccionario válido
    return jsonify({"mensaje": "¡Bienvenido a mi microservicio!"})

@app.route('/api/sumar', methods=['POST'])
def sumar():
    # Obtener los números del cuerpo de la solicitud
    datos = request.get_json()
    numero1 = datos.get('numero1')
    numero2 = datos.get('numero2')

    # Validar que los números sean proporcionados
    if numero1 is None or numero2 is None:
        return jsonify({"error": "Faltan parámetros 'numero1' o 'numero2'"}), 400

    # Calcular la suma
    try:
        resultado = float(numero1) + float(numero2)
    except ValueError:
        return jsonify({"error": "Los parámetros deben ser números válidos"}), 400

    # Devolver el resultado como JSON
    return jsonify({"resultado": resultado})

@app.route('/api/info', methods=['GET'])
def info():
    # Devolver información adicional sobre el microservicio
    return jsonify({
        "nombre": "Microservicio de Suma",
        "version": "1.0",
        "descripcion": "Un microservicio simple para sumar dos números."
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

