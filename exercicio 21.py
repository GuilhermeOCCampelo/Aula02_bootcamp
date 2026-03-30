
try:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = celsius * (9/5) + 32
    print(fahrenheit)
except ValueError as e: 
    print("não é inteiro")