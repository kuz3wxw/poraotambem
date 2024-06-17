class Aluno:
    def __init__(self, nome, idade):
        self.idade = idade
        self.nome = nome


aluno1 = Aluno('Alysson', 20)

print(aluno1.nome, aluno1.idade)

