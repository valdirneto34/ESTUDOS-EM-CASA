from tkinter import *


def valorEscala():
    print(f"Valor da escala: {sc_escala.get()}")


def defiEscala():
    vesc = num_escala.get()
    sc_escala.set(vesc)


app = Tk()
app.title("CFB Cursos")
app.geometry("500x300")

lb_valor = Label(app, text="Valor", bg="#dde", fg="#009")
lb_valor.pack()

sc_escala = Scale(app, from_=0, to=100, orient=HORIZONTAL)
sc_escala.set(50)
sc_escala.pack()

btn_valor = Button(app, text="Valor Escala", bg="#dde",
                   fg="#009", command=valorEscala)
btn_valor.pack()

definirEscala = Label(app, text="Defina Nova Escala:",
                      bg="#dde", fg="#009",).pack()
num_escala = Entry(app)
num_escala.pack()

btn_definir = Button(
    app, text="Setar Novo Valor da Escala", bg="#dde", fg="#009", command=defiEscala)
btn_definir.pack()

app.mainloop()
