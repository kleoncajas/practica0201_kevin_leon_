precio = input("¿Cuál es el precio del producto en euros con dos decimales?  ")
dinero = precio.split(",")
euros = dinero[0]
centimos = dinero[1]
print("El número de euros es",euros, "y el número de céntimos es",centimos)