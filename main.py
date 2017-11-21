from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("pagina.html")

@app.route("/demanda")
def demanda():
    import rpy2.robjects as ro
    from rpy2.robjects.packages import importr
    ro.r('x=c()')
    ro.r('x[1]=22')
    ro.r('x[2]=44')
    return "demanda"

@app.route("/desempeno")
def desempeno():
    return "Predicción desempeño"


if __name__ == "__main__":
    app.run()