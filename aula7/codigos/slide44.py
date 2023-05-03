bits = []
n_bits = list(range(8))
n0s = 0
n1s = 0

for idx in n_bits:
    bit = input("Digite um bit: ")
    bit = int(bit)
    bits.append(bit)

for bit in bits:
    if bit == 0:
        n0s = n0s + 1
    else:
        n1s = n1s + 1

print(n0s)
print(n1s)

