
def calcular_prestacao(casa,salario,anos):
    salario_percent = (30/100) * salario;
    prestacao =  casa / (anos * 12);
    if prestacao > salario_percent:
        return "Empréstimo negado"
    else:
        return "Empréstimo permitido"


print(calcular_prestacao(80000,10000,7));
