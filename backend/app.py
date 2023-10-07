from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/api/test', methods=['GET'])
def test_api():
    response = {'message': 'Test successful nice!'}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
