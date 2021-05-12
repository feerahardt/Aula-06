def somaImposto(taxaImposto, custo):
    valorAtualizado = (taxaImposto/100 * custo) + custo
    print(valorAtualizado)


somaImposto(13, 10)
