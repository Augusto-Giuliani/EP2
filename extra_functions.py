# Arquivo com a função que insere diferentes frases, imagens e nomes
import random as r
import climage

def QUOTE(situation,username):
    if situation == 'invalid':
        l = ['\nRESPOSTA INVÁLIDA! PRESTA ATENÇÃO {}!'.format(username.upper()), '\nO que você digitou não faz sentido. Leia novamente {}.'.format(username),'\nEstá nervoso(a) {}? Sentindo a pressão? Leia direito por gentileza.'.format(username)]
        return r.choice(l)
    elif situation == 'almost_there':
        l = ['\nFalta pouco {}! Não desista...'.format(username),'\nA vitória está perto {}! Tenha paciência.'.format(username),'\nSua mão está quase vazia {}! Vamos lá!'.format(username)]
        return r.choice(l)
    elif situation == 'no_piece':
        l = ['\nEita! Você vai ter que pegar uma peça do monte.','\nInfelizmente você não tem peças para adicionar na mesa.','\nFique calma {}, mas você vai ter que pegar uma peça do monte.'.format(username)]
        return r.choice(l)

def IMAGE(situation):
    if situation == 'alert':
        return climage.convert('image/alert.png', is_unicode=True, width = 30)
    elif situation == 'domino':
        return climage.convert('image/dominopiece.png', is_unicode=True, width = 60)
    elif situation == 'error':
        return climage.convert('image/error.png', is_unicode=True, width = 30)
    elif situation == 'gameover':
        return climage.convert('image/gameover.jpg', is_unicode=True, width = 100)
    elif situation == 'happy':
        return climage.convert('image/happyface.jpg', is_unicode=True, width = 80)
    elif situation == 'insper':
        return climage.convert('image/insperblack.png', is_unicode=True, width = 60)
    elif situation == 'question':
        return climage.convert('image/questionmark.png', is_unicode=True, width = 30)
    elif situation == 'sad':
        return climage.convert('image/sadface.jpg', is_unicode=True, width = 80)
    elif situation == 'tryagain':
        return climage.convert('image/tryagain.png', is_unicode=True, width = 60)

def NAMES(n):
    names = ['Christopher Nolan', 'David Fincher', 'Denis Villeneuve', 'Martin Scorsese', 'Steven Spielberg', 'Quentin Tarantino', 'James Cameron']
    l_names = list()
    for i in range(n):
        name = r.choice(names)
        if name not in l_names:
            l_names.append(name)
    return l_names

        
