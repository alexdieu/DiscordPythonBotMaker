
from googletrans import Translator

client = Translator()

def translate(target,text):
    try:
        return client.translate(f'{text}', dest=f'{target.lower()}').text
    except:
        return "Erreur https://tenor.com/view/erreur-pierre-bellemare-gif-7878816"
