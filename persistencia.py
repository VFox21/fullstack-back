'''Guardar_pedido.py para backend'''
def guardar_pedido(par_nombre,par_apellido):
    '''La funcion guardar_pedido implementa la persistencia en un fichero local.'''

    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write(par_nombre + " " + par_apellido + "\n")
        file.close()
    return True
