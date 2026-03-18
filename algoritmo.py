def busqueda_binaria(lista, punto):
    izquierda = 0 # apunta al inicio
    derecha = len(lista) - 1 # apunta al final

    while izquierda <= derecha: # El valor solo puede existir si hay al menos un elemento en el rango; 
    # izq = der es todavía válido, ese único elemento podría ser el que se busca

        centro = (izquierda + derecha) // 2 # se va recalculando el nuevo centro

        print("Izquierda:", izquierda, "Centro:", centro, "Derecha:", derecha)

        if lista[centro] == punto: # Si el valor en el centro es lo que buscas
            return centro # Devuelve el resultado y TERMINA la función inmediatamente por ende tambien el bucle

        elif punto > lista[centro]: # Todo lo de la izquierda ya no sirve; incluyendo el centro
            izquierda = centro + 1 # El nuevo inicio (izquierda) se mueve a la derecha

        else: # Todo lo de la derecha ya no sirve; incluyendo el centro
            derecha = centro - 1 # El nuevo final (derecha) se mueve a la izquierda

    return -1


numeros = [1, 3, 5, 7, 9, 11, 13] # izquierda = 0 → valor 1 | derecha = 6 → valor 13
        #  0  1  2  3  4  5   6
resultado = busqueda_binaria(numeros, 7)

print(resultado)  # Devuelve 3