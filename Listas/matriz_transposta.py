

matriz = []

nr_linhas = int(input("Digite quantas linhas tera a sua matriz: "));

nr_colunas =int(input("Digite quantas colunas tera a sua matriz: "));



for i in range(nr_linhas):
    linha = []
    for j in range(nr_colunas):
        valor = float(input(f'Digite o valor da linha {i} e coluna {j}: '));
        print("");
        linha.append(valor);
        
    matriz.append(linha[:]);






matriz_transposta = []

for i in  range(nr_colunas):
    coluna_t = []
    for j in   range (nr_linhas):
        coluna_t.append(matriz[j][i]);
    print(coluna_t);
    matriz_transposta.append(coluna_t);


