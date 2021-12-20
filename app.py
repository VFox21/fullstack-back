'''Backend para pedidos pizza fullstack'''
from flask import Flask
from flask import request
from flask import redirect
from flask import Response
from test_persistencia import fn_salvar_persistencia

app = Flask(__name__)

#@app.route("/hello")
@app.route("/pizza",methods=['POST'])

def pizza():
    nombre = str(request.form.get("nombre_cliente"))
    apellido = str(request.form.get("apellido_cliente"))

    print(f"Nombre recibido: {nombre} y apellido: {apellido}")
    diccionario = {"nombre": nombre, "apellidos": apellido}
    pedidos = [diccionario]
    print(f"Pedidos: {pedidos}")

    fn_salvar_persistencia(pedidos)

    #return "<html><body><p>Hello "+ nombre +"!</p></body></html>"
    return redirect("http://localhost/solicita_pedido.html", code=302)

@app.route("/checksize",methods=['POST'])
def checksize():
    """
    Comprueba disponibilidad de un tamaño de pizza.
    """

    size = str(request.form.get("tamanho"))
    respuesta_negativa = "No disponible"
    respuesta_positiva = "Disponible"

    if size == 'S':
        #return redirect("No disponible")
        return Response(respuesta_negativa, 200, {'Access-Control-Allow-Origin': '*'})
    else:
        return Response(respuesta_positiva, 200, {'Access-Control-Allow-Origin': '*'})
        #return redirect("Disponible")