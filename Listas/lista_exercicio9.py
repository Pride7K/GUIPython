

vetor = input("Digite uma palavra de até 10 letras: ");

if(len(vetor) > 10):
    while(len(vetor) > 10):
        vetor = input("Digite uma palavra de até 10 letras: ");

consoantes = 0;

for i in vetor:
    print(i)
    if i != "a" and i != "e" and  i != "i" and  i != "o" and  i != "u" :
        consoantes += 1

print(f'Na palavra {vetor} há {consoantes} consoantes');
        
