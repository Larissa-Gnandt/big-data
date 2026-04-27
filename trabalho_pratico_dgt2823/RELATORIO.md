# Trabalho Prático

## Tema

Tratamento de dados utilizando Python e a biblioteca Pandas.

## Objetivo

Realizar a leitura, visualização, investigação e limpeza de um conjunto de dados em formato CSV, preparando-o para uma etapa posterior de análise ou mineração de dados.

## Arquivos entregues

- `dados.csv`: conjunto de dados obrigatório da atividade, separado por ponto e vírgula.
- `microatividades.py`: script com as cinco microatividades solicitadas.
- `trabalho_pratico.py`: script principal com o processo de limpeza dos dados.

## Microatividades

### Microatividade 1

Foi utilizada a função `read_csv()` da biblioteca Pandas para ler o arquivo `dados.csv`. Como o arquivo utiliza `;` como separador de colunas, foram informados os parâmetros `sep=";"`, `engine="python"` e `encoding="utf-8"`.

### Microatividade 2

Foi criado um subconjunto de dados a partir do dataframe original, selecionando apenas as colunas `ID`, `Date` e `Calories`.

### Microatividade 3

Foi configurada a opção `display.max_rows` para `9999`, permitindo que o Pandas exibisse uma quantidade maior de linhas. Em seguida, o dataframe foi exibido com o método `to_string()`.

### Microatividade 4

Foram utilizados os métodos `head(10)` e `tail(10)` para exibir, respectivamente, as primeiras e as últimas 10 linhas do dataframe.

### Microatividade 5

Foi utilizado o método `info()` para verificar informações gerais do dataframe, como total de linhas, total de colunas, tipos de dados, valores não nulos e memória utilizada. Também foram usados `shape`, `isnull().sum()`, `dtypes` e `memory_usage()`.

## Trabalho prático

O script `trabalho_pratico.py` executa as seguintes etapas:

1. Leitura do arquivo CSV com Pandas.
2. Exibição das informações gerais do dataframe.
3. Exibição das primeiras e últimas 10 linhas.
4. Criação de uma cópia do conjunto original para tratamento.
5. Substituição dos valores nulos da coluna `Calories` por `0`.
6. Substituição inicial dos valores nulos da coluna `Date` por `1900/01/01`.
7. Tentativa de conversão da coluna `Date` para datetime, registrando o erro esperado.
8. Substituição de `1900/01/01` por valor nulo.
9. Nova tentativa de conversão da coluna `Date`, registrando o erro causado pelo valor `20201226`.
10. Correção específica do valor `20201226` para `2020-12-26`, usando `replace()` combinado com `to_datetime()`.
11. Conversão final da coluna `Date` para o tipo datetime.
12. Remoção do registro que permaneceu com valor nulo na coluna `Date`.

## Resultado final

Ao final do processo, os valores nulos da coluna `Calories` foram substituídos por `0`, a coluna `Date` foi convertida para o tipo `datetime64[ns]`, o valor inválido `20201226` foi corrigido e o registro com data nula foi removido. Assim, o conjunto de dados ficou mais adequado para análises posteriores.

## Como executar

No terminal, acesse a pasta do trabalho:

```bash
cd trabalho_pratico_dgt2823
```

Execute as microatividades:

```bash
python3 microatividades.py
```

Execute o trabalho prático:

```bash
python3 trabalho_pratico.py
```
