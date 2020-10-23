from tkinter import *
import re


janela = Tk()

janela.title("Hotel HOTEL")

windowWidth = janela.winfo_reqwidth()
windowHeight = janela.winfo_reqheight()
positionRight = int(janela.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(janela.winfo_screenheight()/2 - windowHeight/2)

# janela.geometry('350x400+0+0')

janela.geometry("350x320+{}+{}".format(positionRight, positionDown))

lbl = Label(janela, text="Bem vindo ao hotel",fg="black",font=('Arial',15))
lbl.place(x=100,y=0)

lbl1 = Label(janela, text="Entre com as reservas antecipadas!",fg="black",font=('Arial',14))
lbl1.place(x=20,y=25)

lbl2 = Label(janela, text="Dias(ex:1-2,3-5):")
lbl2.place(x=0,y=75)

inputEntrada = Entry(janela,width=30)
inputEntrada.place(x=100,y=75)

resultadoLabel = Label(janela, text="Resultado")
resultadoLabel.place(x=0,y=145)





def clicked():
    erro="""Entrada inválida {}
formato válido ex:1-6,3-6
tente novamente"""
    alerta = 0
    valorEntrada = inputEntrada.get()

    try:
        valorEntrada = valorEntrada.split(',')
        entrada = []
        for i in valorEntrada:
            if not re.match("[0-9]+-[0-9]+",i):
                print("erro: ",i)
                erro = erro.format(i)
                alerta=1
                break
            b = i.split('-')
            entrada.append((int(b[0]),int(b[1])))
        print(entrada)
    except:
        erro=erro
        alerta = 1
    
    # print(valorEntrada)
    texto = ""
    
    if(alerta!=0):
        texto = erro
    else:
        # Chamar funções e pegar os resutados
        texto = "Numero de quartos suficiente"
    
    

    
    caixaTexto = Text(janela, height=10,width=50)
    caixaTexto.insert(END,texto)
    caixaTexto.place(x=0, y=160)


btn = Button(janela, text="Analisar", command=clicked)

btn.place(x=100,y=110)

janela.mainloop()