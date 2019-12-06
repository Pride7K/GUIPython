
string = input("Digite algo: ");
print("");
print(f'O tipo primitivo desse valor é {type(string)} \n');
if string == "":
    espaços = True
else:
    espaços = False
print(f'Só tem espaços {espaços} \n');

if string.isnumeric():
    numero = True
else:
    numero = False

print(f'É um número {numero} \n');
