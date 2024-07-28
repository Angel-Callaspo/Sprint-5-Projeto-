def faltante_categorico(data_frame, column, valor):
    """Preenche ausentes/ condicional NAN deve ser = '' por keep_default_na=False na letura"""
    data_frame[column]=data_frame[column].replace('', valor)
    return print(f"Valores univocos da coluna: {column}, são: {data_frame[column].unique()}")

def substituir_nan_coluna(df,column,valor):
    """substituir valores faltantes em uma coluna"""
    for col in column:
        df[col] = df[col].fillna(valor, inplace=True)
    return df
