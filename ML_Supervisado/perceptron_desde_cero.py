from typing import List


class PerceptronDesdeCero:
    """Perceptrón binario (0/1) entrenado con la regla de aprendizaje del perceptrón."""

    def __init__(self, tasa_aprendizaje: float = 0.1, epocas: int = 10):
        self.tasa_aprendizaje = tasa_aprendizaje
        self.epocas = epocas
        self.pesos: List[float] = []
        self.sesgo = 0.0

    @staticmethod
    def funcion_activacion(z: float) -> int:
        return 1 if z >= 0 else 0

    @staticmethod
    def producto_punto(a: List[float], b: List[float]) -> float:
        return sum(x * y for x, y in zip(a, b))

    def predecir(self, x: List[float]) -> int:
        z = self.producto_punto(x, self.pesos) + self.sesgo
        return self.funcion_activacion(z)

    def entrenar(self, x: List[List[float]], y: List[int], verbose: bool = True) -> None:
        n_caracteristicas = len(x[0])
        self.pesos = [0.0 for _ in range(n_caracteristicas)]
        self.sesgo = 0.0

        if verbose:
            print("\nPASO 1) Inicialización")
            print(f"- Pesos iniciales: {self.pesos}")
            print(f"- Sesgo inicial: {self.sesgo}")
            print(f"- Tasa de aprendizaje: {self.tasa_aprendizaje}")
            print(f"- Épocas máximas: {self.epocas}\n")

        for epoca in range(1, self.epocas + 1):
            errores = 0
            if verbose:
                print(f"PASO 2) ÉPOCA {epoca}")

            for i, (x_i, y_real) in enumerate(zip(x, y), start=1):
                z = self.producto_punto(x_i, self.pesos) + self.sesgo
                y_pred = self.funcion_activacion(z)
                error = y_real - y_pred

                if error != 0:
                    self.pesos = [
                        peso + self.tasa_aprendizaje * error * valor_x
                        for peso, valor_x in zip(self.pesos, x_i)
                    ]
                    self.sesgo += self.tasa_aprendizaje * error
                    errores += 1

                if verbose:
                    print(f"  Muestra {i}: x={x_i}, y_real={y_real}")
                    print(f"    - z = w·x + b = {z:.2f}")
                    print(f"    - y_pred = {y_pred}")
                    print(f"    - error = y_real - y_pred = {error}")
                    print(f"    - pesos actualizados: {self.pesos}")
                    print(f"    - sesgo actualizado: {self.sesgo:.2f}\n")

            if verbose:
                print(f"  Errores en la época {epoca}: {errores}\n")

            if errores == 0:
                if verbose:
                    print("PASO 3) Convergencia alcanzada: no hay errores en la época.\n")
                break


def ejercicio_perceptron_and() -> None:
    """Ejercicio completo desde cero con la compuerta lógica AND."""

    # Dataset: compuerta AND
    x = [
        [0.0, 0.0],
        [0.0, 1.0],
        [1.0, 0.0],
        [1.0, 1.0],
    ]
    y = [0, 0, 0, 1]

    print("=== EJERCICIO: PERCEPTRÓN DESDE CERO (A MODO SCRATCH) ===")
    print("Objetivo: aprender la compuerta lógica AND (salida 1 solo cuando ambas entradas son 1).")
    print("\nPASO 0) Datos de entrenamiento")
    for entrada, salida in zip(x, y):
        entrada_legible = [int(valor) for valor in entrada]
        print(f"- Entrada: {entrada_legible} -> Salida esperada: {salida}")

    perceptron = PerceptronDesdeCero(tasa_aprendizaje=0.2, epocas=10)
    perceptron.entrenar(x, y, verbose=True)

    print("PASO 4) Parámetros finales aprendidos")
    print(f"- Pesos finales: {perceptron.pesos}")
    print(f"- Sesgo final: {perceptron.sesgo:.2f}\n")

    print("PASO 5) Prueba final del modelo")
    for entrada, salida_real in zip(x, y):
        salida_predicha = perceptron.predecir(entrada)
        entrada_legible = [int(valor) for valor in entrada]
        print(f"- Entrada: {entrada_legible} | y_real: {salida_real} | y_predicha: {salida_predicha}")


if __name__ == "__main__":
    ejercicio_perceptron_and()
