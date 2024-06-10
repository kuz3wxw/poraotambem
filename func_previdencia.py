
sexo = str(input("Qual o seu sexo (M/F)? "))
idade_inc_contri = int(input("Qual idade comecou a contribuir? "))


idade_contri_proj_m = 65 - idade_inc_contri

if sexo == "M" or sexo == "m":
    if idade_contri_proj_m <= 25:
        print("Voce só terá direito a se aposentar com 65 anos")
        print("")
