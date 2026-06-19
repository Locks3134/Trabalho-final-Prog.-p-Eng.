# Lista para armazenar funcionários
funcionarios = []

# Função para cadastrar funcionário
def cadastrar_funcionario():
    nome = input("Digite o nome do funcionário: ")
    id_func = len(funcionarios) + 1

    funcionario = {
        "id": id_func,
        "nome": nome,
        "pontos": []
    }

    funcionarios.append(funcionario)
    print("Funcionário cadastrado com sucesso!\n")


# Função para listar funcionários
def listar_funcionarios():
    if len(funcionarios) == 0:
        print("Nenhum funcionário cadastrado.\n")
    else:
        for f in funcionarios:
            print(f"ID: {f['id']} | Nome: {f['nome']}")
    print()


# Função para registrar entrada
def registrar_entrada():
    try:
        id_func = int(input("Digite o ID do funcionário: "))
    except ValueError:
        print("Erro: Digite apenas números inteiros!\n")
        return

    for f in funcionarios:
        if f["id"] == id_func:
            entrada = input("Digite o horário de entrada: ")

            registro = {
                "entrada": entrada,
                "saida": ""
            }

            f["pontos"].append(registro)
            print("Entrada registrada!\n")
            return

    print("Funcionário não encontrado.\n")


# Função para registrar saída
def registrar_saida():
    try:
        id_func = int(input("Digite o ID do funcionário: "))
    except ValueError:
        print("Erro: Digite apenas números inteiros!\n")
        return

    for f in funcionarios:
        if f["id"] == id_func:
            if len(f["pontos"]) == 0:
                print("Nenhuma entrada registrada.\n")
                return

            saida = input("Digite o horário de saída: ")
            f["pontos"][-1]["saida"] = saida

            print("Saída registrada!\n")
            return

    print("Funcionário não encontrado.\n")


# Função para mostrar histórico
def mostrar_historico():
    id_func = int(input("Digite o ID do funcionário: "))

    for f in funcionarios:
        if f["id"] == id_func:
            print(f"\nHistórico de {f['nome']}:")

            for p in f["pontos"]:
                print(f"Entrada: {p['entrada']} | Saída: {p['saida']}")

            print()
            return

    print("Funcionário não encontrado.\n")


# MENU PRINCIPAL
while True:
    print("=== SISTEMA DE PONTO ===")
    print("1 - Cadastrar funcionário")
    print("2 - Listar funcionários")
    print("3 - Registrar entrada")
    print("4 - Registrar saída")
    print("5 - Ver histórico")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_funcionario()
    elif opcao == "2":
        listar_funcionarios()
    elif opcao == "3":
        registrar_entrada()
    elif opcao == "4":
        registrar_saida()
    elif opcao == "5":
        mostrar_historico()
    elif opcao == "0":
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida.\n")