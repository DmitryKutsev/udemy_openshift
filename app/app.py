from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello worldddd"



# app.run()
if __name__ == "__main__":
    app.run(port=8080)