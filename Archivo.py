import random
def RandomSelect():
    listText = ["hobbit.txt", "llano.txt"]
    return random.choice(listText)

def LeerArchivo():
    selection = RandomSelect()
    with open(selection,"r") as f:
        lista = f.read().split()

    return lista

print(LeerArchivo())

