numero=int(input("Digite o numero: "))
for x in range(1, numero+1, 1):
    for y in range(1, x+1):
        print(f"{y} ", end=" ")
    print()