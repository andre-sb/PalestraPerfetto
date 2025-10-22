# Inclui inicio do script no JSON
soma = 0

def funcaoA(v: int) -> int:
    #Inclui inicio da função no JSON
    global soma
    for i in range(v):
        soma += i     # Inclui valor da soma no JSON
    #Inclui fim da função no JSON
    return soma

print("Começou")    # Inclui evento "Começou" no JSON
a = funcaoA(10)
print(f"{a=}")      # Inclui evento "a=<valor>" no JSON

# Inclui fim do script no JSON