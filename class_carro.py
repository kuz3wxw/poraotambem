class Carro:
    marca = "chevrolet"
    modelo = "onix sedan"
    ano = 2020
    cor = "preto"
    placa = "BRE54D6"

    def __init__(self, marca, modelo, ano, cor, placa):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.placa = placa

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.ano} {self.cor} {self.placa}"
       

new_carro = Carro("HYUNDAY","HB20",2020,"branco","BVE54D6")

print(new_carro)

