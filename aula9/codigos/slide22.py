def is_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

x = input("Digite um número: ")
x = int(x)
print(str(x)+" é par? "+str(is_par(x)))

