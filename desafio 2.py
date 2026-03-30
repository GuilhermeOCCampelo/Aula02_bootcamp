fixo = 1000
usuario = input("digite seu nome: ")
if usuario.isdigit():
    print("digitou seu nome errado")
    exit()
if len(usuario.strip())==0:
    print("você não digitou nada")
    exit()
try:
    salario = int(input("digite seu salário: "))
    bonus = int(input("digite sua porcentagem do bonus: "))

except ValueError:
    print("VocÊ não digitou um número")
else:
    resultado = fixo + salario * (bonus/100)

    print(f"seu bonus foi {resultado}")

