from exercicio5.utilidadescev.dado import leiaDinheiro

valor = str(input('Digite o preço: R$'))
valor = float(valor.replace(',', '.'))
leiaDinheiro(valor)
