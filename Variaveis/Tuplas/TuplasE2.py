times = ('Palmerias', 'Internacional', 'Corinthians', 'Flamengo', 'Fluminense',
         'Athletico-PR', 'Atlético-MG', 'América-MG', 'Botafogo', 'Fortaleza',
         'Santos', 'São Paulo', 'Brangantino', 'Goiás', 'Coritiba', 'Ceará SC',
         'Cuiabá', 'Atlético-GO', 'Avaí', 'Juventude')

print(times, '\n')
print(times[-4:], '\n')
print(times[0:5], '\n ')
print(sorted(times), '\n')
try:
    print(times.index('Chapecoense'+1), '\n')
except ValueError:
    print('Infelizmente chapecoense não está entre os 20 colocados\n')
