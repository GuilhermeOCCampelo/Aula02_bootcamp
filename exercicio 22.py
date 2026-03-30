palavra = input()

if isinstance(palavra,str):
    formatado = palavra.replace(" ","").lower()
    if formatado == formatado[::-1]:
        print("palindromo")
    else:
        print("não palindromo")
else:
    print("não é string")        