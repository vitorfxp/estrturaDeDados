def buscar_sucessor(arr,posiçao):
    """dado um input de um elemento pelo usuario, busca a posiçao anterior e seu elemento"""
    if posiçao not in arr: 
     return None
    
    sus = arr[posiçao + 1]
    return sus

def buscar_antecessor(arr,posiçao):
    """dado um input de um elemento pelo usuario, busca a posiçao anterior e seu elemento"""
    if posiçao <  0 or posiçao > len (arr):
        raise IndexError("posiçao invalida")

    
    sus = arr[posiçao - 1]
    return sus



arr = [10,20,30,40]
print(buscar_sucessor(arr,2))
print(buscar_antecessor(arr,6))
    
