from random import randint
import time 
class Motorista:

	def __init__(self, nome):
		self.__nome = nome
		self.__habilidade =  6 + randint(0,6)
		self.__energia = 24 + (randint(0,6) + randint(0,6))
		self.__sorte =  6 + randint(0,6)
		self.__kitMedico  = 1
		self.__dinheiro = 200
		self.__player= {
			"Habilidade": self.__habilidade,
			"Energia": self.__energia,
			"Sorte": self.__sorte,
			"KitMedico": self.__kitMedico,
			"Dinheiro": self.__dinheiro
		}
		
	
	#Metodos get 
	def getNome(self):
		return self.__nome

	def getHabilidade(self):
		return self.__habilidade

	def getEnergia(self):
		return self.__energia

	def getSorte(self):
		return self.__energia 

	def getKit(self):
		return self.__sorte

	def getCreditos(self):
		return self.__creditos

		#SETTERS
	def setHabilidade(self, value):
		habilidadeInicial = self.__habilidadeInicial
		if value <= self.__habilidadeInicial:
			self.__habilidade = value
		else:
			self.__habilidade = habilidadeInicial

	def setEnergia(self, value):
		energiaInicial = self.__energiaInicial
		if value <= self.__energiaInicial:
			self.__energia = value
		else:
			self.__energia = energiaInicial
		
	def setSorte(self, value):
		sorteInicial = self.__sorteInicial
		if value <= self.__sorte :
			self.__sorte = value
		else: 
			self.__sorte = sorteInicial 
		
	def setKit(self, value):
		self.__kitMedico = value

	def gastaDinheiro(self, value):
		self.__dinheiro -= value

	#METHODS
	def mostraEstado(self):
		print("Atualmente voce esta no seguinte estado")

		for key, value in self.__player.items():
			print('{} - {}'.format(key, value))

	def perdeuRound(self):
		self.__energia  -=1
		

	def usaKit(self):
		self.__energia  +=4
		self.__kitMedico -=1 

	def testYourLuck(self):
		resutadoDados = randint(0,6) + randint(0,6)
		if resultadoDados > self.__sorte :
			return False
		else: 
			return True
		self.__sorte  -= 1

	def criaPlayer(self):
		rolldice = "\nROLANDO DADOS..."
		for key, value in self.__player.items():
			print(rolldice)
			time.sleep(1.6)
			print('\n{} Inicial: {}'.format(key, value))
			time.sleep(1)
			
			


		'''rolldice= "\nROLANDO DADOS..."
								print(rolldice)
								time.sleep(1.6)
								print("\nENERGIA INICIAL: "+ str(self.__energia))
								time.sleep(1)
								print(rolldice)
								time.sleep(1.6)
								print("\nHABILIDADE INICIAL: " + str(self.__habilidade))
								time.sleep(1)
								print(rolldice)
								time.sleep(1.6)
								print("\nSORTE INICIAL: "+ str(self.__sorte))
								time.sleep(1)
						'''

	def tomaTiro(self):
		danoTiro = randint(0, 6)
		dice = randint(0,6)

		if danoTiro == 0:
			print("O inimigo teria acertado se voce nao tivesse desviado de ultima hora ")
			print("Voce tomou {} de dano".format(danoTiro))
			time.sleep(1.5)
		elif danoTiro == 6 and dice <=5:
			self.__energia =0
			print("O inimigo em um movimento inesperado te deu um tiro na cabeca")
			time.sleep(1.5)
		else:
			self.__energia -= danoTiro
			print("\nVOCE TOMOU UM TIRO")
			print("e perdeu {} de energia".format(danoTiro) )
			time.sleep(1.5)



