def guardar_pedido(par_nombre,par_apellido):
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write(par_nombre + " " + par_apellido + "\n")
        file.close()
    return True


#nombre="Fabian"
#apellido="Herrera"

#if guardar_pedido(nombre,apellido):
#    print("Nombre y apellido guardado!")