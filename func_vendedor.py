nome = input("Digite nome do vendedor")
salario = int(input("Digite salario fixo"))
vendas = int(input("Digite o total de vendas no mes Ex:R$1000"))

def comisao(a):

   return a * 15 / 100

print(nome)
print(salario)
print("comisao do fim do mes ",comisao(salario))