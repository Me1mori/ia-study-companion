"""
Reto Semanal: Calculadora de operaciones básicas

Crea un programa que reciba dos números y una operación (+, -, *, /)
y muestre el resultado. Debe validar errores como división entre cero.
"""

def calculadora(a, b, operacion):
    if operacion == '+':
        return a + b
    elif operacion == '-':
        return a - b
    elif operacion == '*':
        return a * b
    elif operacion == '/':
        return "Error: división entre cero" if b == 0 else a / b
    else:
        return "Operación no válida"

