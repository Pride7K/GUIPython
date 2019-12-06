perguntas = []
contador = 0;

pergunta = input("Telefonou para a vitima?: S/N");
print("")
perguntas.append(pergunta.upper());
pergunta = input("Esteve no local do crime?: S/N");
print("")
perguntas.append(pergunta.upper());
pergunta = input("Mora perto da vítima?: S/N");
print("")
perguntas.append(pergunta.upper());
pergunta = input("Devia para a vítima?: S/N");
print("")
perguntas.append(pergunta.upper());
pergunta = input("Já trabalhou com a vítima?: S/N");
print("")
perguntas.append(pergunta.upper());


for i in perguntas:
    
    if(i=="S"):
        contador = contador + 1;


if(contador==2):
    print("Você é suspeito do crime!\n");
elif(contador>=3 and contador<=4):
    print("Você é suspeito de ser cumplice do crime!\n");
elif(contador == 5):
    print("Você é o assassino do crime!\n");
else:
    print("Você é inocente!\n");
