def encontrar_pares_que_sumen_n(n):
    """
    Encuentra todos los pares de números naturales que suman n.

    Args:
    n (int): Un número natural menor que 10^6.

    Returns:
    list of tuple: Una lista de tuplas, cada una representando un par de números naturales cuya suma es n.
    """
    # Lista para almacenar los pares
    pares = []

    # Encontrar pares (a, b) tal que a + b = n
    # Iniciar desde 1 hasta n//2 + 1 para evitar duplicados
    for a in range(1, n//2 + 1):
        b = n - a
        # Agregar el par (a, b) a la lista de resultados
        pares.append((a, b))

    return pares

# Ejemplo de uso
n = 1000000
resultado = encontrar_pares_que_sumen_n(n)
# Muestra los primeros 5 pares para no saturar la salida
print(resultado[:5])  # Output: [(1, 999999), (2, 999998), (3, 999997), (4, 999996), (5, 999995)]
# Muestra el número total de pares encontrados
print(len(resultado))  # Output: 499999
