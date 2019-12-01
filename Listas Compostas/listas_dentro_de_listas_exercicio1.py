
numeros = [[],[]]

valor_check = float;

print("Exercicio onde só pode usar uma lista e todos os valores devem ser armazenados separadamente em pares e impares e serem printados no final em ordem crescente ! \n");

for i in range(0,7):
    valor = int(input("Digite um numero inteiro: "));
    print("");
    valor_check = valor % 2;
    if(valor_check == 0):
        numeros[0].append(valor);
    else:
        numeros[1].append(valor);

print(sorted(numeros[0]));

print(sorted(numeros[1]));

print(numeros);
