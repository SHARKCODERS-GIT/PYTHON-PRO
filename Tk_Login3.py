from tkinter import *
from tkinter import messagebox
import csv

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

def tela_dash(texto):
    global tela_dash
    tela_dash = Tk()
    tela_dash.title('DASHBOARD AULAS')
    tela_dash.geometry('380x250+600+100')
    tela_dash.wm_resizable(width=False, height=False)

    lb_title = Label(tela_dash, text=texto, font='Time 20 bold', bg=azul, fg=branco, anchor='w', padx=30)
    lb_title.place(width=380, height=50, x=0, y=0, )

    b_logout = Button(tela_dash, text='Logout', command=tela_dash.destroy, font='Time 10 bold', bg=azul, fg=branco)
    b_logout.place(width=80, height=30, x=150, y=170)


def tela_cadastro():

    tela_cadastro = Tk()
    tela_cadastro.title('CADASTRO DE ALUNO')
    tela_cadastro.geometry('380x250+400+50')
    tela_cadastro.wm_resizable(width=False, height=False)

    lb_nome = Label(tela_cadastro, text='Nome *', font='Time 10', anchor='w')
    lb_nome.place(width=60, height=20, x=10, y=30)
    input_nome = Entry(tela_cadastro, font='Time 10')
    input_nome.place(width=250, height=20, x=100, y=30)

    lb_login_new = Label(tela_cadastro, text='Login *', font='Time 10', anchor='w')
    lb_login_new.place(width=60, height=20, x=10, y=70)
    input_login_new = Entry(tela_cadastro, font='Time 10')
    input_login_new.place(width=250, height=20, x=100, y=70)

    lb_senha_new = Label(tela_cadastro, text='Senha *', font='Time 10', anchor='w')
    lb_senha_new.place(width=60, height=20, x=10, y=110)
    input_senha_new = Entry(tela_cadastro, font='Time 10', show='*')
    input_senha_new.place(width=250, height=20, x=100, y=110)

    def cadastrar():
        nome = input_nome.get()
        login = input_login_new.get()
        senha = input_senha_new.get()
        if nome == '' or login == '' or senha == '':
            messagebox.showwarning('Error', 'Entradas Obrigatórias')
        else:
            with open('Cadastro.csv', 'a', encoding='utf-8',newline='') as arquivo:
                editar_csv = csv.writer(arquivo)
                data = [nome,login,senha]
                editar_csv.writerow(data)
                messagebox.showinfo('Sucess', 'Cadastro realizado com sucesso')
                tela_cadastro.destroy()

    b_logout = Button(tela_cadastro, text='Cadastrar', command=cadastrar, font='Time 10 bold', bg=azul, fg=branco)
    b_logout.place(width=80, height=30, x=150, y=170)


def login():

    login = input_login.get()
    senha = input_senha.get()

    if login == '' or senha == '':
        messagebox.showwarning('Error', 'Entradas Obrigatórias')
    else:
        with open('Cadastro.csv', 'r', encoding='utf-8') as arquivo:
            leitor_csv = csv.reader(arquivo)
            for linha in leitor_csv:
                if login in linha:
                    if linha[2] == senha:
                        messagebox.showinfo('SHARCKCODERS Python PRO II', 'Seja bem vindo')
                        tela1.destroy()
                        texto = (f'Bem vindo {linha[0]}')
                        tela_dash(texto)
                    else:
                        messagebox.showerror('SHARCKCODERS Python PRO II', 'Verifique o Login e Senha')


# -------------------------------------------------------------
# botões

b_login = Button(tela1, text='Submeter', command=login, font='Time 10 bold', bg=azul, fg=branco)
b_login.place(width=80, height=30, x=200, y=170)

b_cadastro = Button(tela1, text='Cadastrar', command=tela_cadastro, font='Time 10 bold', bg=azul, fg=branco)
b_cadastro.place(width=80, height=30, x=100, y=170)

# -------------------------------------------------------------
tela1.mainloop()