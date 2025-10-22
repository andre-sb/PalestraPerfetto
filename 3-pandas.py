import pandas as pd
import numpy as np

def GeraPrimeiroDataFrame():
    # Gera um DataFrame com 100 linhas, índice padrão, colunas A e B com inteiros aleatórios
    df1 = pd.DataFrame({
        'A': np.random.randint(0, 1000, size=100),
        'B': np.random.randint(0, 1000, size=100)
    })
    return df1

def GeraSegundoDataFrame():
    # Gera um DataFrame com 100 linhas, índice padrão, colunas C e D com inteiros aleatórios
    df2 = pd.DataFrame({
        'C': np.random.randint(0, 1000, size=100),
        'D': np.random.randint(0, 1000, size=100)
    })
    return df2

def OrganizaDataFrames(df1, df2):
    # Faz merge outer join dos dois dataframes e ordena pelo valor decrescente da coluna A
    merged = pd.merge(df1, df2, left_index=True, right_index=True, how='outer')
    merged_sorted = merged.sort_values(by='A', ascending=False)
    return merged_sorted

def main():
    primeiro = GeraPrimeiroDataFrame()
    segundo = GeraSegundoDataFrame()
    resultado = OrganizaDataFrames(primeiro, segundo)
    print(resultado.head())

if __name__=="__main__":
    main()