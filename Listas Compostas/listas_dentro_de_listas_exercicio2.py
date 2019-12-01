
print("Exercicio onde deve-se criar uma matriz 3x3,receber numeros e preencha-la com eles e mostra-la no final \n");

matriz = []

for i in range(0,3):
    linha = []
    for j in range(0,3):
        valor = int(input("Digite um numero: "));
        linha.append(valor);
    matriz.append(linha[:]);

print("");
for i in matriz:
    print(f'[{i[0]}] [{i[1]}] [{i[2]}] \n');
