ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

def calcular_idade(ano_nascimento, ano_atual):
    idade = ano_atual - ano_nascimento
    return idade
idade = calcular_idade(ano_nascimento, ano_atual)
print("A idade da pessoa é:", idade)