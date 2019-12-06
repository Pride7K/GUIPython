
pessoa = []

idade = []

altura = []

linha =[]


for i in range(0,5):
    idade.append(int(input("Digite a sua idade: ")));
    print("");
    altura.append(float(input("Digite a sua altura: ")));
    print("");
    linha.append(idade);
    linha.append(altura);
    pessoa.append(linha[:]);
    linha.clear();
    
pessoa[0].sort();

pessoa[1].sort();

pessoa[2].sort();

pessoa[3].sort();

pessoa[4].sort();


for i in pessoa:
    print(i);
    print("");
