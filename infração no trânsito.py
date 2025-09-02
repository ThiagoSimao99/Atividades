cor_semaforo = str(input('Digite a cor do semáforo (verde, amarelo ou vermelho): '))
velocidade = int(input('Digite a velocidade do veículo (km/h): '))

if cor_semaforo == 'vermelho':
    print('Infração por avanço de sinal.')
else:
    pass
if velocidade > 66 and velocidade < 81:
    print('Infração grave por excesso de velocidade.')
elif velocidade >= 81:
    print('Infração gravíssima por excesso de velocidade.')
else:
    pass