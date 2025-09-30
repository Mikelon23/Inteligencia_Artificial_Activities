import numpy as np
from sklearn.linear_model import LogisticRegression

# Datos ficticios
X = np.array([[1], [2], [3], [4], [5], [6], [7]])
y = np.array([0, 0, 0, 1, 1, 1, 1])

modelo = LogisticRegression()
modelo.fit(X, y)

# Interactivo
while True:
    entrada = input("\nIngresa las horas de estudio (o escribe 'salir'): ")
    if entrada.lower() == "salir":
        break
    
     try:
        horas = float(entrada)
        prob = modelo.predict_proba([[horas]])[0][1]
        resultado = modelo.predict([[horas]])[0]
        print(f"Probabilidad de aprobar: {prob:.2f}")
        print("Resultado:", "Aprueba ✅" if resultado == 1 else "Reprueba ❌")
    except ValueError:
        print("Por favor ingresa un número válido.")