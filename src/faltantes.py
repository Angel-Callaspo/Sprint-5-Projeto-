def substituir_nan_coluna(df,column,valor):
    """substituir valores faltantes em uma coluna"""
    for col in df[column]:
        df[col].fillna(valor, inplace=True)
    return df
