producto = input("Introduce el nombre del producto  ")
precio = float(input("¿Cuál es el precio del producto?  "))
unidad = int(input("¿Cuál es el número de productos?  "))
coste = precio * unidad
print("El nombre del producto es",producto,", su precio es {:06.2f}, el número de unidades es {:03} y su coste es {:08.2f}".format(precio,unidad,coste))
#Escribo en los corchetes el ":06", ":03" y el ":08" para la parte de los dígitos enteros ya que aparecía de esta manera el comando en internet con el 0 por delante 
#El "." es para separar la parte entera de la parte decimal y después del "." ya es la parte decimal con 2 dígitos, y la "f" es para formatear números reales
#Como pone en los apuntes