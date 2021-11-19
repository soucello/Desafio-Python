# --- TESTE DE PYTHON ---
import math

# --- QUESTAO 1 ---

print('Questão 1:\n')

contador = 0
for i in range(5000000):
    if (i % 2 == 0) and (i % 49 == 0) and (i % 37 == 0):
        contador += 1

print(f'Existem {contador} números que satisfazem as 3 condições\n\n')

# --- QUESTAO 2 ---

print('Questão 2:\n')

vetor = []

for i in range(10):
    if i % 2 == 0:
        x = 3**i + 7*(math.factorial(i))
        vetor.append(x)
    else:
        x = 2**i + 4*(math.log(i))
        vetor.append(x)

maior = vetor.index(max(vetor))
media = sum(vetor)/len(vetor)

print(f'A posição do maior elemento desse vetor é a {maior}ª posição')
print('A média dos elementos contidos nesse vetor é %.2f\n\n' %media)

# --- QUESTAO 3 ---

print('Questão 3:\n')

alunos = 0
notas = {}

while alunos < 5:
    nota = float(input(f'Nota do {alunos+1}º aluno: '))
    notas[f'Aluno {alunos+1}'] = nota
    alunos += 1

maior_nota = notas[max(notas, key=notas.get)]

for key, value in notas.items():
    if value == maior_nota:
        print(f'O aluno com a maior nota é o {key} e sua nota é {value}')
