print("Programa com o intuito de ler varios numeros, mostra-los em ordem decrescente, quantos numeros eu digitei e se o numero 5 foi digitado \n");


lista = []
y = 0;
continuar = "N";

while continuar == "N":
    valor = int(input("Digite um numero: "));
    print("");
    if(len(lista) == 0):
        lista.append(valor);
    else:
        for i in lista:
            if(valor > i):
               y++;
        validador = False
    continuar = str(input("Deseja sair ? S/N \n "));
    continuar = continuar.upper();
                    
                     
print(f'Você digitou {len(lista)} números');

print(f' Os numeros que você digitou em ordem decrescente {lista}');

if 5 in lista:
    print("O número 5 está presente na lista");
else:
    print("O número 5 não está presente na lista");
