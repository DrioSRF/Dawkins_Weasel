# pegando a biblioteca random
import random

# frase objetivo
frase_alvo = "METHINKS IT IS LIKE A WEASEL"
frase_mais_parecida = ''
score = 0
maior_score = 0
frase_pai = []
geracao = 0

for i in range(28):

    frase_pai.append(random.choice(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ "))

while maior_score < 28:

    geracao += 1

    for filha in range(100):

        frase_filha = ''

        for j in range(28):

            numero_aleatorio = random.randint(1, 100)

            if numero_aleatorio <= 5:

                frase_filha += random.choice(
                    "ABCDEFGHIJKLMNOPQRSTUVWXYZ ")

            else:

                frase_filha += frase_pai[j]

            if frase_filha[j] == frase_alvo[j]:

                score += 1

        if maior_score < score:

            frase_mais_parecida = frase_filha
            maior_score = score

        if maior_score == 28:

            break

        print(frase_filha, end="; ")
        print("Geração:", end=" ")
        print(geracao, end="; ")
        print("Filha: " + str(filha), end="; ")
        print("Score: " + str(score))
        score = 0

    frase_pai = frase_mais_parecida

print(frase_mais_parecida, end="; ")
print("Geração:", end=" ")
print(geracao, end="; ")
print("Filha: " + str(filha), end="; ")
print("Score: " + str(score))
