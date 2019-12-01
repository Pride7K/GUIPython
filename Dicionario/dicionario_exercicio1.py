from random import *
from operator import itemgetter

jogadores = {}

jogadores_vencedor = {}


for i in range (1,5):
    jogadores[f'Jogador{i}'] = randint(1,6);

print(jogadores)

for jogador,dado in jogadores.items():
    print(f'O {jogador} tirou {dado}');


print("");

jogadores_vencedor = sorted(jogadores.items(),key=itemgetter(1),reverse=True);

for i in jogadores_vencedor:
    print(f'{i[0]} tirou {i[1]} no dado');
