from random import randint
import time 
class Motorista:

	def __init__(self, nome, habilidade, energia, sorte):
		self.__nome = nome
		self.__habilidade = habilidade
		self.__energia = energia
		self.__sorte = sorte
		self.__kitMedico  = 1
		self.__dinheiro = 200

	
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

	def setDinheiro(self, value):
		self.__dinheiro = value

	#METHODS
	def mostraEstado(self):
		print("\n________________________________________________________________________")
		print("\nATUALMENTE VOCE SE ENCONTRA NO SEGUINTA ESTADO:")
		print("________________________________________________________________________")
		print ("\nENERGIA: "+str(self.__energia )+"\nHABILIDADE: "+ str(self.__habilidade )+ \
		"\nSORTE: "+ str(self.__sorte )+"\nPOSSUI "+str(self.__kitMedico )+ " KIT MEDICO" +\
		"\nDINHEIRO: " + str(self.__dinheiro) +\
		"\n________________________________________________________________________")


	def perdeuRound(self):
		self.__energia  -=1
		return self.__energia 

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
		rolldice= "\nROLANDO DADOS..."
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


