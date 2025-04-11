import tkinter as tk  


bg_color = "#F0F0F5"
header_color = "#282C34"
text_color = "#FFFFFF"
button_color = "#4CAF50"
button_hover = "#45A049"


def on_enter(e):
    e.widget.config(bg=button_hover)

def on_leave(e):
    e.widget.config(bg=button_color)


root = tk.Tk()
root.title("Minha Janela")
root.geometry("1150x750")
root.configure(bg=bg_color)

Largura = 1150
altura = 750
x = (root.winfo_screenwidth() // 2) - (Largura // 2)
y = (root.winfo_screenheight() // 2) - (altura // 2)
root.geometry(f"{Largura}x{altura}+{x}+{y}")

root.attributes("-alpha", 0.95)

header = tk.Frame(root, bg=header_color, height=60)
header.pack(fill="x")


Frase = tk.Label(header,
                 text="Aprendendo Tkinter!",
                 font=("Tahoma", 18,),
                 fg=text_color,
                 bg=header_color,
                 padx=30,
                 anchor="c")
Frase.pack(fill="both", expand=True)

body = tk.Frame(root, bg=bg_color)
body.pack(expand=True)


botao = tk.Button(body,
                  text="Clique!",
                  font=("Tahoma", 14),
                  bg=button_color,
                  fg="white",
                  relief="flat",
                  padx=20,
                  pady=10)
botao.pack(pady=30)
botao.bind("<Enter>", on_enter)
botao.bind("<Leave>", on_leave)

rodape = tk.Frame(root, bg=header_color, height=30)
rodape.pack(fill="x", side="bottom")

tk.Label(rodape, 
         text="teste!", 
         bg=header_color, 
         fg=text_color, 
         font=("Tahoma", 10))

root.mainloop()
