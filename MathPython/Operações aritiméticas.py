n1 = int(input('um valor '))
n2 = int(input('Outro Valor '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2


print('A soma é {},a multiplicão é {} e a divisão é {:.3f}'.format(s, m, d), end=' >>> ')
print('Divisão inteira é {} e a potencia é {}'.format(di, e))
#:.3f : até tres casas decimais
#end= ' ' : ele junta as linhas
#\n : Ele quebra a linha
