vetor = []

media = 0;

for i in range(0,4):
    vetor.append(int(input("Digite a nota: ")));
    print("");



for i in vetor:
    media += i

media = media /4

print(f'{vetor[0]} {vetor[1]} {vetor[2]} {vetor[3]} equivale a média = {media}');
