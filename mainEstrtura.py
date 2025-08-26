def inserir_array(arr, elemento, posiçao):
    """insere elemento em posiçao especifica"""  
    if posiçao <  0 or posiçao > len (arr):
        raise IndexError("posiçao invalida")

    arr.insert(posiçao,elemento)
    return arr

def remoçao_array(arr,elemento):
     if elemento in arr:
        arr.remove(elemento)  
        return arr
   
def busca_array(arr, elemento):
    """Escreve o elemento e busca a posição"""
    if elemento in arr:
        pos = arr.index(elemento)
        return pos
    else:
        return None  
def num_max(arr):
    """busca a maior variavel dentro do array"""
    maior = arr[0]  
    for num in arr[1:]:  
        if num > maior:
            maior = num
    return maior

def num_min(arr):
    """busca a menor variavel dentro do array"""
    menor = arr[0]
    for num in arr[1:]:
        if num < menor:
            menor = num
    return menor 

def buscar_sucessor(arr,posiçao):
    """dado um input de um elemento pelo usuario, busca a posiçao anterior e seu elemento"""
    if posiçao <  0 or posiçao > len (arr):
        raise IndexError("posiçao invalida")

    sus = arr[posiçao + 1]
    return sus

def buscar_antecessor(arr,posiçao):
    """dado um input de um elemento pelo usuario, busca a posiçao anterior e seu elemento"""
    if posiçao <  0 or posiçao > len (arr):
        raise IndexError("posiçao invalida")

    sus = arr[posiçao - 1]
    return sus

def mostar_todas_opçoes(arr):
    """mostra o array inicial"""
    print("Informaçoes sobre o array")
    print("----------------------------------")
    print(f"Array atual:{arr}")
    print(f"Tamanho atual do array:{len(arr)}")

    if len(arr) > 0:
        print(f"Maior numero dentro do array:{num_max(arr)}")
        print(f"Menor numero dentro do array:{num_min(arr)}")
        print("-------------------------------")
    else: 
        print("Array vazio")

    return arr

def executar_operaçoes(arr):
    """Executa com input algumas funçoes"""
    print("------------------------------")
    elemento = int(input("Digite um elemento: "))
    posiçao = int(input("digite uma posiçao para esse elemento: "))
    arr = inserir_array(arr,elemento,posiçao)
    print(f"Aqui esta seu array atual:{arr}")


    posiçao = int(input("Digite uma posiçao de 0 a 4 para remoçao: "))
    elemento_removido = arr [posiçao]
    arr = remoçao_array(arr,posiçao)
    print(f"elemento removido:{elemento_removido}")
    print(f"array atual:{arr}")

    elemento = int(input("Digite um elemento para buscar no array: "))  
    posicao = busca_array(arr, elemento)  #
    print(f"Elemento {elemento} está na posição: {posicao}")

    return arr

    





numero = [10 ,20 ,30 , 40] #array criado para verificaçao das funçoes pedidas pelo professor

print(mostar_todas_opçoes(numero))
print(executar_operaçoes(numero))


