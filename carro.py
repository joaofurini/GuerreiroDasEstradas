from random import randint
import time
class CarroMonstro:
	def __init__(self, poderDeFogo, blindagem):
		self.__poderDeFogo = poderDeFogo
		self.__blindagem = blindagem
		self.__combustivel = 100
		self.__misseis = 4
		self.__acessorios = []

		#METODOS DE ACESSO
	def getPoderDeFogo(self):
		return self.__poderDeFogo

	def getBlindagem(self):
		return self.__blindagem

	def getCombustivel(self):
		return self.__combustivel

	def getAcessorios(self):
		return self.__acessorios

	def getMisseis(self):
		return self.__misseis

		#METODOS SETTERS
	def mostraEstado(self):
		print("\nSEU CARRO SE ENCONTRA NO SEGUINTE ESTADO: ")
		print("Poder de fogo: "+str(self.__poderDeFogo)+ "\nBlindagem: "+str(self.__blindagem) +\
				"\nMisses: "+ str(self.__misseis) + "\nAcessorios: "+ str(self.__acessorios))

	def lancaMissel(self):
		self.__misseis -=1

	def setMisseis(self, value):
		self.__misseis += value


	def tomaTiro(self):
		danoTiro = randint(0, 6)
		if danoTiro == 0:
			print("A sua blindagem foi mais forte")
			print("Voce tomou {} de dano".format(danoTiro))
			time.sleep(1.5)
		else:
			self.__blindagem -= danoTiro
			print("\nO INIMIGO ACERTOU TIROS NO SEU CARRO")
			print("e tirou {} de sua blindagem".format(danoTiro) )
			time.sleep(1.5)
