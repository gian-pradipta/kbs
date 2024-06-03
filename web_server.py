from flask import Flask, request, jsonify, render_template
import main
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/post', methods=['POST'])
def handle_post():
    data = request.get_json()
    dataset = main.get_dataset()
    dataset = main.seperate_based_on_class(dataset, "class")
    result = main.do_naive_bayes(dataset, data)
    return jsonify(result)

@app.route("/", methods=["GET"])
def handle_get():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, port=8000)
