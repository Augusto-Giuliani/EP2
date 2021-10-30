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
# Distribuindo 7 peças para cada jogador, criando monte e mesa (retorna dicionário com tudo isso)
    d_game = inicia_jogo(n,l_pieces)
# Quebrando o dicionário em diferentes variáveis
    players = d_game['jogadores'] # --> NOTE: O usuário é o jogador "0" desse dicionário
    table = d_game['mesa']
    storage = d_game['monte']
# Um dos jogadores é aleatoriamente escolhido para iniciar a rodada
    player = r.randint(0,n-1)
    # INICIANDO A RODADA - CRIANDO OUTRO LOOP
    ROUND = True
    while ROUND:
    # Mostrando as peças sobre a mesa, as peças do usuário e a quantidade de peças do(s) outro(s) jogador(es)
        print(table)
        print('Suas peças:{}.'.format(players[0]))
        alert = list() # --> lista que contém jogadores com apenas uma peça
        for i in range(1,n+1):
            if len(players[i])==1:
                alert.append(i+1)
            print('Quantidade de peças do jogador {}: {}.'.format(i+1,len(players[i])))
    # Dá um aviso se algum jogador só estiver com uma peça
        if alert!=list():
            for i in alert:
                print('CUIDADO! O jogador {} está com apenas uma peça.'.format(i))
    # Verificando as peças possíveis (que podem ser colocadas na mesa) do jogador
        possibilities = posicoes_possiveis(table,players[player])
    # ----> SE NÃO HOUVER PEÇAS POSSÍVEIS
    # Se o jogador não tiver peças "possíveis", ele pega do monte até ter uma peça possível
        while possibilities == list() and storage!=list():
        # Se o jogador for o usuário
            if player==0:
                input('Eita! Você vai ter que pegar uma peça do monte. Aperte a tecla "Enter" para apanhar uma peça do monte.')
        # Se o jogador não for o usuário
            elif player!=0:
                print('O jogador {} se deu mal, vai ter que pegar do monte.'.format(player+1))
            players[player].append(storage[0])
            del storage[0] # --> apaga essa peça obtida do monte no monte
            possibilities = posicoes_possiveis(table,players[player]) # --> novamente verifica as peças possíveis
    # Se o jogador não tiver peças "possíveis" e não tiver monte, é a vez do próximo jogador
        if possibilities == list() and storage == list():
            if player==0:
                input('Uma pena. Como não há mais peças no monte, vamos ter que pular a sua vez. Aperte a tecla "Enter" para continuar o jogo.')
            elif player!=0:
                print('Como não tem monte, vamos pular a vez do jogador {}.'.format(player+1))
            player+=1
    # ----> SE HOUVER PEÇAS POSSÍVEIS
    # Adicionando a peça na mesa
    # Se o jogador for o usuário, ele escolhe qual peça colocar
        if player==0:
        
        

            



    
         

