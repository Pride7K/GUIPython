meses = []
media = 0;

for i in range(0,12):
    linha = []
    mes = input("Digite o mês: ");
    print("");
    temp = float(input("Digite a temperatura media do mês: "));
    print("");
    linha.append(mes);
    linha.append(temp);
    meses.append(linha);

for i in meses:
    media = media + i[1]


media = media /3

for i in meses:
    if i[1] >= media:
        print(f'Mês {i[0]} maior que a média anual de temperaturas');
