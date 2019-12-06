

par = []

impar = []

numeros = []

for i in range(0,20):
    valor = int(input("Digite um numero: "));
    print("");
    numeros.append(valor);
    check = valor % 2
    if(check == 0):
        par.append(valor);
    else:
        impar.append(valor);

print(f'Os numeros digitados foram {numeros} \n');

print(f'Os numeros pares digitados foram {par} \n');

print(f'Os numeros impares digitados foram {impar} \n');
