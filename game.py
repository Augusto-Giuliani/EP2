# Implementando o código central do jogo de dominó

# Importando as funções obrigatórias
from mandatory_functions import cria_pecas,inicia_jogo,verifica_ganhador,soma_pecas,posicoes_possiveis,adiciona_na_mesa
# Importando funções extras
from extra_functions import QUOTE,IMAGE,NAMES
# Importando e inicializando pygame para tocar música
import pygame as py
py.init()
py.mixer.init()
# Importando o módulo random
import random as r

# Introdução
py.mixer.music.load('sound/defaultsong.mp3') # --> carregando a música padrão
py.mixer.music.play(loops=-1) # música vai ficar tocando infinitamente no loop
print(IMAGE('insper'))
print('\nINSPER - Curso de Engenharia - 1° Semestre - 2021.2\nDisciplina: Design de Software\nProfessor: Humberto Sandmann\nAluno: Augusto Giuliani\nAtividade: Exercício Programa 2 - Jogo de Dominó')

# Mensagem inicial e escolha de nome
username = input('\nBem-vindo(a) ao meu jogo de dominó.\n\nShall we begin?\n\nPrimeiramente, escolha um nome para o seu usuário:')
print('\nBoa sorte {}!\n'.format(username))

# INICIANDO O JOGO - CRIANDO O LOOP GAME --> cada loop é um jogo diferente
GAME = True # ---> estado do jogo
while GAME:
# Escolhendo o número de jogadores
    print(IMAGE('question'))
    n = input('\nQuer jogar com quantos jogadores {}? 1, 2 ou 3?\n'.format(username))
    while n!='1' and n!='2' and n!='3': # Se o usuário der uma resposta inválida
        print(IMAGE('error'))
        print(QUOTE('invalid', username))
        n = input('Repetindo, quer jogar com quantos jogadores? 1,2 ou 3?\n')
    n = int(n)
    n+=1 # --> Número total de participantes no jogo, incluindo o usuário (humano)
# Criando a lista de peças e fazendo seu devido embaralhamento
    l_pieces = cria_pecas()
# Distribuindo 7 peças para cada jogador, criando monte e mesa (retorna dicionário com tudo isso)
    d_game = inicia_jogo(n,l_pieces)
# Quebrando o dicionário em diferentes variáveis
    players = d_game['jogadores'] # --> NOTE: O usuário é o jogador "0" desse dicionário
    table = d_game['mesa']
    storage = d_game['monte']
# Dando aos adversários do dicionário players com nomes
    l_names = NAMES(n-1)
    d_names = dict()
    director = 0
    for p in range(1,n):
        d_names[p] = l_names[director]
        director+=1
    print('\nSeus oponentes são:')
    for name in d_names.values():
        print(name)
# Um dos jogadores é aleatoriamente escolhido para iniciar o jogo
    player = r.randint(0,n-1)
