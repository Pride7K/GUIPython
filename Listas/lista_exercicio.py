lista = []

continuar = "S";

valor = int;

while continuar == "S":
    valor = int(input("Digite um numero inteiro: "));
    print("");
    if valor in lista:
        print("Valor duplicado ! Não irei inserir na lista");
    else:
        lista.append(valor);
        continuar = (input("Deseja continuar? S/N \n"));
        continuar = continuar.upper();
        
print(sorted(lista));
