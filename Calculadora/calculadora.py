def suma(a, b): return a + b
def resta(a, b): return a - b
def multiplicacion(a, b): return a * b
def division(a, b): return a / b if b != 0 else "No se puede dividir entre cero"

print("Calculadora Básica")
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

print("Elige la operación:")
print("1. Suma\n2. Resta\n3. Multiplicación\n4. División")
opcion = input("Opción (1-4): ")

if opcion == "1":
    print("Resultado:", suma(a, b))
elif opcion == "2":
    print("Resultado:", resta(a, b))
elif opcion == "3":
    print("Resultado:", multiplicacion(a, b))
elif opcion == "4":
    print("Resultado:", division(a, b))
else:
    print("Opción no válida")