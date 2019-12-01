
dados = {"nome":"Guilherme","idade":18}

dados["nome"] = "Gui"

dados["sexo"] = "Masculino"

print(dados.values());

print(dados.keys());

print(dados.items());

print(dados);

print("");

for chave,valor in dados.items():
    print(f' {chave} {valor} \n');


matriz = []

matriz.append(dados);

print(matriz);

print(matriz[0]["nome"]);

print(matriz[0]["idade"]);


alunos = []

aluno = {}

for i in range(0,3):
    aluno["nome"] = input("Digite o seu nome: ");
    print("");
    aluno["idade"] = int(input("Digite a sua idade: "));
    print("");
    alunos.append(aluno.copy());

print(aluno)

for chave,valor in enumerate(alunos):
    print(f'O aluno {alunos[chave]["nome"]} tem {alunos[chave]["idade"]} anos \n');
