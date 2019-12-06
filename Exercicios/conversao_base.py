def binario(v1):
    lista = []
    while(v1 != 1 ):
        v1 = v1 / 2;
        v2 = v1 % 2;
        lista.append(v2);
        print(lista);
        
numero = float(input("Digite um numero: "));
print("");

print("Para converter em binário tecle 1 \n");

print("Para converter em octal tecle 2 \n");

print("Para converter em hexadecimal tecle 3 \n");

escolha = float(input("Por favor escolha . . . "));
print("");

if escolha == 1:
    binario(numero);
elif escolha == 2:
    binario(numero);
elif escolha ==3:
    binario(numero);
else:
    while(escolha <1 and escolha >3):
        print("Para converter em binário tecle 1 \n");
        print("Para converter em octal tecle 2 \n");
        print("Para converter em hexadecimal tecle 3 \n");
        escolha = float(input("Por favor escolha . . . "));
        print("");



