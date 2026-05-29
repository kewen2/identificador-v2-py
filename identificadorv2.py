lista = []
num = num2 = num_cont = num5 = 0
resp = se5foidigitado = se5estanalista = ""

while resp != "N":
    num = int(input("DIGITE UM NÚMERO"))
    lista.append(num)
    num_cont += 1
    if num == 5:
        num5 += 1
        if num5 >= 1:
            se5foidigitado = "SIM"
            se5estanalista = "SIM"
    


    resp = str(input("QUER PARAR? [RESPONDA N]")) 
for cont in lista:
    print(cont, end= ' ')
print(f"O NÚMERO 5 FOI DIGITADO? {se5foidigitado}")
print(f"ESTÁ NA LISTA? {se5estanalista}")
print(f"{num_cont} NÚMEROS FORAM DIGITADOS")
