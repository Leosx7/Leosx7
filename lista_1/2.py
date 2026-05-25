A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

total = A + B + C
if A < 0 or B < 0 or C < 0:
    print("Os dias devem ser positivos")
else:
    print("O total de dias é:", total)