from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "¡Proyecto Capstone Groupon!"

@app.route("/otro")
def otros():
    return "Test"

if __name__ == "__main__":
    app.run()