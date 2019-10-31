from tkinter import *
from functools import partial
def somar():
    try:
        v1 = float(input1.get());
        v2 = float(input2.get());
    except:
        if(input1.get() == "" or input2.get() == ""):
            lbl2["text"] = "Preencha todos os campos por favor !"
        else:
            lbl2["text"] = "Insira apenas números por favor !"
    else:
        lbl2["text"] = v1 + v2;

janela = Tk();

janela.geometry("300x300");

input1 = Entry(janela);
input2 = Entry(janela);

lbl1 = Label(janela,text="Aplicação para somar valores");

input1.insert(0,0);

input2.insert(0,0);

lbl1.place(x=50,y=50);

input1.place(x=50,y=100);

input2.place(x=50,y=130);

btn1=Button(janela,text="Somar",width=20);
btn1["command"] = somar;

btn1.place(x=50,y=160);

lbl2 = Label(janela,text="");
lbl2.place(x=50,y=200);

janela.mainloop();
