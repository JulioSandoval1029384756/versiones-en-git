def suma(a, b): return a + b
def resta(a, b): return a - b
def multiplicacion(a, b): return a * b
def division(a, b): return a / b if b != 0 else "Error: División entre cero"

while True:
    print("\nCalculadora Básica")
    try:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Error: Ingresa solo números")
        continue

    print("Operaciones:\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Salir")
    opcion = input("Opción (1-5): ")

    if opcion == "1":
        print("Resultado:", suma(a, b))
    elif opcion == "2":
        print("Resultado:", resta(a, b))
    elif opcion == "3":
        print("Resultado:", multiplicacion(a, b))
    elif opcion == "4":
        print("Resultado:", division(a, b))
    elif opcion == "5":
        print("Gracias por usar la calculadora.")
        break
    else:
        print("Opción no válida")