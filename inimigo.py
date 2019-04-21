class Inimigo:
	def __init__(self, habilidade, energia):
		self.__habilidade = habilidade
		self.__energia = energia
		

	def getHabilidade(self):
		return self.__habilidade

	def getEnergia(self):
		return self.__energia

	def setEnergia(self, value):
		self.__energia = value
		
	def perdeuRound(self):
		self.__energia -=1
		return self.__energia


