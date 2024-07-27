

def df_duplicado (data_f):
    """DESCRIÇÃO DA FUNÇÃO DUPLICADOS DE DATAFRAME EXPLÍCITOS"""
    aux_df_duplicado = data_f[data_f.duplicated()]
    tam_df_duplicado = data_f.duplicated().sum()
    if tam_df_duplicado > 0:
        return print(f"{aux_df_duplicado}, Quantidade duplicados é = {tam_df_duplicado}")
    else:
        return print(f"Quantidade de duplicados é = {tam_df_duplicado}")


def serie_duplicado (data_f, column):
    """DESCRIÇÃO DA FUNÇÃO DUPLICADOS DE SERIES EXPLÍCITOS"""
    aux_serie_duplicado = data_f[column].value_counts()
    mascara = aux_serie_duplicado > 1
    duplicado = aux_serie_duplicado.index[mascara]
    if len(duplicado) > 1:
        return print(f"{duplicado}, Quantidade duplicados em {column} é = {len(duplicado)}")
    else:
        return print(f"Quantidade duplicados em {column} é = {len(duplicado)}")
