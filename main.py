def calcular_prestamo():
    print("--- Calculadora de Préstamo Simple ---")

    try:
        # 1. Entrada de datos
        p = float(input("Introduce el monto del préstamo (P): "))
        r = float(input("Introduce la tasa de interés anual % (r): "))
        t = float(input("Introduce el tiempo en años (t): "))

        # 2. Lógica del cálculo
        interes = (p * r * t) / 100
        total_pagar = p + interes

        # 3. Mostrar resultados con dos decimales
        print("\n--- Resultados ---")
        print(f"Interés simple calculado: ${interes:.2f}")
        print(f"Total a pagar al final del periodo: ${total_pagar:.2f}")

    except ValueError:
        print("Error: Por favor, introduce solo valores numéricos.")

if __name__ == "__main__":
    calcular_prestamo()