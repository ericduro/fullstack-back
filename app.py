from flask import Flask, request, redirect
import persistencia

app = Flask(__name__)


@app.route("/pizza", methods=['POST'])
def pizza():
    nombre = request.form.get("nombre")
    apellidos = request.form.get("apellidos")
    print ("Nombre: "+nombre+"\nApellidos: "+apellidos)
    persistencia.guardar_pedido(nombre, apellidos)
    return redirect("http://localhost/M1_U1_ActividadFinal_EricDuroBasilio/solicita_pedido.html", code=302)