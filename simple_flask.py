from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_route():
    return "Hello World"

def start():
    app.run(debug=False, host='0.0.0.0', port=5020)

