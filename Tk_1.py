from tkinter import *

azul = '#364a85'
vermelho = '#b53128'
verdelimao = '#19e04e'
preto = '#000000'
branco = '#ffffff'

root = Tk()
root.title('Color Changer')
root.geometry('500x400+200+200')
root.wm_resizable(width=False, height=False)
root.configure(bg=azul)

def bg_azul():
    root.configure(bg=azul)
    lb1 = Label(root, text='Azul', fg=branco, bg=azul, font='Time 20 bold')
    lb1.place(width=150, height=50, x=170, y=310)

def bg_vermelho():
    root.configure(bg=vermelho)
    lb1 = Label(root, text='Vermelho', fg=branco, bg=vermelho, font='Time 20 bold')
    lb1.place(width=150, height=50, x=170, y=310)

def bg_verde():
    root.configure(bg=verdelimao)
    lb1 = Label(root, text='Verde', fg=branco, bg=verdelimao, font='Time 20 bold')
    lb1.place(width=150, height=50, x=170, y=310)

def bg_preto():
    root.configure(bg=preto)
    lb1 = Label(root, text='Preto', fg=branco, bg=preto, font='Time 20 bold')
    lb1.place(width=150, height=50, x=170, y=310)

bt1 = Button(root, text='Azul', command=bg_azul, font='Time 20 bold')
bt1.place(width=150, height=80, x=80, y=50)

bt2 = Button(root, text='Vermelho', command=bg_vermelho, font='Time 20 bold')
bt2.place(width=150, height=80, x=260, y=50)

bt3 = Button(root, text='Verde', command=bg_verde, font='Time 20 bold')
bt3.place(width=150, height=80, x=80, y=180)

bt4 = Button(root, text='Preto', command=bg_preto, font='Time 20 bold')
bt4.place(width=150, height=80, x=260, y=180)

root.mainloop()