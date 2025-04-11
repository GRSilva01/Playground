import tkinter as tk  

root = tk.Tk()
root.title("Teste do Botao")
root.geometry("400x200")

def acao_botao():
    mensagem.config(text="Você clicou no botão!")

def reset():
    mensagem.config(text="Botao no Tkinter!")

mensagem = tk.Label(root,
                 text="Botao no Tkinter!",
                 font=("Tahoma", 18),
                 fg="red",
                 anchor="c")
mensagem.pack(fill="x")

botao = tk.Button(root, text="Aperte-me!", command=acao_botao)
botao.pack(pady=20)

otherbutton = tk.Button(root, text="reset!", command=reset)
otherbutton.pack(pady=20)

root.mainloop()
