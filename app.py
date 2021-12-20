'''Backend para pedidos pizza fullstack'''
from flask import Flask
from flask import request
from flask import redirect
from flask import Response

app = Flask(__name__)

@app.route("/pizza",methods=['POST'])

def pizza():
    """
    Redireccionamiento para pizza.
    """
    nombre = str(request.form.get("nombre_cliente"))
    apellido = str(request.form.get("apellido_cliente"))

    print(f"Nombre recibido: {nombre} y apellido: {apellido}")
    diccionario = {"nombre": nombre, "apellidos": apellido}
    pedidos = [diccionario]
    print(f"Pedidos: {pedidos}")

    return redirect("http://localhost/solicita_pedido.html", code=302)

@app.route("/checksize",methods=['POST'])
def checksize():
    """
    Comprueba disponibilidad de un tamaño de pizza.
    """

    size = str(request.form.get("tamanho"))
    respuesta = "Disponible"

    if size == 'S':
        respuesta = "No disponible"

    return Response(respuesta, 200, {'Access-Control-Allow-Origin': '*'})
