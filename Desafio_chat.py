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

corpo_botao = tk.Frame(j
                )
corpo_botao.pack(expand=True)


botao_mais = tk.Button (corpo_botao,
                        text="+1",
                        bg="#098c00"
)
botao_mais.pack(expand=True)


botao_reset = tk.Button (corpo_botao,
                        text="reset",
                        bg="#b80000"
)
botao_reset.pack(expand=True)

j.mainloop()
