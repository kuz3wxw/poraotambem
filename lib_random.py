
import random

numero_sorteado = random.randint(1,5)

sorteado = None
tentativas = 0

while sorteado != numero_sorteado:
    sorteado = int(input("Adivinhe o numero entre 1 e 100\n"))
    tentativas += 1

    if sorteado == numero_sorteado:
        print("Parabens voce adivinhou o numero em" , tentativas, "tentativas.")

    elif sorteado <= numero_sorteado:
        print("Digite um numero maior\n") 

    elif sorteado >= numero_sorteado:
        print("Digite um numero menor\n")  

    else:
        print("Digite algo valido\n")  