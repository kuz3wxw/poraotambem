import time

segundos = 0
minutos = 1 #int(input('Quantos minutos deseja esperar? '))

print(minutos,":",segundos)
for l in range(60*minutos):


    time.sleep(0.1)

    if segundos == 0 and minutos >= 0:
        minutos = minutos-1
        segundos = segundos + 59

    else:
        segundos = segundos-1

    print(minutos,":",segundos)

    if segundos == 0 and minutos == 0:
        print("seu tempo acabou")
