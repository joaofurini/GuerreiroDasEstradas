from player import Motorista
from random import randint
from carro import CarroMonstro
from inimigo import Inimigo
from combate import Batalha
from carroInimigo import CarroInimigo

#BREVE INTRODUCAO
print("\n___________________BOLETIM DA VID NEWS_________________")
print("___________________DATA 21 DE JULHO DE 2022____________")
print("\nO desastre aconteceu justamente quando o mundo estava comecando a melhorar. \nNinguem poderia ter previsto essa catastrofe." +\
	"A Terceira Guerra Mundial havia \nsido evitada e os blocos economicos estavam trabalhando juntos pela paz e unidade mundial"+\
	"\nVAMOS LA")
#CRIACAO DO JOGADOR
nome = input("\nDigite o seu nome: ")
habilidade = 6 + randint(0,6)
energia = 24 + (randint(0,6) + randint(0,6))
sorte = 6 + randint(0,6)
player = Motorista(nome, habilidade, energia, sorte)
player.criaPlayer()
player.mostraEstado()
#CRIACAO DO CARRO DO JOGADOR
poderDeFogo = 6 + randint(0,6)
blindagem = 24 + (randint(0,6) + randint(0,6))
carro = CarroMonstro(poderDeFogo, blindagem)
carro.mostraEstado()



