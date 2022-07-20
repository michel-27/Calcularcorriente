from tkinter import *

def resultado():
    I.set( float(R.get()) * float(V.get()) )
    borrar()

def borrar():
    R.set("")
    V.set("")

michel=Tk()
michel.title('Valor de corriente de un circuito')
michel.resizable(False, False)
michel.geometry("450x250")
#michel.configure(bg='blue')
miFrame= Frame()
miFrame.pack()
michel.config(bd=15)
bienvenido=Label(miFrame, text='BIENVENIDO')
bienvenido.grid(row=0, column=0)
bienvenido.config(font=('Arial', 16))

R = StringVar()
V = StringVar()
I = StringVar()
#--R--
Label(michel, text="Resistencia equivalente").pack()
Entry(michel, justify="center", textvariable=R).pack()
#--V--
Label(michel, text="Voltaje").pack()
Entry(michel, justify="center", textvariable=V).pack()
#--I--
Label(michel, text="Corriente").pack()
Entry(michel, justify="center", textvariable=I, state="disabled").pack()


Button(michel, text="Resultado", command=resultado).pack(side="left")

michel.mainloop()
