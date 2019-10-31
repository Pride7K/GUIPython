from tkinter import *


janela = Tk();


janela.geometry("300x300");


lb = Label(janela,text="linha1",bg="green");
lb2 = Label(janela,text="linha1",bg="yellow");
lb3 = Label(janela,text="linha1",bg="blue");
lb4 = Label(janela,text="linha1",bg="black");

lb.pack(side="left",fill="both",expand=1);
lb2.pack(side="left",fill="both",expand=1);
lb3.pack(side="left",fill="both",expand=1);
lb4.pack(side="left",fill="both",expand=1);

janela.mainloop();
