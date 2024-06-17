class Computador:
    
    def __init__(self, cpu, qntd_memoria, ligado):
        self.cpu = cpu
        self.qntd_memoria = qntd_memoria
        self.ligado = ligado
       
    def ligar(self):
        self.ligado = True
        print("ligando")

    def desligar(self):
        self.ligado = False
        print("desligando")

class Pc_gammer(Computador):
    def __init__(self, cpu, qntd_memoria, ligado):
        super().__init__(cpu, qntd_memoria, ligado)
        self.jogando = False

    def iniciar_jogo(self):
        self.jogando = True
        print("jogando")

    def fechar_jogo(self):
        self.jogando = False
        print("fechando jogo")

computador = Computador("intel", 4, True)

computador.ligar()

pcgamer = Pc_gammer("intel", 4, True)

pcgamer.iniciar_jogo()




