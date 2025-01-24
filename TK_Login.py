from tkinter import *
from tkinter import messagebox


# -------------------------------------------------------------

# cor

branco = '#ffffff'
azul = '#364a85'
vermelho = '#b53128'
amarelo = '#ffef08'
verdelimao = '#19e04e'


# -------------------------------------------------------------

# tela
tela1 = Tk()
tela1.title('SHARCKCODERS Python PRO II')
tela1.geometry('380x250+500+100')
tela1.wm_resizable(width=False, height=False)

# labels e entrys

lb_title = Label(tela1, text='Dashboard do Aluno', font='Time 20 bold', bg=azul, fg=branco, anchor='w', padx=50)
lb_title.place(width=380, height=50, x=0, y=0, )

lb_login = Label(tela1, text='Login *', font='Time 10', anchor='w')
lb_login.place(width=60, height=20, x=10, y=70)
input_login = Entry(tela1, font='Time 10')
input_login.place(width=250, height=20, x=100, y=70)

lb_senha = Label(tela1, text='Senha *', font='Time 10', anchor='w')
lb_senha.place(width=60, height=20, x=10, y=110)
input_senha = Entry(tela1, font='Time 10',show='*')
input_senha.place(width=250, height=20, x=100, y=110)

# -------------------------------------------------------------

# funções

def procurar():

    login = input_login.get()
    senha = input_senha.get()

    if login == 'admin' and senha == 'admin':
        messagebox.showinfo('SHARCKCODERS Python PRO II', 'Seja bem vindo')
    else:
        messagebox.showerror('SHARCKCODERS Python PRO II', 'Verifique o Login e Senha')


# -------------------------------------------------------------
# botões

b_procurar = Button(tela1, text='Submeter', command=procurar, font='Time 10 bold', bg=azul, fg=branco)
b_procurar.place(width=80, height=30, x=150, y=170)

# -------------------------------------------------------------
tela1.mainloop()