def somaImposto(taxaImporto, custo):
    valor_final = custo + (taxaImporto * custo)
    return valor_final

valor = somaImposto(0.2, 100)
print(valor)