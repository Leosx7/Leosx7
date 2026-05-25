hora_atual = int(input("Digite a hora atual (0-23): "))

def saudacao(hora):
    if 0 <= hora < 12:
        return "Bom dia!"
    elif 12 <= hora < 18:
        return "Boa tarde!"
    elif 18 <= hora < 24:
        return "Boa noite!"
    else:
        return "Hora inválida. Por favor, digite um valor entre 0 e 23."
print(saudacao(hora_atual))