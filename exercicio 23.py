

try:
    numero1 = float(input())
    numero2 = float(input())
    operador = input()
    if operador == "+":
        resultado = numero1 + numero2
    elif operador == "-":
        resultado = numero1 - numero2
    elif operador == "*":
        resultado = numero1 * numero2
    elif operador == "/":
        resultado = numero1 / numero2
except ValueError:
    print("foi digitado um não float")

else:
    print(resultado)