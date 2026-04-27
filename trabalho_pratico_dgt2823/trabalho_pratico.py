import pandas as pd


CAMINHO_CSV = "dados.csv"


def titulo(texto):
    print("\n" + "=" * 80)
    print(texto)
    print("=" * 80)


# 1. Leitura do CSV fornecido.
dados_originais = pd.read_csv(
    CAMINHO_CSV,
    sep=";",
    engine="python",
    encoding="utf-8",
)

titulo("Dados importados - informacoes gerais")
dados_originais.info()

titulo("Primeiras 10 linhas dos dados originais")
print(dados_originais.head(10))

titulo("Ultimas 10 linhas dos dados originais")
print(dados_originais.tail(10))

# 2. Criacao de uma copia para limpeza, preservando os dados originais.
dados_limpos = dados_originais.copy()

# 3. Substituicao de valores nulos na coluna Calories por 0.
dados_limpos["Calories"] = dados_limpos["Calories"].fillna(0)

titulo("Apos substituir valores nulos de Calories por 0")
print(dados_limpos.to_string())

# 4. Substituicao inicial dos valores nulos da coluna Date por 1900/01/01.
dados_limpos["Date"] = dados_limpos["Date"].fillna("1900/01/01")

titulo("Apos substituir valores nulos de Date por 1900/01/01")
print(dados_limpos.to_string())

# 5. Tentativa orientada no roteiro: a data sem aspas simples nao corresponde
# ao formato usado nos demais registros, por isso o erro e exibido e tratado.
titulo("Tentativa de converter Date para datetime")
try:
    pd.to_datetime(dados_limpos["Date"], format="'%Y/%m/%d'")
except ValueError as erro:
    print("Erro encontrado na conversao:")
    print(erro)

# 6. Correcao do valor 1900/01/01 para nulo.
dados_limpos["Date"] = dados_limpos["Date"].replace("1900/01/01", pd.NA)

titulo("Apos substituir 1900/01/01 por valor nulo")
print(dados_limpos.to_string())

# 7. Nova tentativa de conversao. Agora o erro esperado ocorre no valor 20201226.
titulo("Nova tentativa de converter Date para datetime")
try:
    pd.to_datetime(dados_limpos["Date"], format="'%Y/%m/%d'")
except ValueError as erro:
    print("Erro encontrado na conversao:")
    print(erro)

# 8. Correcao especifica da string 20201226, combinando replace e to_datetime.
dados_limpos["Date"] = dados_limpos["Date"].replace(
    "20201226",
    pd.to_datetime("2020/12/26", format="%Y/%m/%d"),
)

titulo("Apos corrigir especificamente a data 20201226")
print(dados_limpos.to_string())

# 9. Conversao final de toda a coluna Date para datetime.
dados_limpos["Date"] = pd.to_datetime(dados_limpos["Date"], format="'%Y/%m/%d'")

titulo("Apos converter toda a coluna Date para datetime")
print(dados_limpos.to_string())
print(dados_limpos.dtypes)

# 10. Remocao dos registros que ainda possuem valores nulos na coluna Date.
dados_limpos = dados_limpos.dropna(subset=["Date"])

titulo("Dataframe final apos remover registros com Date nulo")
print(dados_limpos.to_string())

titulo("Informacoes finais do dataframe tratado")
dados_limpos.info()
