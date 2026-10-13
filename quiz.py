# Codigo de prueba

monto_total_diario = 0.0
open_caja = True

while open_caja:
    print("Menú")
    print("1. Registrar ventas. ")
    print("2. Ver total acumulado del día. ")
    print("3. Cerrar caja y salir. ")
    opcion = int(input("Elija una opcion: "))

    if opcion < 1 or opcion > 3:
        print("Error, por favor ingrese un opcion valida.")
        input("Presiona Enter para volver a intentar.")

    if opcion == 3:
        print("Gracias por utilizar nuestros servicios. Venta cerrada.")
        print("Su monto total diario acumulado es:", monto_total_diario)
        open_caja = False

    if opcion == 1:
        print("Registro del cliente")
        subtotal_cliente = 0
        registro_venta = True

        while registro_venta:
            precio = input("Ingrese el precio del producto(s): ")

            if precio < "0":
                print("Error")
                input("Presione intro para volver a intentar.")

            if precio == "0" or precio == "Fin":
                registro_venta = False
            
            else:
                precio = int(precio)
                subtotal_cliente = subtotal_cliente + precio

        monto_iva = subtotal_cliente * 0.19
        total_cliente = monto_iva + subtotal_cliente

        print(" Boleta ")
        print("Subtotal cliente: ", subtotal_cliente)
        print("IVA: ", monto_iva)
        print("Total (+IVA): ", total_cliente)
        input("Presione Enter para ir al siguiente.")
        
        calculo = True
        while calculo:

            print("Metodos de pago")
            print("1. Efectivo. ")
            print("2. Tarjeta. ")
            opcion2 = int(input("Seleccione un metodo de pago: "))

            if opcion2 < 1 or opcion2 > 2:
                print("Error, por favor ingrese una opcion valida.")
                input("Presiona Enter para volver a intentar.")
            
            if opcion2 == 1:
                descuento = total_cliente * 0.05
                total_cliente_descuento = total_cliente - descuento
                print ("Usted a pagado en efectivo recibe un descuento del 5%:", descuento)
                print("Valor final: ", total_cliente_descuento)
                input("Presione Enter para volver al menu principal.")
                monto_total_diario = monto_total_diario + total_cliente_descuento
                calculo = False
            
            elif opcion2 == 2:
                print("Ha elegido pagar con tarjeta, usted tiene que pagar:", total_cliente)
                input("Presione Enter para volver al menu principal.")
                monto_total_diario = monto_total_diario + total_cliente
                calculo = False

            if total_cliente >= 15000:
                print("Venta alta.")
            else:
                print("Venta habitual.")

    if opcion == 2:
        print("Su monto total diario acumulado es:", monto_total_diario)
        input("Presione intro para continuar.")