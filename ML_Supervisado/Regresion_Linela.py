# Regresión Lineal desde cero y con Scikit-learn

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos ficticios: metros cuadrados vs precio en miles de dólares
X = np.array([[50], [60], [80], [100], [120]])
y = np.array([150, 180, 220, 260, 300])
# Entrenar modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Predecir
nueva_casa = np.array([[90]])
prediccion = modelo.predict(nueva_casa)

print(f"Precio estimado para una casa de 90 m²: {prediccion[0]:.2f} mil dólares")
