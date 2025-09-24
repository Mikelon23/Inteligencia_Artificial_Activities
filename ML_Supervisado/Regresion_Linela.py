# Regresión Lineal desde cero y con Scikit-learn

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos ficticios: metros cuadrados vs precio en miles de dólares
X = np.array([[50], [60], [80], [100], [120]])
y = np.array([150, 180, 220, 260, 300])
