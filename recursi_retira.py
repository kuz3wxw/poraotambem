palavras = ["ferrari","lamborguini","mercedes","pagani","maserati","renessey","audi","bmw","lancia","ford"]

print("Todos os itens serão retirados um a um")

def retira_item():
    if len(palavras) == 0:
        print("Todas as palavras foram retiradas")
    else:
        palavras.pop()
        print(palavras)
        retira_item()

retira_item()