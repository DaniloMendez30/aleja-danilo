def factura(cantidad,iva):
    total_factura = cantidad * iva
    print("el total de la factura es: " + str(total_factura))

log = """

escribe el porcentaje del iva a aplicar
si no tienes el valor del iva digita 0
: 

"""

cantidad = int(input("escribe el total del la factura con iva: "))
iva = int(input(log))

if iva == 0:
    iva = 0.21
    factura(cantidad,iva)
else:
    iva = iva/100
    factura(cantidad,iva)
