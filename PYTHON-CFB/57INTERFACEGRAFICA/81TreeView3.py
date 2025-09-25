from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def inserir():
    if vid.get() == "" or vnome.get() == "" or vfone.get() == "":
        messagebox.showinfo(title="ERRO", message="Digite todos os dados!")
        return
    tv.insert("", "end", values=(vid.get(), vnome.get(), vfone.get()))
    vid.delete(0, END)
    vnome.delete(0, END)
    vfone.delete(0, END)
    vid.focus()


def deletar():
    try:
        itemSelecionado = tv.selection()[0]
        tv.delete(itemSelecionado)
    except:
        messagebox.showinfo(
            title="ERRO", message="Selecione um elemento a ser deletado!")


def obter():
    try:
        itemSelecionado = tv.selection()[0]
        valores = tv.item(itemSelecionado, "values")
        print(f'ID......: {valores[0]}')
        print(f'Nome....: {valores[1]}')
        print(f'Telefone: {valores[2]}')
    except:
        messagebox.showinfo(
            title="ERRO", message="Selecione um elemento a ser obtido!")


app = Tk()
app.title("CFB Cursos")
app.geometry("550x350")

lbid = Label(app, text="ID")  # , anchor=W
vid = Entry(app)

lbnome = Label(app, text="Nome")  # , anchor=W
vnome = Entry(app)

lbfone = Label(app, text="Telefone")  # , anchor=W
vfone = Entry(app)


tv = ttk.Treeview(app, columns=('id', 'nome', 'fone'), show='headings')
tv.column('id', minwidth=0, width=50)
tv.column('nome', minwidth=0, width=250)
tv.column('fone', minwidth=0, width=100)
tv.heading('id', text='ID')
tv.heading('nome', text='NOME')
tv.heading('fone', text='TELEFONE')

btn_inserir = Button(app, text="Inserir", command=inserir)
btn_deletar = Button(app, text="Deletar", command=deletar)
btn_obter = Button(app, text="Obter", command=obter)

lbid.grid(column=0, row=0, sticky='w')
vid.grid(column=0, row=1)
lbnome.grid(column=1, row=0, sticky='w')
vnome.grid(column=1, row=1)
lbfone.grid(column=2, row=0, sticky='w')
vfone.grid(column=2, row=1, sticky='w')

tv.grid(column=0, row=3, columnspan=3, pady=5)

btn_inserir.grid(column=0, row=4)
btn_deletar.grid(column=1, row=4)
btn_obter.grid(column=2, row=4)

# tv.insert("", "end", values=(i, n, f))


app.mainloop()
