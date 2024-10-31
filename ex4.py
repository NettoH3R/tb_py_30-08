import pandas as pd


dados = {
    "Coluna1": [1, 2, 3],
    "Coluna2": ["A", "B", "C"],
    "Coluna3": [4.5, 5.5, 6.5]
}


df = pd.DataFrame(dados)
df.to_csv("exemplo.csv", index=False, sep=",")

def ler_csv_para_lista(nome_arquivo, separador):

    df = pd.read_csv(nome_arquivo, sep=separador)
    

    lista_bidimensional = df.values.tolist()
    
    print("Conteúdo do arquivo:", lista_bidimensional)
    return lista_bidimensional

lista = ler_csv_para_lista("exemplo.csv", ",")