import tkinter as tk



def enviar():
    entrada_usuario = campo_input.get()
    if not entrada_usuario.strip():
        return

    # Simulação de resposta (só enquanto a GAIA não tá ligada)
    resposta_fake = "A resposta da GAIA vai aparecer aqui..."
    campo_chat.insert(tk.END, f"Você: {entrada_usuario}\nGAIA: {resposta_fake}\n\n")
    campo_input.delete(0, tk.END)

# Criar a janela principal
janela = tk.Tk()
janela.title("GAIA - Interface")
janela.geometry("600x400")
janela.resizable(False, False)

# Corrigir aqui
mic_img = tk.PhotoImage(file="MIC.png").subsample(15, 15)

# Área de chat (Text)
campo_chat = tk.Text(janela, height=20, width=70, wrap="word")
campo_chat.pack(padx=10, pady=10)

# Frame para input e botão
frame_input = tk.Frame(janela)
frame_input.pack(padx=10, pady=10, fill="x")

# Campo de entrada (Entry)
campo_input = tk.Entry(frame_input, width=50)
campo_input.pack(side=tk.LEFT, expand=True, fill="x")

# Botão de enviar
botao_enviar = tk.Button(frame_input, text="Enviar", command=enviar)
botao_enviar.pack(side=tk.LEFT, padx=(10, 0))

# Botão com imagem (microfone)
botao_falar = tk.Button(frame_input, image=mic_img, command=enviar)
botao_falar.image = mic_img  # manter referência pra não ser deletado
botao_falar.pack(side=tk.LEFT, padx=(10, 0))

# Rodar a interface
janela.mainloop()
