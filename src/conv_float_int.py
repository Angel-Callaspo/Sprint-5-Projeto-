import numpy as np

def conver_float_int(data, column):
    """Conversão de tipo float para inteiro"""
    verifica_conver = np.array_equal(data[column], data[column].astype('int'))
    if verifica_conver==True:
        data[column] = data[column].astype('int')
        print(data.info(show_counts=True))
        return print("É seguro a conversão de float64 para int64")
    else:
        return print('Não é seguro a conversão de tipos de dados de float64 para int64')
