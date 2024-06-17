import somar
import subtrair
import multiplicacao
import divisao

calculos =int(input("Escolha um numero / 1-somar / 2-subtrair / 3-multiplicar / 4-dividir: "))

a = int(input("Escolha o primeiro numero: "))

b = int(input("Escolha o segundo numero: "))
                   
match calculos:
    case 1:
        somar.somar(a,b)

    case 2:
        subtrair.subtracao(a,b)

    case 3:
        multiplicacao.multiplicacao(a,b)

    case 4:
        divisao.divisao(a,b)
