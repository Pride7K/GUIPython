
print("Brincando com as listas do python \n");

print("Tuplas \n")

print("Tuplas que são listas só que ao inves de [] é () são imutaveis ou seja nao tem como inserir ou alterar seus valores \n");

lista_tupla = (4,5,2,3,1,10)

try:
    lista_tupla.pop();
except:
    print("nao deu pra deletar \n");
else:
    print(lista_tupla);


try:
    lista_tupla.append(11);
except:
    print("nao deu pra inserir \n");
else:
    print(lista_tupla);

lista2 = []

for c in range(1,5):
    lista2.append(int(input("Digite um valor inteiro: ")))


for c,v in enumerate(lista2):
    print(f'Na posição {c} achei o valor {v}');
print("Cheguei ao final da lista2 \n");


##lista.insert(1,5);

##print(lista)

lista = [4,5,2,3,1,10]


print(lista)

lista.pop(1);

print(lista)

print("sorted");

print(sorted(lista,reverse=True))

print(sorted(lista,reverse=False))

print(lista)

lista = [4,5,2,3,1,10]


print("sort")

lista.sort();

print(lista);

print(len(lista));

print("Duplicando listas \n");

lista_dubplicada1 = [4,5,6,7];

lista_dubplicada2 = lista_dubplicada1;

print(f'O valor da lista lista_dubplicada1 = {lista_dubplicada1}');
print(f'O valor da lista lista_dubplicada2 = {lista_dubplicada2} \n');

lista_dubplicada2.append(10);

print(f'O valor da lista lista_dubplicada1 = {lista_dubplicada1}');
print(f'O valor da lista lista_dubplicada2 = {lista_dubplicada2}');


print("Para evitar isso basta fazer da seguinte forma lista_dubplicada2 = lista_dubplicada1[:] \n");


lista_dubplicada3 = lista_dubplicada1[:];

lista_dubplicada3.append(11);

print(f'O valor da lista lista_dubplicada1 = {lista_dubplicada1}');
print(f'O valor da lista lista_dubplicada2 = {lista_dubplicada2}');
print(f'O valor da lista lista_dubplicada3 = {lista_dubplicada3}');
