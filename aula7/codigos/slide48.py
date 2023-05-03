popA = 80000
taxA = 3/100

popB = 200000
taxB = 1.5/100

anos = 0

while popA <= popB:
    aumentoA = popA * taxA
    popA = popA + aumentoA

    aumentoB = popB * taxB
    popB = popB + aumentoB

    anos = anos + 1

print(anos)

