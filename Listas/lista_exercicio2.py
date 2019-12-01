lista = []
valor = int;
valor_check = 0;
print("Ordenando uma lista sem o sort \n");

for c in range(0,5):
    valor = int(input("Digite um valor inteiro: "));
    print("");
    if(c == 0):
        lista.append(valor);
    else:
        for i in lista:
            if(valor >i):
                z = lista.index(i);
                validador = True;
        if(validador == True):
            lista.insert(z + 1 ,valor);
        else:
            lista.insert(0,valor);
        validador = False
        
print(f'A lista é {lista}');
