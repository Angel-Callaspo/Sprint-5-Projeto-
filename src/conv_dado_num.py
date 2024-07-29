import numpy as np

def seg_float_int(data, column):
    """Conversão segura de tipo float para inteiro"""
    verifica_conver = np.array_equal(data[column], data[column].astype('int'))
    if verifica_conver==True:
        #print(data[column].info(show_counts=True))
        data[column] = data[column].astype('int')
        print(data[column])
    else:
        return print('Não é seguro a conversão de tipos de dados de float64 para int64')

def conver_str_float(data, column):
    """Conversão de tipo string para float"""
    data[column] = data[column].astype('float')
    return print(data[column].info())

def conv_float_int(data, column):
    """Conversão de tipo string para float"""
    data[column] = data[column].astype('int')
    return print(data[column].info())

def conv_str_int(data, column):
    """Conversão de tipo string para int"""
    data[column] = data[column].astype('float')
    data[column] = data[column].astype('int')
    return print(data[column].info())
