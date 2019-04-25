from random import randint
import time
class Inimigo:
	def __init__(self, habilidade, energia):

		self.__inimigo= {
			"Habilidade": habilidade,
			"Energia": energia
		}
		self.__habilidade = habilidade
		self.__energia = energia
		

	def getHabilidade(self):
		return self.__inimigo['Habilidade']

	def getEnergia(self):
		return self.__inimigo['Energia']

	def setEnergia(self, value):
		self.__inimigo['Energia'] = value

	def perdeuRound(self):
		self.__inimigo['Energia'] -=1
		
	def mostraEstado(self):
		print("\n==========================================================")
		print("ATUALMENTE SEU INIMIGO SE ENCONTRA NO SEGUINTE ESTADO:")
		for key, value in self.__inimigo.items():
			print('{} - {}'.format(key, value))
		print("\n==========================================================")

	def tomaTiro(self):
		danoTiro = randint(0, 6)
		if danoTiro == 0:
			print("Voce teria acertado se o inimigo nao tivesse desviado de ultima hora ")
			print("Voce tirou {} de dano".format(danoTiro))
			time.sleep(1.5)

		elif danoTiro == 6:
			self.__inimigo['Energia'] =0
			print("Voce acertou um tiro na cabeca do inimigo e ele esta morto")
		else:
			self.__inimigo['Energia'] -= danoTiro
			print("\nVOCE ACERTOU UM TIRO")
			print("e tirou {} de energia do inimigo".format(danoTiro))