# Criando variáveis
    ALERT = 0 # --> não ficar recomeçando música tensa
    alert = list() # --> lista que contém jogadores com menos de 3 peças
    DRAW = False # --> valor determina se houve um empate
    print('\nIniciando...\n')
    print(IMAGE('domino'))
    # INICIANDO A RODADA - CRIANDO O LOOP ROUND --> cada loop é uma rodada diferente 
    ROUND = True
    while ROUND:
        # Criando variável que contabiliza a quantidade de vezes na rodada que um jogador não colocou uma peça na mesa, já que foi pulada a sua vez
        skips = 0
        # INICIANDO A VEZ - CRIANDO O LOOP TURN --> cada loop é a vez de um jogador
        TURN = True
        while TURN:
        # Mostrando as peças sobre a mesa, as peças do usuário, a quantidade de peças no monte e a quantidade de peças do(s) outro(s) jogador(es)
            print('\nMESA:\n{}'.format(table))
            if player==0: # só mostra se for a vez do usuário (não ficar repetitivo)
                if len(players[0])<=2: # --> mensagem se estiver faltando poucas peças para ganhar o jogo
                    print(QUOTE('almost_there', username))
                print('\nQuantidade de peças...')
                if len(storage)!=0: # --> não mostra a quantidade de peças do monte se não houver monte
                    print('no MONTE: {}'.format(len(storage)))
                for i in range(1,n):
                    if len(players[i])<=2 and i not in alert: # --> não ficar adicionando os mesmos jogadores
                        alert.append(i)
                    print('do {}: {}'.format(d_names[i],len(players[i])))
                print('\nSuas peças:')
                for piece in players[0]:
                    print(piece)
        # Quando for a vez do usuário, dá um aviso se algum jogador estiver com menos de 3 peças
            if alert!=list() and player==0:
                if ALERT==0:
                    py.mixer.music.load('sound/tensesong.mp3') # --> carregando a música tensa
                    py.mixer.music.play(loops=-1)
                    ALERT = 1
                print(IMAGE('alert'))
                print('\nCUIDADO {}! Os seguintes jogadores estão com menos de 3 peças:'.format(username.upper()))
                for i in alert:
                    print('{}'.format(d_names[i]))
        # Verificando as peças possíveis (que podem ser colocadas na mesa) do jogador
            possibilities = posicoes_possiveis(table,players[player])
        # ----> SE NÃO HOUVER PEÇAS POSSÍVEIS
        # Se o jogador não tiver peças "possíveis", ele pega do monte até ter uma peça possível
            while possibilities == list() and storage!=list():
            # Se o jogador for o usuário
                if player==0:
                    print(QUOTE('no_piece',username))
                    input('Aperte a tecla "Enter" para apanhar uma peça do monte.')
            # Se o jogador não for o usuário
                elif player!=0:
                    print('\nO {} se deu mal, vai ter que pegar do monte.'.format(d_names[player]))
                players[player].append(storage[0])
                del storage[0] # --> apaga essa peça obtida do monte no monte
                possibilities = posicoes_possiveis(table,players[player]) # --> novamente verifica as peças possíveis
        # Se o jogador não tiver peças "possíveis" e não tiver monte, é a vez do próximo jogador
            if possibilities == list() and storage == list():
                if player==0:
                    input('\nUma pena {}. Como não há peças no monte, vamos ter que pular a sua vez.\nAperte a tecla "Enter" para continuar o jogo.'.format(username))
                elif player!=0:
                    print('\nComo não tem monte, vamos pular a vez do {}.'.format(d_names[player]))
                player+=1
                skips+=1
        # ----> SE HOUVER PEÇAS POSSÍVEIS
            if possibilities!=list():
            # Adicionando a peça na mesa 
            # Se o jogador for o usuário, ele escolhe qual peça colocar
                if player==0:
                # Mostrando para o usuário as posições de cada peça que ele pode usar
                    print('\nSua vez {}! Essas são as peças possíveis:'.format(username))
                    for i in possibilities:
                        print('{} --> {}'.format(i,players[player][i]))
                    chosen_piece = input('\nSelecione uma das posições possíveis:\n')
                    while not chosen_piece.isdigit() or int(chosen_piece) not in possibilities: # Se o usuário der uma resposta inválida
                        print(IMAGE('error'))
                        print(QUOTE('invalid',username))
                        chosen_piece = input('Repetindo, selecione uma das posições possíveis:\n')
                    chosen_piece = int(chosen_piece)
                # Atualizando a mesa com a peça escolhida
                    table = adiciona_na_mesa(players[player][chosen_piece],table)
                    del players[player][chosen_piece] # --> apaga essa peça da lista de peças que o jogador possui
            # Se o jogador não for o usuário
                if player!=0:
                    print('\nÉ a vez do {}.'.format(d_names[player]))
                    chosen_piece = r.choice(possibilities)
                    table = adiciona_na_mesa(players[player][chosen_piece],table)
                    del players[player][chosen_piece] # --> apaga essa peça da lista de peças que o jogador possui
            # Após um jogador ter adicionado uma peça na mesa, verifica-se se há um ganhador
                winner = verifica_ganhador(players)
                if winner==-1: # --> jogo continua e passa a vez para o próximo jogador
                    player+=1
                if winner!=-1: # --> acaba o loop TURN e ROUND
                    TURN = False
                    ROUND = False
            if player>=n: # --> verifica se o número player passou do número de participantes
                TURN = False
        player = 0 # --> reinicia a rodada
    # Se nenhum jogador colocou peças em toda uma rodada, encerra-se o jogo e, para efeito de vitória, conta-se os valores das faces das peças
        if skips==n:
            print('\nNenhum jogador colocou peças na rodada, então o jogo está encerrado e, para efeito de vitória, conta-se os valores das faces das peças de cada jogador. \nGanha o que tiver a menor soma desses valores.')
            # Imprimindo as peças dos jogadores
            for p in players:
                if p==0:
                    print('\nSuas peças {}:'.format(username))
                    for P in players[p]:
                        print (P)
                else:
                    print('\nPeças do {}:'.format(d_names[p]))
                    for P in players[p]:
                        print (P)
            ROUND = False
            d_points = dict() # --> dicionário que contém a soma dos valores das peças de cada jogador
            for pl,pis in players.items():
                d_points[pl] = soma_pecas(pis)
            # Determinando o menor valor (assumindo que o usuário possui o menor valor)
            smallest = d_points[0]
            for v in d_points.values():
                if v<=smallest:
                    smallest = v
            l_winners = list() # --> lista que contém vencedor(es)
            for p,v in d_points.items():
                if v==smallest:
                    l_winners.append(p)
            if len(l_winners)==1:
                winner = l_winners[0]
            # Em caso de empate
            if len(l_winners)!=1:
                DRAW = True
                # Se o usuário é um dos vencedores
                if 0 in l_winners: 
                    l_winners.remove(0)
                    L_winners = list()
                    for p in l_winners:
                        L_winners.append(p)
                    print('\nEMPATE! E você é um dos vencedores, junto com o(s) jogador(es):')
                    for p in L_winners:
                        print('{}'.format(d_names[p]))
                    print('\nParabéns! Mas será se dá para fazer melhor {}?'.format(username))
                else:
                    L_winners = list()
                    for p in l_winners:
                        L_winners.append(p)
                    print('\nEMPATE! Mas infelizmente você não é um dos vencedores. Os jogadores vencedores são:')
                    for p in L_winners:
                        print('{}'.format(d_names[p]))
                    print('\nSerá se dá para fazer melhor {}?'.format(username))
    # Mensagem de vitória/perda
    if winner==0 and not DRAW:
        py.mixer.music.load('sound/victorysong.mp3') # --> carregando a música de vitória
        py.mixer.music.play(loops=-1)
        print(IMAGE('happy'))
        print('\nWINNER WINNER CHICKEN DINNER! Parabéns {}! Você é o vencedor!\n'.format(username)) 
    if winner!=0 and not DRAW:
        py.mixer.music.load('sound/sadsong.mp3') # --> carregando a música triste
        py.mixer.music.play(loops=-1)
        print(IMAGE('sad'))
        print('\nVish {}... O {} ganhou. Talvez na próxima você ganhe.\n'.format(username,d_names[winner]))
    # Pergunta se o usuário quer jogar novamente
    print(IMAGE('question'))
    again = input('\nVamos jogar de novo {}? Digite S para SIM e N para NÃO:\n'.format(username))
    while again!='S' and again!='N': # Se o usuário der uma resposta inválida
        print(IMAGE('error'))
        print(QUOTE('invalid',username))
        again = input('Repetindo, digite S para SIM e N para NÃO por favor:\n')
    # Se a resposta for não, termina com o loop central
    if again=='N':
        GAME = False 
    if again=='S':
        print('\nExcelente {}! Vamos de novo...\n'.format(username))
        print(IMAGE('tryagain'))
        py.mixer.music.load('sound/defaultsong.mp3') # --> carregando a música padrão
        py.mixer.music.play(loops=-1)
# GoodBye
py.quit()
print('\nSem problemas. Nos vemos outro dia {}.\n'.format(username))
print(IMAGE('gameover'))