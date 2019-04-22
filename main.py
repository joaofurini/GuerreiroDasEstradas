from player import Motorista
from random import randint
from carro import CarroMonstro
from inimigo import Inimigo
from combate import Batalha
from carroInimigo import CarroInimigo
from historia import *

#BREVE INTRODUCAO
caimpaing = Historia()

print(caimpaing.introducao())

#CRIACAO DO JOGADOR
nome = input("\nDigite o seu nome: ")
player = Motorista(nome)
player.criaPlayer()
player.mostraEstado()
#CRIACAO DO CARRO DO JOGADOR 
carro = CarroMonstro()
carro.mostraEstado()



