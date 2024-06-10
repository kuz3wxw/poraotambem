gasto_total = 0
bebida = int(input("Voce planeja beber, digite 0 para nao e 1 para sim: "))
comida = int(input("Voce planeja comer, digite 0 para nao e 1 para sim: "))
transporte = int(input("Voce planeja contratar tranporte, digite 0 para nao e 1 para sim: "))
pessoas = int(input("Quantas pessoas sairam com voce: "))

def vai_bebe_come_transp(b,c,t,a):
    global gasto_total
    if b == 1:
        gasto_total += 80
    if c == 1:
        gasto_total += 60
    if t == 1:
        gasto_total += 15
    if a > 0:
        gasto_total += gasto_total*a+1
    
vai_bebe_come_transp(bebida,comida,transporte,pessoas)

print(f"o gasto estimado da noite é R${gasto_total}")


#bebida = 80 
#comida = 60
#transporte = 15

