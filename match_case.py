codigo = int(input("Digite o codigo do produto: "))

match codigo:
    case 1:
        print("Alimento não-perecivel")

    case x if codigo >= 2 and codigo <= 4:
        print("Alimento perecivel")

    case x if codigo >= 5 and codigo <= 6:
        print("Vestuario")

    case 7:
        print("Higiene pessoal")
        
    case codigo if codigo >= 8 or codigo <= 15:
        print("Limpeza e utensilios domesticos")

    case _:
        print("Codigo invalido")