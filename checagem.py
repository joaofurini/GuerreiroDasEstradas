class Checagem:
	def checkDecisao(self, resposta):
		
		while resposta!=1 and resposta!= 2:
			resposta = int(input("Digite apenas 1 ou 2 por favor:\n"))
		return resposta
