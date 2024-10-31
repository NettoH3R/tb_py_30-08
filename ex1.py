import pandas as pd


with open("financeiro.log", "r") as file:
    data = []
    for line in file:
        parts = line.split()  # Divide a linha em partes
        valor = int(parts[0])  # Primeiro elemento é o valor
        descricao = " ".join(parts[1:])  # O restante é a descrição
        data.append([valor, descricao])

df = pd.DataFrame(data, columns=["valor", "descricao"])


saldo = df["valor"].sum()
print("Saldo financeiro da empresa:", saldo)