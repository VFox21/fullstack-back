from flask import Flask
from flask import request
from flask import redirect
#from test_persistencia import fn_salvar_persistencia

app = Flask(__name__)

#@app.route("/hello")
@app.route("/pizza",methods=['POST'])

def pizza():
    '''Se implementa el listener para el contaxto pizza.'''

    nombre = str(request.form.get("nombre_cliente"))
    apellido = str(request.form.get("apellido_cliente"))

    print(f"Nombre recibido: {nombre} y apellido: {apellido}")
    diccionario = {"nombre": nombre, "apellidos": apellido}
    pedidos = [diccionario]
    print(f"Pedidos: {pedidos}")

    #fn_salvar_persistencia(pedidos)

    #return "<html><body><p>Hello "+ nombre +"!</p></body></html>"
    return redirect("http://localhost/solicita_pedido.html", code=302)
