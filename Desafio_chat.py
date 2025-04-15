import tkinter as tk

Numero = 0

#----------------------------------------------------------------------------
def acrecentar():
    global Numero
    Numero +=1
    Frase.config(text=str(Numero))

def diminuir():
    global Numero
    if Numero > 0:
        Numero -=1
        Frase.config(text=str(Numero))
    else:
        Frase.config(text="Não é possivel diminuir!")

def setar():
    global Numero
    try:
        Palavra = int(receber.get())
        if Palavra >=0:
            Numero = Palavra
            Frase.config(text=str(Numero))
        else:
            Frase.config(text="Valor negativo não permitidor!")
    except ValueError:
        Frase.config(text="Digite um número válido!")

def reset():
    global Numero
    Numero = 0
    Frase.config(text=str(Numero))

def upgrade_10():
    global Numero
    Numero +=1
    Frase.config(text=str(Numero))
    j.after(1, upgrade_10)

def upgrade_100():
    global Numero
    Numero +=10
    Frase.config(text=str(Numero))
    j.after(1, upgrade_100)

def b_upgrade_10():
    global Numero
    if Numero >= 10:
        Numero -=10
        upgrade_10()
        Frase.config(text=str(Numero))
    else:
        Frase.config(text="Valor insuficiente!")

def b_upgrade_100():
    global Numero
    if Numero >= 100:
        Numero -=100
        upgrade_100()
        Frase.config(text=str(Numero))
    else:
        Frase.config(text="Valor insuficiente!")
#-----------------------funções---------------------------------------------

#Codigo cria uma janela com um "mini jogo" clicker, fiz como um desafio do ChatGPT para aprender mais sobre Tkinter

#--------------------------------------------------------------------------
j = tk.Tk()
j.title("Minha Janela")
j.geometry("1150x750")
j.configure(bg="#FFFFFF")

Largura = 1150
altura = 750
x = (j.winfo_screenwidth() // 2) - (Largura // 2)
y = (j.winfo_screenheight() // 2) - (altura // 2)
j.geometry(f"{Largura}x{altura}+{x}+{y}")
j.attributes("-alpha", 0.95)
#--------------------------CABEÇALHO--------------------------------------

Frase = tk.Label(j,
                 text=str(Numero),
                 font=("Tahoma", 20,),
                 padx=30,
                 pady=30,
                 anchor="c",
                 bg="#FFFFFF")
Frase.pack(fill="both", expand=True)

corpo_botao = tk.Frame(j, bg="#FFFFFF")
corpo_botao.pack(pady=50)


botao_mais = tk.Button (corpo_botao,
                        text="+1",
                        font=("Tahoma", 20),
                        bg="#098c00",
                        fg="white",
                        width=10,
                        command=acrecentar)

botao_mais.pack(side=tk.LEFT, padx=10)

botao_menos = tk.Button (corpo_botao,
                        text="-1",
                        font=("Tahoma", 20),
                        bg="#3967db",
                        fg="white",
                        width=10,
                        command=diminuir)

botao_menos.pack(side=tk.LEFT, padx=10)


botao_reset = tk.Button (corpo_botao,
                        text="reset",
                        font=("Tahoma", 20),
                        bg="#b80000",
                        fg="white",
                        width=10,
                        command=reset)
botao_reset.pack(side=tk.LEFT, padx=10)

botao_setar = tk.Button (corpo_botao,
                       text="set",
                       font=("Tahoma", 20),
                       bg="#F01F01",
                       fg="white",
                       width=10,
                       command=setar)
botao_setar.pack(side=tk.LEFT, padx=10)

botao_upgrade = tk.Button (corpo_botao,
                       text="up +10",
                       font=("Tahoma", 20),
                       bg="#F01F01",
                       fg="white",
                       width=10,
                       command=b_upgrade_10)
botao_upgrade.pack(side=tk.LEFT, padx=10)

botao_upgrade_100 = tk.Button (corpo_botao,
                       text="up +100",
                       font=("Tahoma", 20),
                       bg="#F01F01",
                       fg="white",
                       width=10,
                       command=b_upgrade_100)
botao_upgrade_100.pack(side=tk.LEFT, padx=10)

receber = tk.Entry(j)
receber.pack(pady=10)

j.mainloop()
