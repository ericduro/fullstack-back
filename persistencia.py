""" Archivo para la función para guardar pedidos con el guión delante """
def guardar_pedido(nombre, apellidos):
    """ Función para guardar los pedidos recibiendo nombre y apellidos como argumento """
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write("-" + nombre + " " + apellidos + "\n")
        file.close()
