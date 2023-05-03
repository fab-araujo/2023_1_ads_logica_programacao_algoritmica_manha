usuario = input("Digite um usuário: ")
senha = input("Digite uma senha: ")

while usuario == senha:
    print("Erro! Usuário e senha não podem ser iguais!")
    usuario = input("Digite um usuário: ")
    senha = input("Digite uma senha: ")

print("Obrigado!")

