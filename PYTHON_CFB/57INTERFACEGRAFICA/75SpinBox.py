from tkinter import *

def impVal():
    print(f"Valor: {sp_valores.get()}")

app = Tk()
app.title("CFB Cursos")
app.geometry("500x300")

# sp_valores=Spinbox(app,from_=0,to=10)
sp_valores = Spinbox(app, values=(1, 2, 3, 4, 5))
sp_valores.pack()

btn_valor=Button(app,text="Imprimir valor",command=impVal)
btn_valor.pack()

app.mainloop()
