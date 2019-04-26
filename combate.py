from random import randint 
import time

#CRIAR A CHEGAGEM PARA O LANCAMENTO DE MISSEIS

def printBatalhaComDado(linhas):
		"""
			Padroniza output

			:param linhas: Mensagens a serem exibidas
			:type linhas: list
		"""
		print("___________________________________________________________________")
		print("\nROLANDO OS DADOS...")
		time.sleep(1)
		for linha in linhas:
			print(linha)
		print("___________________________________________________________________")


class Batalha:
	def __init__(self):
		self.playerPerdido = 0



	def estadoRound(self, player, inimigo):
		"""
			Calcula o vencedor da batalha

			:param forcaAtaquePlayer: Ataque
			:type forcaAtaquePlayer: list
		"""
		payload = []
		forcaAtaqueInimigo = inimigo.getHabilidade() + (randint(0,6) + randint(0,6))
		forcaAtaquePlayer = player.getHabilidade() + (randint(0,6) + randint(0,6))
		if forcaAtaquePlayer > forcaAtaqueInimigo:
			payload.append("VENCEU")
		elif forcaAtaqueInimigo> forcaAtaquePlayer:
			self.playerPerdido += 1
			player.perdeuRound()
			payload.append("PERDEU")
		elif forcaAtaquePlayer == forcaAtaqueInimigo:
			payload.append("EMPATOU")
		payload.append([forcaAtaqueInimigo, forcaAtaquePlayer])
		return payload

	

	def corpoACorpo(self, player, inimigo):
		partidas = 0
		estadoPartida = False
		
		while True:
			payload = self.estadoRound(player, inimigo)
			if payload[0] != "EMPATOU":
				partidas += 1
			printBatalhaComDado(["\nATAQUE INIMIGO:{} ".format(payload[1][0]), \
								 "\nSEU ATAQUE:{} ".format(payload[1][1])])

			print("\n [ROUND {}] -> VOCE {}!!!".format(partidas, payload[0]))

			if partidas >= 6:
				if self.playerPerdido >= 6:
					print("\nVOCE PERDEU A LUTA")
					break
				elif partidas - self.playerPerdido  >= 6:
					print("\nVOCE VENCEU A LUTA")
					estadoPartida = True
					break
			
		self.playerPerdido = 0
		return estadoPartida

	def bangBang(self, player, inimigo):

		rolldice = "\nROLANDO OS DADOS..."
		while (player.getEnergia()!=0) and (inimigo.getEnergia() != 0):
			print("___________________________________________________________________")
			print(rolldice) 
			time.sleep(1)
			forcaAtaqueInimigo = inimigo.getHabilidade() + (randint(0,6) + randint(0,6))
			forcaAtaquePlayer = player.getHabilidade() + (randint(0,6) + randint(0,6))
			print("\nATAQUE INIMIGO:{} ".format(forcaAtaqueInimigo))
			print("\nSEU ATAQUE:{} ".format(forcaAtaquePlayer))
			print("___________________________________________________________________")
			
			if forcaAtaqueInimigo > forcaAtaquePlayer:
				player.tomaTiro()
				time.sleep(1.5)
				
			elif forcaAtaquePlayer > forcaAtaqueInimigo:
				inimigo.tomaTiro()
				time.sleep(1.5)

			elif forcaAtaquePlayer == forcaAtaqueInimigo:
				print("Voces dois erraram")

			if player.getEnergia() <= 0:
				print("VOCE ESTA MORTO")
				print("___________________________________________________________________")
				return False

			if inimigo.getEnergia()<=0:
				print("VOCE MATOU O INIMIGO")
				print("___________________________________________________________________")
				return True

	def carBattle(self, carro, carroInimigo):
		missel =False
		rolldice = "\nROLANDO DADOS"

		while ((carro.getBlindagem()!=0) and (carroInimigo.getBlindagem()!= 0)) and missel == False:
			if carro.getMisseis() > 0:
				lancarMissel = input("\nDeseja lancar um missel? s/n")
				if carro.getMisseis()>0 and lancarMissel == 's':
					print("Voce explodiu o inimigo")
					carro.lancaMissel()
					break
			else:
				pass

			print("\n___________________________________________________________________")
			print(rolldice) 
			time.sleep(1)
			forcaAtaqueInimigo = carroInimigo.getPoderDeFogo() + (randint(0,6) + randint(0,6))
			forcaAtaquePlayer = carro.getPoderDeFogo() + (randint(0,6) + randint(0,6))
			print("\nATAQUE INIMIGO:{} ".format(forcaAtaqueInimigo))
			print("\nSEU ATAQUE:{} ".format(forcaAtaquePlayer))
			print("___________________________________________________________________")

			
			if forcaAtaqueInimigo > forcaAtaquePlayer:
				carro.tomaTiro()
			
				print("\n=========================")
				print("Sua blindagem atual: {}".format(carro.getBlindagem()))
				print("blindagem do inimigo: {}".format(carroInimigo.getBlindagem()))
				print("=========================")
				time.sleep(1.5)
					
			elif forcaAtaquePlayer > forcaAtaqueInimigo:
				carroInimigo.tomaTiro()
				print("\n=========================")
				print("Sua blindagem atual: {}".format(carro.getBlindagem()))
				print("blindagem do inimigo: {}".format(carroInimigo.getBlindagem()))
				print("===========================")
				time.sleep(1.5)

			elif forcaAtaquePlayer == forcaAtaqueInimigo:
				print("\nVOCES DOIS ERRARAM")

			if carro.getBlindagem() <= 0:
				print("O SEU CARRO CAPOTOU")
				print("VOCE ESTA MORTO")
				print("___________________________________________________________________")
				return False

			if carroInimigo.getBlindagem()<=0:
				print("O CARRO DO INIMIGO CAPOTOU E EXPLODIU")
				print("VOCE VENCEU ESSA BATALHA")
				print("___________________________________________________________________")
				return True

		










				

	























