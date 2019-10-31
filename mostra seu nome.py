from tkinter import *
from functools import partial

janela = Tk();


def btn_clicou():
    lbl2["text"] = "Seu nome é ",input1.get();

janela.geometry("300x300");

janela.title("teste de aprendizado da biblioteca tkinter");

lbl1 = Label(janela,text="Digite seu nome ",width=20);
lbl1.place(x=22,y=50);

input1 = Entry(janela);
input1.place(x=50,y=100);

btn1 = Button(janela,text="Mostrar seu nome",width=20);
btn1["command"] = partial(btn_clicou);
btn1.place(x=50,y=150);

lbl2 = Label(janela,text="",width=20);
lbl2.place(x=25,y=200);



janela.mainloop();
