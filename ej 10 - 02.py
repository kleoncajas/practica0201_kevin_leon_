cesta = input("Introduce los productos de la cesta de tu compra separados por comas  ")
productos = cesta.split(",")
productos1 = "\n".join(productos)
print(productos1)