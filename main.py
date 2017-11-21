from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "¡Proyecto Capstone Groupon!"

@app.route("/otro")
def otros():
    with open('test.txt', 'r') as archivo:
        for linea in archivo:
            string= linea
            
    return string

if __name__ == "__main__":
    app.run()