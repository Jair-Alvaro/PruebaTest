def contar_unicos_y_repetidos(matriz):
    """
    Cuenta la cantidad de números que aparecen solo una vez y la cantidad de términos repetidos en una matriz nxn.

    Args:
    matriz (list of list of int): Una matriz nxn de enteros.

    Returns:
    list: Un arreglo cuyo primer elemento es la cantidad de números únicos y el segundo elemento es la cantidad de números repetidos.
    """
    # Diccionario para almacenar la frecuencia de cada número
    frecuencia = {}

    # Contar la frecuencia de cada número en la matriz
    for fila in matriz:
        for numero in fila:
            if numero in frecuencia:
                frecuencia[numero] += 1
            else:
                frecuencia[numero] = 1

    # Contar números únicos y repetidos
    cantidad_unicos = 0
    cantidad_repetidos = 0

    for cantidad in frecuencia.values():
        if cantidad == 1:
            cantidad_unicos += 1
        else:
            cantidad_repetidos += 1

    return [cantidad_unicos, cantidad_repetidos]

# Ejemplos de uso
print(contar_unicos_y_repetidos([[2, 2], [2, 2]]))  # Output: [0, 1]
print(contar_unicos_y_repetidos([[2, 1, 3], [4, 5, 2], [6, 6, 6]]))  # Output: [4, 2]
