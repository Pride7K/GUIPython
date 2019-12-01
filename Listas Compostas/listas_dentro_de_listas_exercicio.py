
pessoa = list()

pessoas_final = []

continuar = "S"

contador = 0;

pesadas = 0;

pessoa_mais_pesada = []

pessoa_mais_leve = []

leves = 0;

while continuar == "S":
    pessoa.append(input("Digite o seu nome: "));
    print("");
    pessoa.append(float(input("Digite o seu peso: ")));
    print("");
    pessoas_final.append(pessoa[:]);
    pessoa.clear();
    continuar = input("Deseja continuar ? S/N ");
    continuar = continuar.upper();
    print("");
    contador += 1;

print(f'{contador} pessoas foram cadastradas ! \n');

for j in pessoas_final:
    if pesadas == 0:
        pesadas = j[1];
    else:
        if j[1] > pesadas:
            pesadas = j[1]
    if leves == 0:
        leves = j[1];
    else:
        if j[1] < leves:
            leves = j[1]

for j in pessoas_final:
    if pesadas == j[1]:
        pessoa_mais_pesada.append(j[0]);
    if leves == j[1]:
        pessoa_mais_leve.append(j[0]);


print(f'O maior peso registrado foi de {pesadas}. As pessoas com este peso são {pessoa_mais_pesada}\n');

print(f'O menor peso registrado foi de {leves}. As pessoas com este peso são {pessoa_mais_leve} \n');



