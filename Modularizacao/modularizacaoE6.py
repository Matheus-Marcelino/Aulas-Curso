from exercicio5.utilidadescev.dado import leiaDinheiro

valor = float(input('Digite o preço: R$'))
valor = str(valor).replace('.', ',')

leiaDinheiro(float(valor))
