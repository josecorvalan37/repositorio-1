print("¡Bienvenido a tu lista de compras!")
productos = []

productos.append("Leche")
productos.append("Pan")

print("\nProductos iniciales:", productos)
print("\nAhora, añade tu producto.")

nuevo_producto = input("Introduce el nombre de tu producto: ")
productos.append(nuevo_producto)

print("\nLista de productos después de añadir uno nuevo:", productos)


producto_a_modificar = input("\n¿Quieres modificar algún producto? (Escribe el nombre del producto a modificar): ")

if producto_a_modificar in productos:
    nuevo_nombre = input(f"Escribe el nuevo nombre para {producto_a_modificar}: ")
    index = productos.index(producto_a_modificar)
    productos[index] = nuevo_nombre
    print(f"\nEl producto ha sido modificado: {productos}")
else:
    print("\nNo se encontró el producto para modificar.")

    producto_a_eliminar = input("\n¿Quieres eliminar un producto? (Escribe el nombre del producto a eliminar): ")

if producto_a_eliminar in productos:
    productos.remove(producto_a_eliminar)
    print(f"\nEl producto ha sido eliminado. Lista actualizada: {productos}")
else:
    print("\nEl producto no se encuentra en la lista.")

    print("\nLista final de productos para comprar:", productos)