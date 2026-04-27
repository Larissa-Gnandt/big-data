import pandas as pd


CAMINHO_CSV = "dados.csv"


def titulo(texto):
    print("\n" + "=" * 80)
    print(texto)
    print("=" * 80)


# Microatividade 1: leitura de arquivo CSV com Pandas.
dados = pd.read_csv(
    CAMINHO_CSV,
    sep=";",
    engine="python",
    encoding="utf-8",
)

titulo("Microatividade 1 - Leitura do arquivo CSV")
print(dados)

# Microatividade 2: criacao de subconjunto de dados.
subconjunto = dados[["ID", "Date", "Calories"]]

titulo("Microatividade 2 - Subconjunto com 3 colunas")
print(subconjunto)

# Microatividade 3: configuracao do numero maximo de linhas exibidas.
pd.set_option("display.max_rows", 9999)

titulo("Microatividade 3 - Exibicao completa com to_string()")
print(dados.to_string())

# Microatividade 4: exibicao das primeiras e ultimas N linhas.
titulo("Microatividade 4 - Primeiras 10 linhas")
print(dados.head(10))

titulo("Microatividade 4 - Ultimas 10 linhas")
print(dados.tail(10))

# Microatividade 5: informacoes gerais sobre colunas, linhas e dados.
titulo("Microatividade 5 - Informacoes gerais do dataframe")
dados.info()

titulo("Microatividade 5 - Resumo solicitado")
print(f"Total de linhas: {dados.shape[0]}")
print(f"Total de colunas: {dados.shape[1]}")
print("Quantidade de dados nulos por coluna:")
print(dados.isnull().sum())
print("Tipos de dados por coluna:")
print(dados.dtypes)
print(f"Memoria utilizada: {dados.memory_usage(deep=True).sum()} bytes")
