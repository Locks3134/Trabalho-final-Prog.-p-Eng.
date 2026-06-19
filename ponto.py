from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# Lista de funcionários
funcionarios = []

# Função para cadastrar funcionário
def cadastrar():
    nome = entry_nome.get()

    if nome == "":
        messagebox.showerror("Erro", "Digite um nome!")
        return

    id_func = len(funcionarios) + 1

    funcionario = {
        "id": id_func,
        "nome": nome,
        "pontos": []
    }

    funcionarios.append(funcionario)
    messagebox.showinfo("Sucesso", f"{nome} cadastrado com ID {id_func}")
    entry_nome.delete(0, tk.END)
    lista_funcionarios.insert(tk.END, f"{id_func} - {nome}")


# Função para registrar entrada
def entrada():
    try:
        id_func = int(entry_id.get())
    except:
        messagebox.showerror("Erro", "Digite um ID válido!")
        return

    for f in funcionarios:
        if f["id"] == id_func:

            hora = datetime.now().strftime("%d/%m/%Y - %H:%M")
            registro = {
            "entrada": hora,
            "saida": ""
}
            f["pontos"].append(registro)
            messagebox.showinfo("Sucesso", "Entrada registrada!")
            return

    messagebox.showerror("Erro", "Funcionário não encontrado!")


# Função para registrar saída
def saida():
    try:
        id_func = int(entry_id.get())
    except:
        messagebox.showerror("Erro", "Digite um ID válido!")
        return

    for f in funcionarios:
        if f["id"] == id_func:
            if len(f["pontos"]) == 0:
                messagebox.showerror("Erro", "Sem entrada registrada!")
                return

            agora = datetime.now().strftime("%d/%m/%Y - %H:%M")
            f["pontos"][-1]["saida"] = agora

            messagebox.showinfo("Sucesso", "Saída registrada!")
            return

    messagebox.showerror("Erro", "Funcionário não encontrado!")


# Função para mostrar histórico
def historico():
    try:
        id_func = int(entry_id.get())
    except:
        messagebox.showerror("Erro", "Digite um ID válido!")
        return

    for f in funcionarios:
        if f["id"] == id_func:
            texto.delete(1.0, tk.END)
            texto.insert(tk.END, f"Histórico de {f['nome']}:\n")

            for p in f["pontos"]:
                texto.insert(tk.END, f"Entrada: {p['entrada']} | Saída: {p['saida']}\n")

            return

    messagebox.showerror("Erro", "Funcionário não encontrado!")


# ===== INTERFACE =====
janela = tk.Tk()
janela.title("Sistema de Ponto")
janela.geometry("800x600")
janela.configure(bg="#1e1e1e")  # fundo escuro

# 3 colunas (centro fixo)
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=0)
janela.grid_columnconfigure(2, weight=1)
janela.grid_columnconfigure(3, weight=1)

janela.resizable(True, True)

# Título
tk.Label(
    janela,
    text="Sistema de Ponto",
    font=("Arial", 16, "bold"),
    bg="#1e1e1e",
    fg="white"
).grid(row=0, column=1, pady=15)

# Nome
tk.Label(
    janela,
    text="Nome:",
    bg="#1e1e1e",
    fg="white"
).grid(row=1, column=1, pady=5)

entry_nome = tk.Entry(
    janela,
    width=25,
    bg="#2c2c2c",
    fg="white",
    insertbackground="white"  # cor do cursor
)
entry_nome.grid(row=2, column=1, pady=5)

# Botão cadastrar
tk.Button(
    janela,
    text="Cadastrar Funcionário",
    command=cadastrar,
    bg="#27ae60",
    fg="white",
    width=25
).grid(row=3, column=1, pady=10)


# Título da lista lateral
tk.Label(
    janela,
    text="Funcionários",
    bg="#1e1e1e",
    fg="white",
    font=("Arial", 12, "bold")
).grid(row=1, column=3, pady=5)

# Lista de funcionários
lista_funcionarios = tk.Listbox(
    janela,
    width=25,
    height=15,
    bg="#2c2c2c",
    fg="white"
)
lista_funcionarios.grid(row=2, column=3, rowspan=6, padx=10, pady=10)


# ID
tk.Label(
    janela,
    text="ID do Funcionário:",
    bg="#1e1e1e",
    fg="white"
).grid(row=4, column=1, pady=5)

entry_id = tk.Entry(
    janela,
    width=25,
    bg="#2c2c2c",
    fg="white",
    insertbackground="white"
)
entry_id.grid(row=5, column=1, pady=5)

# Botões de ação
tk.Button(
    janela,
    text="Registrar Entrada",
    command=entrada,
    bg="#3498db",
    fg="white",
    width=25
).grid(row=6, column=1, pady=3)

tk.Button(
    janela,
    text="Registrar Saída",
    command=saida,
    bg="#e74c3c",
    fg="white",
    width=25
).grid(row=7, column=1, pady=3)

tk.Button(
    janela,
    text="Ver Histórico",
    command=historico,
    bg="#9b59b6",
    fg="white",
    width=25
).grid(row=8, column=1, pady=10)

# Área de texto
texto = tk.Text(
    janela,
    height=10,
    width=60,
    bg="#2c2c2c",
    fg="white",
    insertbackground="white"
)
texto.grid(row=9, column=1, pady=10)

janela.mainloop()