# Arquivo com a função que insere imagens
import climage
def IMAGE(situation):
    if situation == 'alerta':
        return climage.convert('image/alert.png', is_unicode=True, width = 50)
    elif situation == 'domino':
        return climage.convert('image/dominopiece.png', is_unicode=True, width = 80)
    elif situation == 'error':
        return climage.convert('image/error.png', is_unicode=True, width = 40)
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



        


