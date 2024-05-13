import tkinter as tk
from tkinter import messagebox
import getUser
from cleanDisk import cleanDisk
from clearArqTemp import clearArqTemps
from esvaziarLixeira import esvaziarLixeira
from delArqsExplorer import delArqsExplorer

def limpar_arquivos_temporarios():
    clearArqTemps()
    messagebox.showinfo("Limpar Arquivos Temporários", "Executando a limpeza de arquivos temporários...")

def limpar_disco():
    cleanDisk()
    messagebox.showinfo("Limpar Disco", "Executando a limpeza do disco...")

def limpar_pastas():
    delArqsExplorer()
    messagebox.showinfo("Limpar Pastas", "Executando a limpeza de pastas...")

def esvaziar_lixeira():
    esvaziarLixeira()
    messagebox.showinfo("Esvaziar Lixeira", "Esvaziando a lixeira...")

def ver_ipv4():
    ip_address = getUser.ver_ipv4()  # Corrija o nome do módulo aqui
    messagebox.showinfo("Ver IPv4", f"Exibindo o endereço IPv4... {ip_address}")

def sair():
    exit()

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