lista = []

continuar = "N"

while continuar == "N":
    valor = int(input("Digite um numero inteiro: "));
    print("");
    lista.append(valor);
    continuar = input("Deseja Sair ? S/N");
    print("");
    continuar = continuar.upper();

lista_par = []
lista_impar = []


for i in lista:
    valor = i % 2;
    if(valor == 0):
        lista_par.append(i);
    else:
        lista_impar.append(i);

print("Listas \n");

print(f'Os numeros que você digitou foram {lista} \n');

print(f'Os numeros pares que você digitou foram {lista_par} \n');

print(f'Os numeros impares que você digitou foram {lista_impar} \n');
