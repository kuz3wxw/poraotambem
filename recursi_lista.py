
frases = []
def nova_frase():
    print("Você deseja adicionar uma frase?\n Digite qualquer coisa,\n Caso não digitar nada,\n o programa para.")
    entrada = input("Digite a frase: ")
    if entrada == "":
        print("você não digitou nada, fim do programa.")
        print(frases)
    else:
        frases.append(entrada)
        nova_frase()

nova_frase()
 
