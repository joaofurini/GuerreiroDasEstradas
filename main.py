from player import Motorista
from random import randint
from carro import CarroMonstro



#Criacao do player
nome = input("Digite o seu nome: ")
habilidade = 6 + randint(0,6)
energia = 24 + (randint(0,6) + randint(0,6))
sorte = 6 + randint(0,6)
player = Motorista(nome, habilidade, energia, sorte)
player.criaPlayer()
player.mostraEstado()

poderDeFogo = 6 + randint(0,6)
blindagem = 24 + (randint(0,6) + randint(0,6))
carro = CarroMonstro(poderDeFogo, blindagem)

carro.mostraEstado()
