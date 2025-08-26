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

num = [10,20,40,30]
print(num_max(num))
print(num_min(num))






