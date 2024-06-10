
codigo = int(input("Digite o codigo: "))
quantidade= int(input("Digite a quantidade :"))


match codigo:
    case 100:
        result =  quantidade * 1.70 
        print("Vai pagar")

    case 101:
        result1 = quantidade * 2.30 
        print("o valor a pagar é" + result1)

    case 102:
        result2 = quantidade * 2.60 
        print("o valor a pagar é" + result2)

    case 103:
        result3 = quantidade * 2.40 
        print("o valor a pagar é" + result3)

    case 104:
        result4 = quantidade * 2.50 
        print("o valor a pagar é" + result4)

    case 105:
        result5 = quantidade * 1.00 
        print("o valor a pagar é" + result5)

    case _:
        print("Invalido")