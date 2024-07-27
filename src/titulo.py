def cabecalhos_df (df):
    """Corrigir cabeçalhos de colunas"""
    coluna_nova = []
    for aux_col in df.columns:
        sem_espaços = aux_col.strip()
        minuscula = sem_espaços.lower()
        underline = minuscula.replace(' ','_')
        coluna_nova.append(underline)
    df.columns = coluna_nova
    return df
