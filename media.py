aluno=input(f"Digite o nome do aluno: \n")
nota_1=float(input("Digite a primeira nota: "))
nota_2=float(input("Digite a segunda nota: "))
nota_3=float(input("Digite a terceira nota: "))

media=(nota_1 + nota_2 + nota_3)/3

if media >= 6.0:
    print("\naluno(a)",aluno," aprovado!! Sua media foi ",media)

else:
    print("\naluno(a)",aluno," reprovado!! Sua media foi ",media)