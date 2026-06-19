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
janela.configure(bg="#f0f0f0")

# Título
tk.Label(
    janela,
    text="Sistema de Ponto",
    font=("Arial", 16, "bold"),
    bg="#f0f0f0"
).grid(row=0, column=0, columnspan=2, pady=10)

# Nome
tk.Label(janela, text="Nome:", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_nome = tk.Entry(janela, width=25)
entry_nome.grid(row=1, column=1, padx=10, pady=5)

# Botão cadastrar
tk.Button(
    janela,
    text="Cadastrar Funcionário",
    command=cadastrar,
    bg="#4CAF50",
    fg="white",
    width=25
).grid(row=2, column=0, columnspan=2, pady=10)

# ID
tk.Label(janela, text="ID do Funcionário:", bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_id = tk.Entry(janela, width=25)
entry_id.grid(row=3, column=1, padx=10, pady=5)

# Botões de ação
tk.Button(
    janela,
    text="Registrar Entrada",
    command=entrada,
    bg="#2196F3",
    fg="white",
    width=25
).grid(row=4, column=0, columnspan=2, pady=3)

tk.Button(
    janela,
    text="Registrar Saída",
    command=saida,
    bg="#f44336",
    fg="white",
    width=25
).grid(row=5, column=0, columnspan=2, pady=3)

tk.Button(
    janela,
    text="Ver Histórico",
    command=historico,
    bg="#9C27B0",
    fg="white",
    width=25
).grid(row=6, column=0, columnspan=2, pady=10)

# Área de texto
texto = tk.Text(janela, height=10, width=45)
texto.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

janela.mainloop()