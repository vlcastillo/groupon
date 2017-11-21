from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "¡Proyecto Capstone Groupon!"

if __name__ == "__main__":
    app.run()