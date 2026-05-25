contagem = 10

while contagem > 0:
    if contagem % 2 == 0:
        print("Faltam apenas ", contagem, "segundos - não perca essa oportunidade!")
    else:
        print("A contagem continua: ", contagem, "segundos restantes.")
    contagem -= 1
print("Aproveite a promoção agora!")