# Arquivo com a função que insere diferentes frases
import random as r

def QUOTE(situation,username):
    if situation == 'invalid':
        l = ['\nRESPOSTA INVÁLIDA! PRESTA ATENÇÃO {}!'.format(username.upper()), '\nO que você digitou não faz sentido. Leia novamente {}.'.format(username.upper()),'\nEstá nervoso(a) {}? Sentindo a pressão? Leia direito por gentileza.'.format(username.upper())]
        return r.choice(l)
    elif situation == 'almost_there':
        l = ['\nFalta pouco {}! Não desista...'.format(username),'\nA vitória está perto {}! Tenha paciência.'.format(username),'\nSua mão está quase vazia {}! Vamos lá!'.format(username)]
        return r.choice(l)
    elif situation == 'no_piece':
        l = ['\nEita! Você vai ter que pegar uma peça do monte.','\nInfelizmente você não tem peças para adicionar na mesa.','\nFique calma {}, mas você vai ter que pegar uma peça do monte.'.format(username)]
        return r.choice(l)
    
        
