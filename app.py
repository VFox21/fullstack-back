'''Backend para pedidos pizza fullstack'''
from flask import Flask
from flask import request
from flask import redirect
from flask import Response
from test_persistencia import test_guardar_pedido

app = Flask(__name__)

#@app.route("/hello")
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

    #test_guardar_pedido(pedidos)

    #return "<html><body><p>Hello "+ nombre +"!</p></body></html>"
    return redirect("http://localhost/solicita_pedido.html", code=302)

@app.route("/checksize",methods=['POST'])
def checksize():
    """
    Comprueba disponibilidad de un tamaño de pizza.
    """

    size = str(request.form.get("tamanho"))
    respuesta_positiva = "Disponible"

    if size == 'S':
         respuesta_negativa = "No disponible"       

    return Response(respuesta_negativa, 200, {'Access-Control-Allow-Origin': '*'})
        #return redirect("Disponible")
