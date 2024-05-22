from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/compile', methods=['POST'])
def compile_code():
    data = request.get_json()
    code = data['code']
    
    # Aquí deberías llamar a tu compilador para compilar el código
    # y devolver el resultado de la compilación (por ejemplo, mensajes de error)
    
    result = f"Código recibido para compilación:\n{code}"
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(debug=True)
