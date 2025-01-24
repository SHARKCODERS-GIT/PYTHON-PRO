from random import randint
import Play_mp3
from time import sleep
import emoji


pc=randint(0,1) #varialvel de randomizar
user=int(input("Qual numero entre 0 e 5 eu estou pensando? "))
print()
print("Processando ....")
print()
sleep(2)
#condicional
if user==pc:
    print(emoji.emojize('Parabéns você acertou :thumbs_up:'))
else:
    print("Voce errou!")
    Play_mp3.play("bang.WAV")