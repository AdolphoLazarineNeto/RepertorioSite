import tkinter as tk
from tkinter import messagebox

def verificar_resposta():
    resposta = entry.get().lower()
    if resposta == "y":
        messagebox.showinfo("Resposta", "Parabéns, você fez a escolha certa! Estou ansioso para trabalhar na sua equipe!\nEnvie-me um e-mail em adolpholneto@hotmail.com para conversarmos.")
    elif resposta == "n":
        messagebox.showinfo("Resposta", "Resposta errada, me dê uma chance de mostrar meu valor. Não vou te decepcionar.")
    else:
        messagebox.showerror("Opção inválida", "Opção inválida. Por favor, responda com 'y'.")

# Configurações da janela principal
root = tk.Tk()
root.title("Questionário para Contratação")

# Texto explicativo
label = tk.Label(root, text="Você está pronto para ter o melhor desenvolvedor da sua empresa, mais dedicado, pontual e onde quer viver disto? (y/n)")
label.pack()

# Entrada de texto
entry = tk.Entry(root)
entry.pack()

# Botão de verificação
button = tk.Button(root, text="Verificar", command=verificar_resposta)
button.pack()

# Rodar o loop da aplicação
root.mainloop()
