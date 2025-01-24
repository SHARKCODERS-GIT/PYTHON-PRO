from tkinter import *
from random import randint

# -------------------------------------------------------------

# cor

branco = '#ffffff'
preto = '#000000'
vermelho = '#b53128'


# -------------------------------------------------------------

jackpot = 1000

# tela
tela1 = Tk()
tela1.title('Roulette')
tela1.geometry('350x300+500+100')
tela1.wm_resizable(width=False, height=False)

# labels e entrys

lb_title = Label(tela1, text='Roulette Simulator', font='Time 20', bg=preto, fg=branco, anchor='w', padx=60)
lb_title.place(width=350, height=50, x=0, y=0, )

lb_jackpot = Label(tela1, text='Saldo: 1000 euros', font='Time 20', bg=preto, fg=branco, anchor='w', padx=10)
lb_jackpot.place(width=350, height=50, x=0, y=250, )

# -------------------------------------------------------------

# funções

def par():
    global jackpot
    roleta = randint(1,36)
    if roleta % 2 == 0:
        jackpot += 250
        texto = ('Saldo:',jackpot,'euros')
    else:
        jackpot -= 250
        texto = ('Saldo:',jackpot,'euros')

    lb_jackpot = Label(tela1, text=texto, font='Time 20', bg=preto, fg=branco, anchor='w', padx=10)
    lb_jackpot.place(width=350, height=50, x=0, y=250, )

    lb_num = Label(tela1, text=roleta, font='Time 20', anchor='w', padx=30)
    lb_num.place(width=90, height=50, x=130, y=120)

def impar():
    global jackpot
    roleta = randint(1,36)
    if roleta % 2 == 1:
        jackpot += 250
        texto = ('Saldo:',jackpot,'euros')
    else:
        jackpot -= 250
        texto = ('Saldo:',jackpot,'euros')

    lb_jackpot = Label(tela1, text=texto, font='Time 20', bg=preto, fg=branco, anchor='w', padx=10)
    lb_jackpot.place(width=350, height=50, x=0, y=250, )

    lb_num = Label(tela1, text=roleta, font='Time 20', anchor='w', padx=30)
    lb_num.place(width=90, height=50, x=130, y=120)

def r_vermelho():
    global jackpot
    roleta = randint(1,2)
    if roleta == 1:
        jackpot += 250
        texto = ('Saldo:',jackpot,'euros')
    else:
        jackpot -= 250
        texto = ('Saldo:',jackpot,'euros')

    lb_jackpot = Label(tela1, text=texto, font='Time 20', bg=preto, fg=branco, anchor='w', padx=10)
    lb_jackpot.place(width=350, height=50, x=0, y=250, )

def r_preto():
    global jackpot
    roleta = randint(1,2)
    if roleta == 2:
        jackpot += 250
        texto = ('Saldo:',jackpot,'euros')
    else:
        jackpot -= 250
        texto = ('Saldo:',jackpot,'euros')

    lb_jackpot = Label(tela1, text=texto, font='Time 20', bg=preto, fg=branco, anchor='w', padx=10)
    lb_jackpot.place(width=350, height=50, x=0, y=250, )


# -------------------------------------------------------------
# botões

b_par = Button(tela1, text='Par', command=par, font='Time 15 bold')
b_par.place(width=80, height=50, x=50, y=80)

b_impar = Button(tela1, text='Impar', command=impar, font='Time 15 bold')
b_impar.place(width=80, height=50, x=220, y=80)

b_vemelho = Button(tela1, text='V', command=r_vermelho, font='Time 15 bold', bg=vermelho)
b_vemelho.place(width=80, height=50, x=50, y=170)

b_preto = Button(tela1, text='P', command=r_preto, font='Time 15 bold', bg=preto, fg=branco)
b_preto.place(width=80, height=50, x=220, y=170)

# -------------------------------------------------------------
tela1.mainloop()