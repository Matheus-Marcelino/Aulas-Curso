from math import cos, sin, tan, radians

n = float(input('Digite um valor: '))

print(f'seu cosseno é {cos(radians(n)):.2f}\nO seu seno é {sin(radians(n)):.2f}\nA sua tangente é '
      f'{tan(radians(n)):.2f}')  # passando tudo para radianos
