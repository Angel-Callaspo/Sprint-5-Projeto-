 
def mod_cabecalhos_df (df, indice,renome): #num_col, renome
    """modificar cabeçalhos das colunas"""
    colunas = list(df.columns)
    colunas.pop(indice-1)
    colunas.insert(indice-1,renome)#a = colunas[indice-1]
    df.columns = colunas
    return df
