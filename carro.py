from random import randint
import time
class CarroMonstro:
	def __init__(self):

		self.__carro = {
			"Poder De Fogo": 6 + randint(0,6),
			"Blindagem": 24 + (randint(0,6) + randint(0,6)),
			"Combustivel": 100,
			"Misseis": 4,
			"Acessorios": [],
		}

		#METODOS DE ACESSO
	def getPoderDeFogo(self):
		return self.__carro['Poder De Fogo']

	def getBlindagem(self):
		return self.__carro['Blindagem']

	def getCombustivel(self):
		return self.__carro['Combustivel']

	def getAcessorios(self):
		return self.__carro['Acessorios']

	def getMisseis(self):
		return self.__carro['Misseis']

		#METODOS SETTERS
	def mostraEstado(self):
		print("\n==========================================================")
		print("ATUALMENTE O SEU CARRO SE ENCONTRA NO SEGUITNE ESTADO: ")
		for key, value in self.__carro.items():
			print('{} - {}'.format(key, value ))
		print("==========================================================")

	def lancaMissel(self):
		self.__carro['Misseis'] -=1

	def setMisseis(self, value):
		self.__carro['Misseis'] += value


	def tomaTiro(self):
		danoTiro = randint(0, 6)
		if danoTiro == 0:
			print("A sua blindagem foi mais forte")
			print("Voce tomou {} de dano".format(danoTiro))
			time.sleep(1.5)
		else:
			self.__carro['Blindagem'] -= danoTiro
			print("\nO INIMIGO ACERTOU TIROS NO SEU CARRO")
			print("e tirou {} de sua blindagem".format(danoTiro) )
			time.sleep(1.5)
