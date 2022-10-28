from exercicio5.utilidadescev.dado import leiaDinheiro

valor = str(input('Digite o preço: R$'))
valor = valor.replace(',', '.')
leiaDinheiro(valor)
