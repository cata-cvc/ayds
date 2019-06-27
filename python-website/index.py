from flask import Flask,render_template,request, session , abort
from flask_sqlalchemy import SQLAlchemy
import psycopg2

dentro=False

app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:@localhost/prototipo'
db = SQLAlchemy(app)


@app.route("/")
def home():
    return render_template('home.html')



@app.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        correo=request.form['correo']
        contrasena=request.form['contraseña']
        print(correo+" "+contrasena)
        if correo!="" and contrasena!="":
            if correo=="prueba@noingreso.com" and contrasena !="":
                return render_template("home.html")
            else:
                dentro=True
                return render_template("menui.html")
        else:
            return render_template("home.html")

@app.route("/ingresar")
def ingresar():
    dentro=True
    return render_template("ingresar.html")


@app.route("/ingreso", methods=['POST'])
def ingreso():
    dentro=True
    if request.method =='POST':
        cant = request.form['cantidad']
        fech = request.form['fecha']
        prov = request.form['proveedor']
        print(cant+" "+fech+" "+ prov)
        #db.session.add(datos)
        #db.session.commit()
    return render_template("ingresar.html")

@app.route("/retirar")
def retiro():
    dentro=True
    return render_template("retirar.html")

@app.route("/construccion")
def reportes():
    dentro=True
    return render_template("construccion.html")

@app.route("/actualizar-proveedor")
def actprov():
    dentro = True
    return render_template("act-prov.html")

@app.route("/menu")
def menu():
    return render_template("menui.html")


@app.route("/salir")
def salir():
    dentro=False
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)
