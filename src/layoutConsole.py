import tkinter
import tkinter as tk
from tkinter import messagebox

def limpar_arquivos_temporarios():
    messagebox.showinfo("Limpar Arquivos Temporários", "Executando a limpeza de arquivos temporários...")

def limpar_disco():
    messagebox.showinfo("Limpar Disco", "Executando a limpeza do disco...")

def limpar_pastas():
    messagebox.showinfo("Limpar Pastas", "Executando a limpeza de pastas...")

def esvaziar_lixeira():
    messagebox.showinfo("Esvaziar Lixeira", "Esvaziando a lixeira...")

def ver_ipv4():
    messagebox.showinfo("Ver IPv4", "Exibindo o endereço IPv4...")

def sair():
    window.destroy()  # WINDOW NAO TA SENDO DEFINIDO DEFINA

def layout():
    window = tk.Tk()
    window.title("Opções de Limpeza")
    
    label = tk.Label(window, text="Selecione uma opção:", font=("Arial", 12))
    label.pack()

    options = [
        ("Limpar Arquivos Temporários", limpar_arquivos_temporarios),
        ("Limpar Disco", limpar_disco),
        ("Limpar Pastas", limpar_pastas),
        ("Esvaziar Lixeira", esvaziar_lixeira),
        ("Ver IPv4", ver_ipv4),
        ("Sair", sair)
    ]

    for text, command in options:
        button = tk.Button(window, text=text, width=30, command=command)
        button.pack(pady=5)

    window.mainloop()

layout()