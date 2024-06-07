from flask import Flask, request, jsonify, render_template
import data_provider
import naive_bayes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/post', methods=['POST'])
def handle_post():
    data = request.get_json()
    dataset = data_provider.get_dataset()
    dataset = data_provider.seperate_based_on_class(dataset, "class")
    result = naive_bayes.do_naive_bayes(dataset, data)
    return jsonify(result)

@app.route("/", methods=["GET"])
def handle_get():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, port=8000)
