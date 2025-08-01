def suma(a, b): return a + b
def resta(a, b): return a - b
def multiplicacion(a, b): return a * b
def division(a, b): return a / b if b != 0 else "No se puede dividir entre cero"

print("Calculadora Básica")
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

print("Suma:", suma(a, b))
print("Resta:", resta(a, b))
print("Multiplicación:", multiplicacion(a, b))
print("División:", division(a, b))