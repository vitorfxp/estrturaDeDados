def inserir_array(arr, elemento, posicao):
    """Insere elemento em posição específica"""  
    if posicao < 0 or posicao > len(arr):
        raise IndexError("posição invalida")

    arr.insert(posicao, elemento)
    return arr


def remocao_array(arr, elemento):
    """Remove um elemento se existir"""
    if elemento in arr:
        arr.remove(elemento)  
    return arr


def busca_array(arr, elemento):
    """Escreve o elemento e busca a posição"""
    if elemento in arr:
        pos = arr.index(elemento)
        return pos
    else:
        return None  # caso não encontre