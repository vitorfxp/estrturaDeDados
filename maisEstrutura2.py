def inserir_array(arr, elemento, posiçao):
    """insere elemento em posiçao especifica"""  
    if posiçao <  0 or posiçao > len(arr):
        raise IndexError("posiçao invalida")

    arr.insert(posiçao,elemento)
    return arr

def remoçao_array(arr, elemento):
    if elemento in arr:
        arr.remove(elemento)  
    return arr

def busca_array(arr, elemento):
    """escreve o elemento e busca a posiçao"""
    if elemento in arr:
        pos = arr.index(elemento)
        return pos
    else:
        return None

def num_max(arr):
    """busca a maior variavel dentro do array"""
    if len(arr) == 0:
        return None
    maior = arr[0]  
    for num in arr[1:]:  
        if num > maior:
            maior = num
    return maior

def num_min(arr):
    """busca a menor variavel dentro do array"""
    if len(arr) == 0:
        return None
    menor = arr[0]
    for num in arr[1:]:
        if num < menor:
            menor = num
    return menor 

def buscar_sucessor(arr, posiçao):
    """dado um input de um elemento pelo usuario, busca a posiçao"""
    if posiçao <  0 or posiçao > len (arr):
        raise IndexError("posiçao invalida")

    sus = arr[posiçao + 1]
    return sus

def buscar_antecessor(arr, posiçao):
    """dado um input de um elemento pelo usuario, busca a posiçao anterior e seu elemento"""
    if posiçao <  0 or posiçao > len (arr):
        raise IndexError("posiçao invalida")

    sus = arr[posiçao - 1]
    return sus

def mostar_todas_opçoes(arr):
    """mostra o array inicial"""
    print("Informaçoes sobre o array")
    print("----------------------------------")
    print(f"Array atual: {arr}")
    print(f"Tamanho atual do array: {len(arr)}")

    if len(arr) > 0:
        print(f"Maior numero dentro do array: {num_max(arr)}")
        print(f"Menor numero dentro do array: {num_min(arr)}")
        print("-------------------------------")
    else: 
        print("Array vazio")

    return arr

def executar_operaçoes(arr):
    """Executa com input algumas funçoes"""
    print("------------------------------")

    #inserçaõ
    elemento = int(input("Digite um elemento: "))
    posiçao = int(input("digite uma posiçao para esse elemento: "))
    arr = inserir_array(arr, elemento, posiçao)
    print(f"Aqui esta seu array atual: {arr}")

    #remorção
    posiçao = int(input("Digite um elemento para remoçao: "))
    arr = remoçao_array(arr, posiçao)
    print(f"Aqui esta seu array: {arr}")

    #busca
    elemento_busca = int(input("Digite um elemento para buscar no array: "))
    pos = busca_array(arr, elemento_busca)

    if pos is not None:
        print(f"Aqui está a posição do elemento {elemento_busca} no array: {pos}")
    else:
        print("Elemento não encontrado no array.")
    
    return arr




#array criado para verificaçao das funçoes pedidas pelo professor

numero = [10 ,20 ,30 , 40] 
print(mostar_todas_opçoes(numero))
print(executar_operaçoes(numero))