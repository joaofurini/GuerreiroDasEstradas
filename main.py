from player import Motorista
from random import randint
from carro import CarroMonstro
from inimigo import Inimigo
from combate import Batalha
from carroInimigo import CarroInimigo
from checagem import Checagem
from historia import *

#BREVE INTRODUCAO
check = Checagem()
caimpaing = Historia()

decisao = check.checkDecisao(int(input("{}\n".format(caimpaing.Historia[1]))))

if decisao == 1:
	decisao = check.checkDecisao(int(input("{}\n".format(caimpaing.Historia[126]))))
	if decisao == 1:
		print(caimpaing.Historia[274])
		decisao = check.checkDecisao(int(input('{}\n'.format(caimpaing.Historia[34]))))
	else:
		decisao = check.checkDecisao(int(input('{}\n'.format(caimpaing.Historia[155]))))
		if decisao == 1:
			print(caimpaing.Historia[219])
		else:
			print(caimpaing.Historia[333])

else: 
	decisao = check.checkDecisao(input(caimpaing.Historia[34]))
	if decisao == 1:
		decisao = check.checkDecisao(input(caimpaing.Historia[302]))
		if decisao == 1:
			decisao = check.checkDecisao(int(input(caimpaing.Historia[209])))
		else:
			decisao = check.checkDecisao(int(input(caimpaing.Historia[48])))
	else:
		print(caimpaing.Historia[188])
	

#CRIACAO DO JOGADOR
nome = input("\nDigite o seu nome: ")
player = Motorista(nome)
oponente = Inimigo(10, 10)

carro = CarroMonstro()
carroInimigo = CarroInimigo(10, 10)

Batalha.carBattle(carro, carroInimigo)

player.criaPlayer()
player.mostraEstado()
#CRIACAO DO CARRO DO JOGADOR 
carro = CarroMonstro()

'''carro.mostraEstado()'''



