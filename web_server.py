from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def handle_post():
    data = request.get_json()
    response_data = {"message": "Data received", "received_data": data}
    return jsonify(response_data)

@app.route("/get", methods=["GET"])
def handle_get():
    return jsonify

if __name__ == '__main__':
    app.run(debug=True, port=8000)
