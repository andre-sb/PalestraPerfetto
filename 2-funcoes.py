contador = 0

def funcaoA(v: int) -> int:
    global contador
    contador += 1
    soma = 0
    for i in range(v):
        soma += i
    return soma

def funcaoB(v:int) -> int:
    soma = 0
    for i in range(v):
        soma += funcaoA(i)
    return soma

def funcaoC(v:int) -> int:
    pass
    pass
    pass
    soma = funcaoB(v)
    pass
    pass
    pass
    if (v%2) != 0:
        soma += funcaoB(v)
    else:
        soma += funcaoA(v)
    pass
    pass
    pass
    return soma

def funcaoD(v:int) -> int:
    return funcaoA(v) + funcaoB(v) + funcaoC(v)

def main():
    a = funcaoA(3)
    b = funcaoB(4)
    c = funcaoC(5)
    d = funcaoD(6)
    print(f"{a=}\n{b=}\n{c=}\n{d=}")

if __name__ == "__main__":
    main()
