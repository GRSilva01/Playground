import tkinter as tk

Numero = 0

def acrecentar(e):
    e.widget.config(Numero + 1)

def reset(e):
    e.widget.config(Numero = 0)
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

contagem = str(Numero)
Frase = tk.Label(j,
                 text=contagem,
                 font=("Tahoma", 18,),
                 padx=30,
                 anchor="c")
Frase.pack(fill="both", expand=True)

corpo_botao = tk.Frame(j
                )
corpo_botao.pack(pady=355)


botao_mais = tk.Button (corpo_botao,
                        text="+1",
                        bg="#098c00"
)
botao_mais.pack(side=tk.RIGHT, padx=(50, 0))


botao_reset = tk.Button (corpo_botao,
                        text="reset",
                        padx=50,
                        pady=100,
                        bg="#b80000"
)
botao_reset.pack(side=tk.LEFT, padx=(50, 0))

j.mainloop()
