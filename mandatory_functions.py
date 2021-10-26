#Implementando as funções obrigatórias (oriundas dos exercícios na Academia Python)

# ---> CRIANDO PEÇAS DE DOMINÓ:
import random as r
def cria_pecas():
    answer = list()
    a = 0
    # Enquanto a lista a ser retornada não atingir a quantidade de 28 peças
    while len(answer)<28:
        b = 0
        while b<=6:
            piece = [a,b]
        # Testa o inverso também (que no dominó seria a mesma peça)
            tenet = [b,a] 
            if piece not in answer and tenet not in answer:
                answer.append(piece)
            b+=1
        a+=1
    # Embaralha
    r.shuffle(answer)
    return answer 
# ---> INICIANDO O JOGO DE DOMINÓ:
def inicia_jogo(n,pieces):
    answer = dict()
    players_d = dict()
    used_pieces = list()
    storage = list()
    table = list()
    i = 0
    for player in range(n):
        I = 0
        players_l = list()
    # Distribui 7 peças para cada jogador
        while I<7:
            players_l.append(pieces[i+I])
            I+=1
        i+=I 
        players_d[player] = players_l
    # Adiciona as peças já distribuídas numa lista 
        used_pieces+=players_l
    # Se tiver resto, joga no monte as peças já distrubuídas
    for piece in pieces:
        if piece not in used_pieces:
            storage+=[piece]
    # Criando o dicionário que deve ser retornado
    answer['jogadores'] = players_d
    answer['monte'] = storage
    answer['mesa'] = table
    return answer
# ---> QUEM GANHOU NO DOMINÓ?:
def verifica_ganhador(d_players):
    # Verifica quem não tem peças (lista vai ser vazia)
    for player,pieces in d_players.items():
        if pieces==list():
            return player
    # Se não tiver um ganhador
    return -1
# ---> SOMA PEÇAS DO DOMINÓ:
def soma_pecas(l_player_pieces):
    answer = 0
    # Somando os valores de face de todas as peças do jogador
    for piece in l_player_pieces:
        answer+=sum(piece)
    return answer
# ---> POSIÇÕES POSSÍVEIS DA MÃO:
def posicoes_possiveis(table,l_pieces):
    answer = list()
    # Se a mesa estiver vazia
    if table==list():
        for i in range(len(l_pieces)):
            answer.append(i)
        return answer
    # Obtendo os valores das pontas da mesa
    ends = [table[0][0],table[-1][-1]]
    i = 0
    # Verifica as posições possíveis
    for piece in l_pieces:
        if ends[0] in piece or ends[1] in piece:
            answer.append(i)
        i+=1
    return answer
# ---> ADICIONANDO PEÇAS A MESA NUM JOGO DE DOMINÓ:
def adiciona_na_mesa(piece,l_table):
    # Se a mesa estiver vazia
    if l_table==list():
        l_table.append(piece)
        return l_table
    # Gerando condições para diferentes cenários
    if piece[0]==l_table[0][0]:
        piece.reverse()
        return [piece] + l_table
    if piece[1]==l_table[0][0]:
        return [piece] + l_table
    if piece[0]==l_table[-1][-1]:
        return l_table + [piece]
    if piece[1]==l_table[-1][-1]:
        piece.reverse()
        return l_table + [piece]