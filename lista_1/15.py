palavra = input("Digite uma palavra: ")

def quantidade_caracteres(palavra):
    quantidade = len(palavra)
    return quantidade
quantidade = quantidade_caracteres(palavra)
print("Essa palavra tem", quantidade, "caracteres.")