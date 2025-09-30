#Predice precio de casas según los m² que ingreses por teclado.
import numpy as np
from sklearn.linear_model import LinearRegression

# Datos ficticios
X = np.array([[50], [60], [80], [100], [120]])
y = np.array([150, 180, 220, 260, 300])

modelo = LinearRegression()
modelo.fit(X, y)

# Interactivo
while True:
    entrada = input("\nIngresa los m² de la casa (o escribe 'salir'): ")
    if entrada.lower() == "salir":
        break
    
