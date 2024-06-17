class Peixe:


    def __init__(self, especie, tipo_de_agua, profundidade_encontrada):
        self.especie = especie
        self.tipo_da_agua = tipo_de_agua
        self.profundidade_encontrada = profundidade_encontrada

list_peixes = []

list_nomes = ["Truta Arco-íris", "Salmão", "Atum", "Bagre", "Tubarão-branco"]
list_tipo_de_agua = ["doce", "doce e salgada", "salgada", "doce", "salgada"]
list_profundidade_encontrada =[20, 100, 200, 10, 1.200]

    
for especie, tipo_de_agua, profundidade_encontrada in zip(list_nomes, list_tipo_de_agua, list_profundidade_encontrada):

    list_peixes.append(Peixe(especie, tipo_de_agua, profundidade_encontrada))

for peixe in list_peixes:
    print(f"especie: {peixe.especie}  tipo da agua: {peixe.tipo_da_agua}profundidade:  {peixe.profundidade_encontrada}")
