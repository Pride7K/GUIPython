from datetime import datetime

pessoa = {}

now = datetime.now();

now = now.year

pessoa["nome"] = input("Digite o seu nome: ");
pessoa["ano de nascimento"] = int(input("Digite o seu ano de nascimento: "));
pessoa["cdt"] = int(input("Digite o sua carteira de trabalho(caso nao tenha digite 0): "));

if(pessoa["cdt"] !=0):
    pessoa["ano_contrato"] = int(input("Digite o ano de sua contratação: "));
    pessoa["salario"] = int(input("Digite o seu salario: "));
    pessoa["aposentar"] = pessoa["ano_contrato"] + 35;
    
    print("");
    print(f'O seu nome é {pessoa["nome"]} \n');
    print(f'A sua idade é {now  - pessoa["ano de nascimento"]} \n');
    print(f'A sua carteira de trabalho é {pessoa["cdt"]} \n');
    print(f'A sua contratação foi em {pessoa["ano_contrato"]} \n');
    print(f'O seu salario é {pessoa["salario"]} \n');
    print(f'O Você ira se aposentar em {pessoa["aposentar"]} \n');
else:
    print(f'O seu nome é {pessoa["nome"]} \n');
    print(f'A sua idade é {now  - pessoa["ano de nascimento"]} \n');
