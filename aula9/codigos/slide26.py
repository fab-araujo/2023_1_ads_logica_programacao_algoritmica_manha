
def is_primo(n):
    contador = 2
    while contador < n:
        if n % contador == 0:
            return False
        contador = contador + 1
        
    return True

n = input("Digite um número: ")
n = int(n)
print(str(n)+" é primo? "+str(is_primo(n)))

