
def ola():
    entr = input("")
    if entr == "paro":
        print("paro")
    else:
        print("ola")
        ola()

ola()