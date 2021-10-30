# Implementando o código central do jogo de dominó

# Importando as funções obrigatórias
from mandatory_functions import cria_pecas,inicia_jogo,verifica_ganhador,soma_pecas,posicoes_possiveis,adiciona_na_mesa
# Importando o módulo random
import random as r

# Introdução
print('INSPER - Curso de Engenharia - 1° Semestre - 2021.2\nDisciplina: Design de Software\nProfessor: Humberto Sandmann\nAluno: Augusto Giuliani\nAtividade: Exercício Programa 2 - Jogo de Dominó')

# Mensagem inicial
print('\nBem-vindo(a) ao meu jogo de dominó.\nBoa sorte!')

# INICIANDO O JOGO - CRIANDO O LOOP CENTRAL
GAME = True # ---> estado do jogo
while GAME:
# Escolhendo o número de jogadores
    n = input('Quer jogar com quantos jogadores? 1,2 ou 3?')
    while n!=1 and n!=2 and n!=3: # Se o usuário der uma resposta inválida
        n = input('Quer jogar com quantos jogadores? 1,2 ou 3?')
    n+=1 # --> Número total de participantes no jogo, incluindo o usuário (humano)
# Criando a lista de peças e fazendo seu devido embaralhamento
    l_pieces = cria_pecas()
# Distribuindo 7 peças para cada jogador, criando monte e mesa (retorna dicionário com tudo isso).
# NOTE: O usuário é o jogador "0" desse dicionário
    d_game = inicia_jogo(n,l_pieces)
# Um dos jogadores é aleatoriamente escolhido para iniciar a rodada
    player = r.randint(0,n-1)
    
         

