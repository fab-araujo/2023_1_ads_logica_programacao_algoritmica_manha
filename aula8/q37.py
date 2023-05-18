valor = 0

val_0_25 = 0
val_26_50 = 0
val_51_75 = 0
val_76_100 = 0

while valor >= 0:
    valor = input("Digite um valor: ")
    valor = int(valor)
    if valor >= 0 and valor <= 25:
        val_0_25 = val_0_25 + 1
    elif valor >= 26 and valor <= 50:
        val_26_50 = val_26_50 + 1
    elif valor >= 51 and valor <= 75:
        val_51_75 = val_51_75 + 1
    elif valor >= 76 and valor <= 100:
        val_76_100 = val_76_100 + 1

print(val_0_25)
print(val_26_50)
print(val_51_75)
print(val_76_100)