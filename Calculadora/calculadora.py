def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir entre cero"

print("Suma:", suma(2, 3))
print("Resta:", resta(5, 2))
print("Multiplicación:", multiplicacion(4, 6))
print("División:", division(10, 2))