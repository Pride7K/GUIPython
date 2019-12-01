dados = ["Guilherme",18]

pessoas = list();

pessoas.append(dados[:]);

dados = ["Guila",19]

pessoas.append(dados[:]);

dados = ["Guefa",20];

pessoas.append(dados[:]);

print(pessoas[0][0]);

print(pessoas[2]);

print(pessoas[1][1]);

pessoas2 = [["teste",1],["teste",2],["teste",3],["teste",4]]

print(pessoas2);

print(pessoas2[3][1]);

for i in pessoas2:
    print(i);

for i in pessoas2:
    for j in pessoas2:
        print(pessoas2[i][j]);
