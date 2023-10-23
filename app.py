from flask import Flask, request, jsonify
import math

app = Flask(__name__)

@app.route('/', methods=['GET'])
def health():
    try:
        response = {
            'message': 'server sehat'
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/kuadrat', methods=['POST'])
def kuadrat():
    try:
        data = request.get_json()
        bilangan = data['bilangan']
        hasil_kuadrat = math.sqrt(bilangan)
        response = {
            'input': bilangan,
            'hasil_kuadrat': hasil_kuadrat
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
