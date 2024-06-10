
print("Digite um numero para:")
print("1-media entre os numeros")
print("2-diferença entre os numeros")
print("3-produto entre os numeros digitados")
print("4-divisao do primeiro pelo segundo")

operacao= int(input("Digite um numero: "))

primeiro_n = int(input("Digite o primeiro numero: "))
segundo_n= int(input("Digite o segundo numero : "))


match operacao:

    case 1:
        result = (primeiro_n + segundo_n) / 2 
        print("a media ente os numeros é" + result)

    case 2:
        result1 = primeiro_n - segundo_n
        print("o resultado é" + result1)

    case 3:
        result2 = primeiro_n * segundo_n
        print("o resultado é" + result2)

    case 4:
        result3 = primeiro_n / segundo_n
        print("o resultado é" + result3)

    case _:
        print("Invalido")