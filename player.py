from random import randint
import time 
class Motorista:

	def __init__(self, nome):
		self.__player= {
			"Nome": nome,
			"Habilidade": 6 + randint(0,6),
			"Energia":24 + (randint(0,6) + randint(0,6)),
			"Sorte": 6 + randint(0,6),
			"Kit Medico": 1,
			"Dinheiro": 200
		}
		
		self.__habilidadeInicial = self.__player['Habilidade']
		self.__energiaInicial = self.__player['Energia']
		self.__sorteInicial = self.__player['Sorte']
		
	#Metodos get 
	def getNome(self):
		return self.__player['Nome']

	def getHabilidade(self):
		return self.__player['Habilidade']

	def getEnergia(self):
		return self.__player['Energia']

	def getSorte(self):
		return self.__player['Sorte']

	def getKit(self):
		return self.__player['Kit Medico']

	def getCreditos(self):
		return self.__player['Dinheiro']

		#SETTERS
	def setHabilidade(self, value):

		if value <= self.__habilidadeInicial:
			self.__player['Habilidade'] = value
		else:
			self.__player['Habilidade'] = self.__habilidadeInicial

	def setEnergia(self, value):

		if value <= self.__energiaInicial:
			self.__player['Energia'] = value
		else:
			self.__player['Energia'] = self.__energiaInicial

	def setSorte(self, value):

		if value <= self.__sorteInicial:
			self.__player['Sorte'] = value
		else:
			self.__player['Sorte'] = self.__sorteInicial

	def ganhaKit(self, value):
		self.__player['Kit Medico'] += value

	def perdeKit(self, value):
		self.__player['Kit Medico'] -= value

	def gastaDinheiro(self, value):
		self.__player['Dinheiro'] -= value

	def gastaDinheiro(self, value):
		self.__player['Dinheiro'] += value

	#METHODS
	def mostraEstado(self):
		print("\n==========================================================")
		print("ATUALMENTE VOCE SE ENCONTRA NO SEGUINTE ESTADO:")
		for key, value in self.__player.items():
			print('{} - {}'.format(key, value))
		print("\n==========================================================")

	def perdeuRound(self):
		self.__player['Energia'] -=1
		

	def usaKit(self):
		self.__player['Energia']  +=4
		self.__player['Kit Medico'] -=1 

	def testYourLuck(self):
		resutadoDados = randint(0,6) + randint(0,6)
		if resultadoDados > self.__player['Sorte'] :
			return False
		else: 
			return True
		self.__player['Sorte']  -= 1

	def criaPlayer(self):
		rolldice = "\nROLANDO DADOS..."
		for key, value in self.__player.items():
			print(rolldice)
			time.sleep(1.6)
			print('\n{} Inicial: {}'.format(key, value))
			time.sleep(1)
			

	def tomaTiro(self):
		danoTiro = randint(0, 6)
		dice = randint(0,6)

		if danoTiro == 0:
			print("O inimigo teria acertado se voce nao tivesse desviado de ultima hora ")
			print("Voce tomou {} de dano".format(danoTiro))
			time.sleep(1.5)
		elif danoTiro == 6 and dice <=5:
			self.__player['Energia'] =0
			print("O inimigo em um movimento inesperado te deu um tiro na cabeca")
			time.sleep(1.5)
		else:
			self.__player['Energia'] -= danoTiro
			print("\nVOCE TOMOU UM TIRO")
			print("e perdeu {} de energia".format(danoTiro) )
			time.sleep(1.5)



