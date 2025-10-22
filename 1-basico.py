soma = 0

def funcaoA(v: int) -> int:
    global soma
    for i in range(v):
        soma += i
    return soma

print("Começou")
a = funcaoA(10)
print(f"{a=}")