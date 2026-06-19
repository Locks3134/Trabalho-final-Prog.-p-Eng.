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
            registro = {"entrada": "Agora", "saida": ""}
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

            f["pontos"][-1]["saida"] = "Agora"
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

# Nome
tk.Label(janela, text="Nome:").pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

tk.Button(janela, text="Cadastrar Funcionário", command=cadastrar).pack(pady=5)

# ID
tk.Label(janela, text="ID do Funcionário:").pack()
entry_id = tk.Entry(janela)
entry_id.pack()

# Botões
tk.Button(janela, text="Registrar Entrada", command=entrada).pack(pady=2)
tk.Button(janela, text="Registrar Saída", command=saida).pack(pady=2)
tk.Button(janela, text="Ver Histórico", command=historico).pack(pady=5)

# Área de texto
texto = tk.Text(janela, height=10, width=40)
texto.pack()

janela.mainloop()