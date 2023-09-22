resposta="S"
while resposta=="S":
    nota1 = int(input("Digite a primeira nota: "))

    while nota1 < 0 or nota1 > 10:
        nota1 = int(input("Digite a primeira nota novamente: "))


    nota2 = int(input("Digite a segunda nota: "))
    while nota2 < 0 or nota2 > 10:
        nota2 = int(input("Digite a segunda nota novamente: "))
    media = (nota1 + nota2) / 2
    print(f"a média do aluno é {media}")
    resposta=input("deseja realizar o cáulculo novamente? use S para sim e N para não: ")
else:
    print("cabou")
