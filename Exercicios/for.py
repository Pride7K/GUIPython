contador = 0;

for i in range(1,500):
    validador = 0;
    validador2 = 0;
    validador = i % 3;
    validador2 = i % 2;
    if validador == 0:
        if validador2 != 0:
            contador = contador + i;


print(contador);
