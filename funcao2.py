
x = 10      #aqui ela ta fora entao pode ser usada em qualquer lugar até dentro da função

def escreve_global():
    print(x) 

escreve_global()



def escreve_escopo():
    y = 10    #aqui a variavel ta dentro, entao a variavel é somente da função. 
    print(y)

escreve_escopo()

