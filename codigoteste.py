notas = []

for i in range(50):
    nota = float(input(f"Aluno {i+1}, digite sua nota (ou -1 para encerrar): "))
    if nota == -1:  
        break
    notas.append(nota)

if len(notas) > 0:
    media = sum(notas) / len(notas)

    
    maior_nota = max(notas)
    menor_nota = min(notas)

    print("\n--- RESULTADOS ---")
    print(f"Notas: {notas}")
    print(f"Média da turma: {media:.2f}")
    print(f"Maior nota: {maior_nota}")
    print(f"Menor nota: {menor_nota}")
else:
    print("Nenhuma nota foi registrada.")













#/ print("aqui estar seu numero adicionado:", inserir_array(numero,50,4))
#print("aqui estar seu numero removido:", remoçao_array(numero,2))
#print("aqui esta a posiçao buscada dentro do array:", busca_array(numero,30))
#print("O maior numero e:", num_max(numero))
#print("O menor numero e:", num_min(numero))
#print(buscar_sucessor(numero,3))
#print(buscar_antecessor(numero,2))

