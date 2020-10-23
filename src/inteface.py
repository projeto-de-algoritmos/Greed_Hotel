from bookings import possiveisHorarios, quartosNecessarios, tratarDados
from tkinter import *

janela = Tk()

janela.title("Bem vindo ao Greed app")

windowWidth = janela.winfo_reqwidth()
windowHeight = janela.winfo_reqheight()
positionRight = int(janela.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(janela.winfo_screenheight()/2 - windowHeight/2)

# janela.geometry('350x400+0+0')

janela.geometry("450x465+{}+{}".format(positionRight, positionDown))

lbl = Label(janela, text="Bem vindo ao hotel",fg="black",font=('Arial',15))
lbl.place(x=140,y=0)

lbl1 = Label(janela, text="Entre com as reservas antecipadas!",fg="black",font=('Arial',13))
lbl1.place(x=80,y=25)


lbl2 = Label(janela, text="Dias (ex:1-2,3-5):", font=('Arial',11))
lbl2.place(x=10,y=53)

inputEntrada = Entry(janela,width=52)
inputEntrada.place(x=10,y=78)

resultadoLabel = Label(janela, text="Resultado",fg="black",font=('Arial',14))
resultadoLabel.place(x=10,y=160)
resultadoLabel.configure(background='blue')


caixaTexto = Text(janela, height=14,width=53, fg="white")
# caixaTexto.insert(END,texto)
caixaTexto.place(x=10, y=190)
# caixaTexto.configure(background='black')

def clicked():
    valorEntrada = inputEntrada.get()
    try:
        valorEntrada = valorEntrada.split(',')
    except:
        print("error")
    
    print(valorEntrada)

    # -------------------------------------------------
    #   Entrada para teste
    # 1-4, 3-5, 0-6, 5-7, 6-9, 5-9, 7-10, 8-11, 11-12, 2-14, 13-16
    # -------------------------------------------------
    texto = tratarDados(valorEntrada)
    # texto = "O numero de quartos ideal é: "
    # texto = "Não há quartos suficientes...."
    # -------------------------------------------------
    
    caixaTexto = Text(janela, height=14,width=53, fg="black")
    caixaTexto.insert(END,texto)
    caixaTexto.place(x=10, y=190)
    caixaTexto.configure(font=('Arial',11))


# -------------------------------------------------------------
btn = Button(janela, text="Verificar disponibilidade", command=clicked, fg="black",font=('Arial',11))
# btn.configure(background='blue')
# -------------------------------------------------------------

btn.place(x=100,y=105)

janela.mainloop()