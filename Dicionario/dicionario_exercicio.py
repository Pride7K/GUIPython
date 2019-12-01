

aluno = {}

aluno["nome"] = input("Digite o seu nome: ");
print("");
aluno["media"] = int(input("Digite a sua média: "));
print("");
if(aluno["media"] >=7):
   aluno["situacao"] = "Aprovado"
else:
    aluno["situacao"] = "Reprovado"


print(f'O aluno {aluno["nome"]} com a média {aluno["media"]} foi {aluno["situacao"]} \n');
