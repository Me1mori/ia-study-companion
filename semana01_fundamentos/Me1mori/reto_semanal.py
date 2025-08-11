entrada = True

while entrada:
    a = float(input("Num 1: "))
    signo = input("+, -, *, /: ")
    b = float(input("Num 2: "))
    total = 0

    if signo == '+':
        total = a + b
    elif signo == '-':
        total = a - b
    elif signo == '*':
        total = a * b
    elif signo == '/':
        if b != 0:
            total = a / b
        else:
            total = "Error: división entre cero"
    else:
        total = "Operación no válida"

    if isinstance(total, float):
        if total.is_integer():
            total = int(total)

    print(f"El total es: {total}")

    entrada = input("¿Quieres terminar? (si/no): ").strip().lower()
    if entrada == "si" or "s":
        entrada = False
    else:
        entrada = True
