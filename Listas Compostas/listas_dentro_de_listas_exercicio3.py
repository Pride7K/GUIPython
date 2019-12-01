print("Versão aprimorada do exercicio anterior, mostrando agora a soma dos numeros pares, a soma dos numeros da terceira coluna  e o maior valor da segunda linha");


matriz = []
par= float;

soma_dos_pares = 0;

soma_da_terceira_coluna = 0;

maior_valor_segunda_linha = list ();


for i in range(0,3):
    linhas = []
    for j in range(0,3):
        valor = int(input("Digite um numero: "));
        print("");
        par = valor % 2;
        if(par == 0):
            soma_dos_pares += valor
        if(j == 2):
            soma_da_terceira_coluna += valor;
        linhas.append(valor);
    matriz.append(linhas[:]);


print(f'A soma dos numeros pares digitados é de {soma_dos_pares} \n');

print(f'A soma dos numeros da terceira coluna é de {soma_da_terceira_coluna} \n');

maior_valor_segunda_linha.append(matriz[:]);

maior_valor_segunda_linha[0][1].sort();

print(f'o maior valor da segunda linha é de {maior_valor_segunda_linha[0][1][2]}');
