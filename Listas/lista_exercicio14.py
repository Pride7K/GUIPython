vetor1 = []

vetor2 = []

vetor3 = []

vetor4 = []

for i in range(1,31):
    if i<=10:
        vetor1.append(int(input(f'Digite um numero que sera colocado na posição {i}: ')));
        print("");
    elif i<=20:
        vetor2.append(int(input(f'Digite um numero que sera colocado na posição {i}: ')));
        print("");
    elif i<=30:
        vetor3.append(int(input(f'Digite um numero que sera colocado na posição {i}: ')));
        print("");

for i in vetor1:
    vetor4.append(i);

for i in vetor2:
    vetor4.append(i)

for i in vetor3:
    vetor4.append(i)

print(vetor4);
