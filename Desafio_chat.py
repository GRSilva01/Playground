import tkinter as tk

Numero = 0

def acrecentar():
    global Numero
    Numero +=1
    Frase.config(text=str(Numero))

def reset():
    global Numero
    Numero = 0
    Frase.config(text=str(Numero))

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

botao_mais.pack(side=tk.LEFT, padx=50)


botao_reset = tk.Button (corpo_botao,
                        text="reset",
                        font=("Tahoma", 20),
                        bg="#b80000",
                        fg="white",
                        width=10,
                        command=reset)
botao_reset.pack(side=tk.LEFT, padx=50,)

j.mainloop()
