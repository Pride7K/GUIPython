lista = []


for c in range(1,6):
    lista.append(int(input("Digite um valor numerico: ")));
print("\n");

print("Mostrando o menor e o maior valor digitado! \n");

lista.sort();


for chave,valor in enumerate(lista):
    if(chave == 0):
        print(f'O menor valor digitado foi {valor} na posição {chave}');
    if(chave == 4):
        print(f'O maior valor digitado foi {valor} na posição {chave}');

