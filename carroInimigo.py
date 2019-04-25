from random import randint
import time

class CarroInimigo:

	def __init__(self, poderDeFogo, blindagem):
		self.__carro = {
			"Poder De Fogo": poderDeFogo,
			"Blindagem": blindagem
		}
	def getPoderDeFogo(self):
		return self.__carro['Poder De Fogo']

	def getBlindagem(self):
		return self.__carro['Blindagem']

	def tomaTiro(self):
		danoTiro = randint(0, 6)
		
		if danoTiro == 0:
			print("A blindagem do inimigo foi mais forte")
			print("Voce deu {} de dano".format(danoTiro))
			time.sleep(1.5)
		else:
			self.__carro['Blindagem'] -= danoTiro
			print("\nVOCE ACERTOU TIROS NO CARRO DO INIMIGO")
			print("e tirou {} da blindagem dele".format(danoTiro))
			time.sleep(1.5)




		




