contador = 0;

print("Checando se uma expressão é valida através dos parenteses \n");

expressao = input("Digite a expressão: ");

print("");

for i in expressao:
    if i == "(" or i == ")":
        contador = contador + 1
        
contador = contador % 2

if contador == 0:
    print("Expressão valida !");
else:
    print("Expressão invalida !");
