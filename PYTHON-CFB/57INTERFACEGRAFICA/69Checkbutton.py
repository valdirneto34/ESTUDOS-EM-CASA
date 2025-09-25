from tkinter import *


def futebolClicado():
    print(f"Futebol:{vfutebol.get()}")


def voleiClicado():
    print(f"Vôlei:{vvolei.get()}")


def basqueteClicado():
    print(f"Basquete:{vbasquete.get()}")


app = Tk()
app.title("CFB Cursos")
app.geometry("500x300")

vfutebol = IntVar()
vvolei = IntVar()
vbasquete = IntVar()

fr_quadro1 = Frame(app, borderwidth=1, relief="solid")
fr_quadro1.place(x=10, y=10, width=300, height=100)

cb_futebol = Checkbutton(fr_quadro1, text="Futebol", variable=vfutebol,
                         onvalue=1, offvalue=0, command=futebolClicado)
cb_futebol.pack(side=LEFT)

cb_volei = Checkbutton(fr_quadro1, text="Vôlei", variable=vvolei,
                       onvalue=1, offvalue=0, command=voleiClicado)
cb_volei.pack(side=LEFT)

cb_basquete = Checkbutton(fr_quadro1, text="Basquete", variable=vbasquete,
                          onvalue=1, offvalue=0, command=basqueteClicado)
cb_basquete.pack(side=LEFT)

app.mainloop()
