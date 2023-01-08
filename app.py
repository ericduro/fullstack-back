""" Archivo para recoger los nombres y apellidos ejecutados en la app y lanzar
la función para guardar esos nombres en un archivo .txt utilizando una función
"""
from flask import Flask, request, redirect, Response
import persistencia

app = Flask(__name__)


@app.route("/pizza", methods=['POST'])
def pizza():
    """ Aplicación para recoger los nombres de los pedidos, guardarlos en un
    .txt mediante un archivo y redirigir al usuario a otra página
    """
    nombre = request.form.get("nombre")
    apellidos = request.form.get("apellidos")
    print ("Nombre: "+nombre+"\nApellidos: "+apellidos)
    persistencia.guardar_pedido(nombre, apellidos)
    return redirect("http://localhost/M1_U1_ActividadFinal_EricDuroBasilio/solicita_pedido.html",
    code=302)

@app.route("/checksize",methods=['POST'])
def checksize():
    """
    Comprueba disponibilidad de un tamaño de pizza.
    """
    size = request.form.get('tamano')
    if size == 'S':
        mensaje = "No disponible"
    else:
        mensaje = "Disponible"
    return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})
