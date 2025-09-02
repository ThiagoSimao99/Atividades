km_inicial = float(input('Quilometragem inicial: '))
km_final = float(input('Quilometragem final: '))
litros = int(input('Digite aqui quantos litros irá colocar: '))
combustivel = int(input('''Qual tipo de combustível voce deseja?
[1] Gasolina
[2] Gasolina Aditivada
[3] Álcool
[4] Diesel
Digite aqui o tipo de combustível: '''))
autonomia = (km_final - km_inicial) / litros

if combustivel == 1:
    print(f'Você colocou {litros} litros de gasolina e sua autonomia foi de {autonomia:.1f} km/l.')
elif combustivel == 2:
    print(f'Você colocou {litros} litros de gasolina aditivada e sua autonomia foi de {autonomia:.1f} km/l.')
elif combustivel == 3:
    print(f'Você colocou {litros} litros de álcool e sua autonomia foi de {autonomia:.1f} km/l.')
elif combustivel == 4:
    print(f'Você colocou {litros} litros de diesel e sua autonomia foi de {autonomia:.1f} km/l.')
else:
    print('Número inválido.')