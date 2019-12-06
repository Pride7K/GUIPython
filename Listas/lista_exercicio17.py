
def maior_numero(lista):
    contador = 0;
    lista.sort();
    contador = len(lista);
    contador = contador -1;
    print(lista[contador]);

lista2 = [1,2,3,4,5,6,7,8,9]


maior_numero(lista2[:]);

def soma_lista(lista):
    contador = 0;
    for i in lista:
        contador = contador + i;
    print(contador);


soma_lista(lista2[:]);


    
def numero_vezes_primeroElemento(lista):
    contador = 0;
    for i in lista:
        if i == lista[0]:
            contador = contador + 1;
    print(contador);

numero_vezes_primeroElemento(lista2[:]);

def media(lista):
    contador = 0;
    tamanho = len(lista);
    for i in lista:
        contador = contador + i
    print(int((contador / tamanho)));

media(lista2[:]);


lista3 = [1,2,3,4,5,6,7,8,9]

def iguais(lista,lista2):
    return lista==lista2

print(iguais(lista2,lista3))
