def adicionar_registro(valor, descricao):
    with open("financeiro.log", "a") as file:
        file.write(f"{valor} {descricao}\n")
    print("Registro adicionado com sucesso!")

adicionar_registro(500, "venda adicional")

