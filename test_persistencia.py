from persistencia import guardar_pedido

def fn_clear_limpiar_fichero():
    
    with open("pedidos.txt", "w", encoding="utf-8") as file:
        file.write("")
        file.close()
    return True


def fn_salvar_persistencia(diccionario):
    if fn_clear_limpiar_fichero():
        print(f"Documento pedidos.txt limpiado!")
    
    for item in diccionario:
        print(f"El nombre es: {item['nombre']} y el apellido es {item['apellidos']}")
        guardar_pedido(str(item['nombre']),str(item['apellidos']))


#pedidos = [{"nombre": "Pedro", "apellidos": "Gil de Diego"},{"nombre": "Michael", "apellidos": "Jordan"},{"nombre": "Fabian", "apellidos": "Herrera"}]

#fn_salvar_persistencia(pedidos)

