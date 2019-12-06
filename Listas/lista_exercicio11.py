
numeros = []

soma = []

multi = []

aux = 0;

aux2 = 1;

for i in range(1,6):
    valor = int(input("Digite um numero inteiro: "));
    print("");
    numeros.append(valor);
    soma.append(valor);
    multi.append(valor);



for i in soma:
    aux += i;

for i in multi:
    print(i);
    aux2 *= i;


print(f'O resultado da soma dos seguintes numeros {numeros} foi de {aux} \n');

print(f'O resultado da multiplicação dos seguintes numeros {numeros} foi de {aux2}');

