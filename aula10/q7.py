valores = []
def valorPagamento(valor, atraso):
    valor_final = valor
    if atraso > 0:
        valor_final = valor + (0.03 * valor) + (atraso * 0.001 * valor)
    valores.append(valor_final)
    return valor_final

prestacao = ""
while prestacao != 0:
    prestacao = input("Digite o valor da prestação: ")
    prestacao = int(prestacao)
    if prestacao > 0:
        atraso = input("Digite o número de dias em atraso: ")
        atraso = int(atraso)
        valor_final = valorPagamento(prestacao, atraso)
        print(valor_final)
    else:
        print(len(valores))
        soma = 0
        for valor in valores:
            soma = soma + valor
        print(soma)