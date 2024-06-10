
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

nota_final = (nota1 + nota2) / 2


match nota_final:

    case x if nota_final >= 0.0 and nota_final <= 4.0:
        print("Reprovado")

    case x if nota_final >= 4.1 and nota_final <= 7.0:
        print("Exame")

    case x if nota_final >= 7.1 and nota_final <= 10.0:
        print("Aprovado")

    case _:
        print("Invalido")
        
        
        # 0,0-4,0 reprova
        # 4,1-7,0 exam
        # 7,1-10 aprovado