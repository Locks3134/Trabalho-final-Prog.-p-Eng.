# Importa a biblioteca para trabalhar com data e hora
from datetime import datetime

# Importa o Tkinter (interface gráfica)
import tkinter as tk

# Importa caixas de mensagem (alertas na tela)
from tkinter import messagebox


# Lista principal onde todos os funcionários serão armazenados
funcionarios = []


# =========================
# FUNÇÃO: CADASTRAR FUNCIONÁRIO
# =========================
def cadastrar():
    # Pega o nome digitado na caixa de texto
    nome = entry_nome.get()

    # Verifica se o usuário deixou vazio
    if nome == "":
        messagebox.showerror("Erro", "Digite um nome!")
        return

    # Gera um ID automático (posição na lista + 1)
    id_func = len(funcionarios) + 1

    # Cria um dicionário representando o funcionário
    funcionario = {
        "id": id_func,
        "nome": nome,
        "pontos": []  # lista onde serão armazenados os horários
    }

    # Adiciona o funcionário na lista principal
    funcionarios.append(funcionario)

    # Mostra mensagem de sucesso
    messagebox.showinfo("Sucesso", f"{nome} cadastrado com ID {id_func}")

    # Limpa o campo de nome
    entry_nome.delete(0, tk.END)

    # Adiciona o funcionário na lista lateral
    lista_funcionarios.insert(tk.END, f"{id_func} - {nome}")


# =========================
# FUNÇÃO: REGISTRAR ENTRADA
# =========================
def entrada():
    try:
        # Tenta converter o ID digitado para número inteiro
        id_func = int(entry_id.get())
    except:
        # Se der erro, mostra mensagem
        messagebox.showerror("Erro", "Digite um ID válido!")
        return

    # Procura o funcionário com o ID informado
    for f in funcionarios:
        if f["id"] == id_func:

            # Pega data e hora atual do sistema
            hora = datetime.now().strftime("%d/%m/%Y - %H:%M")

            # Cria um registro de ponto (entrada sem saída ainda)
            registro = {
                "entrada": hora,
                "saida": ""
            }

            # Adiciona o registro ao funcionário
            f["pontos"].append(registro)

            messagebox.showinfo("Sucesso", "Entrada registrada!")
            return

    # Caso não encontre o funcionário
    messagebox.showerror("Erro", "Funcionário não encontrado!")


# =========================
# FUNÇÃO: REGISTRAR SAÍDA
# =========================
def saida():
    try:
        # Converte o ID
        id_func = int(entry_id.get())
    except:
        messagebox.showerror("Erro", "Digite um ID válido!")
        return

    # Procura o funcionário
    for f in funcionarios:
        if f["id"] == id_func:

            # Verifica se existe entrada registrada
            if len(f["pontos"]) == 0:
                messagebox.showerror("Erro", "Sem entrada registrada!")
                return

            # Pega hora atual
            agora = datetime.now().strftime("%d/%m/%Y - %H:%M")

            # Atualiza o último registro com a saída
            f["pontos"][-1]["saida"] = agora

            messagebox.showinfo("Sucesso", "Saída registrada!")
            return

    messagebox.showerror("Erro", "Funcionário não encontrado!")


# =========================
# FUNÇÃO: MOSTRAR HISTÓRICO
# =========================
def historico():
    try:
        id_func = int(entry_id.get())
    except:
        messagebox.showerror("Erro", "Digite um ID válido!")
        return

    # Procura funcionário
    for f in funcionarios:
        if f["id"] == id_func:

            # Limpa a área de texto
            texto.delete(1.0, tk.END)

            # Mostra o nome
            texto.insert(tk.END, f"Histórico de {f['nome']}:\n")

            # Percorre todos os registros de ponto
            for p in f["pontos"]:
                texto.insert(
                    tk.END,
                    f"Entrada: {p['entrada']} | Saída: {p['saida']}\n"
                )

            return

    messagebox.showerror("Erro", "Funcionário não encontrado!")

#=========================
# FUNÇÃO: SELECIONAR FUNCIONÁRIO DA LISTA
#=========================
def selecionar_funcionario(event):
    try:
        # Pega o item selecionado na lista
        selecao = lista_funcionarios.get(lista_funcionarios.curselection())

        # Extrai o ID (parte antes do "-")
        id_func = selecao.split(" - ")[0]

        # Limpa o campo de ID
        entry_id.delete(0, tk.END)

        # Insere o ID automaticamente
        entry_id.insert(0, id_func)

    except:
        pass  # evita erro se nada estiver selecionado

# =========================
# INTERFACE GRÁFICA
# =========================

# Cria a janela principal
janela = tk.Tk()

# Define o título da janela
janela.title("Sistema de Ponto")

# Define tamanho da janela
janela.geometry("800x600")

# Define cor de fundo (dark mode)
janela.configure(bg="#1e1e1e")


# Configuração de colunas (centralização + painel lateral)
janela.grid_columnconfigure(0, weight=1)  # espaço vazio esquerda
janela.grid_columnconfigure(1, weight=0)  # conteúdo central
janela.grid_columnconfigure(2, weight=1)  # espaço vazio direita
janela.grid_columnconfigure(3, weight=1)  # painel lateral

# Permite redimensionar janela
janela.resizable(True, True)


# =========================
# TÍTULO
# =========================
tk.Label(
    janela,
    text="Sistema de Ponto",
    font=("Arial", 16, "bold"),
    bg="#1e1e1e",
    fg="white"
).grid(row=0, column=1, pady=15)


# =========================
# CAMPO NOME
# =========================
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
    insertbackground="white"
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


# =========================
# LISTA LATERAL
# =========================

# Título da lista
tk.Label(
    janela,
    text="Funcionários",
    bg="#1e1e1e",
    fg="white",
    font=("Arial", 12, "bold")
).grid(row=1, column=3, pady=5)

# Lista que mostra funcionários cadastrados
lista_funcionarios = tk.Listbox(
    janela,
    width=25,
    height=15,
    bg="#2c2c2c",
    fg="white"
)
lista_funcionarios.grid(row=2, column=3, rowspan=6, padx=10, pady=10)
lista_funcionarios.bind("<<ListboxSelect>>", selecionar_funcionario)

# =========================
# CAMPO ID
# =========================
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


# =========================
# BOTÕES DE AÇÃO
# =========================
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


# =========================
# ÁREA DE TEXTO
# =========================
texto = tk.Text(
    janela,
    height=10,
    width=60,
    bg="#2c2c2c",
    fg="white",
    insertbackground="white"
)
texto.grid(row=9, column=1, pady=10)


# =========================
# INICIA A INTERFACE
# =========================
janela.mainloop()