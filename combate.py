from random import randint 

class Batalha:
	def corpoACorpo(player, inimigo):
		forcaAtaqueInimigo = inimigo.getHabilidade() + (randint(0,6) + randint(0,6))
		forcaAtaquePlayer = player.getHabilidade() + (randint(0,6) + randint(0,6))
		



