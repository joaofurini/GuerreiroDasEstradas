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

		#METODOS SETTERS
	def mostraEstado(self):
		print("\nSEU CARRO SE ENCONTRA NO SEGUINTE ESTADO: ")
		print("Poder de fogo: "+str(self.__poderDeFogo)+ "\nBlindagem: "+str(self.__blindagem) +\
				"\nMisses: "+ str(self.__misseis) + "\nAcessorios: "+ str(self.__acessorios))


		
