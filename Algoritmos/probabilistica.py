import numpy as np

def lanzar_moneda():
    # Genera un número aleatorio entre 0 y 1
    resultado = np.random.rand()

    # Determina si es cara o cruz basado en la probabilidad de 0.5 para cada lado
    if resultado < 0.5:
        return "Cara"
    else:
        return "Cruz"

# Simula el lanzamiento de una moneda
resultado_lanzamiento = lanzar_moneda()

# Muestra el resultado
print(f"Resultado del lanzamiento de la moneda: {resultado_lanzamiento}")