from random import randint 
import time

class Batalha:
	def corpoACorpo(player, inimigo):
		rolldice = "\nROLANDO OS DADOS..."
		playerPerdido = 0
		inimigoPerdido = 0
		
		while playerPerdido < 6 and inimigoPerdido < 6:
			print("___________________________________________________________________")
			print(rolldice) 
			time.sleep(1)
			forcaAtaqueInimigo = inimigo.getHabilidade() + (randint(0,6) + randint(0,6))
			forcaAtaquePlayer = player.getHabilidade() + (randint(0,6) + randint(0,6))
			print("\nATAQUE INIMIGO:{} ".format(forcaAtaqueInimigo))
			print("\nSEU ATAQUE:{} ".format(forcaAtaquePlayer))
			time.sleep(1)
			print("___________________________________________________________________")

			if forcaAtaquePlayer > forcaAtaqueInimigo:
				inimigoPerdido += 1
				print('\nVOCE VENCEU ESSE ROUND')
			elif forcaAtaqueInimigo> forcaAtaquePlayer:
				playerPerdido += 1
				player.perdeuRound()
				print('\nVOCE PERDEU ESSE ROUND')
			elif forcaAtaquePlayer == forcaAtaqueInimigo:
				print("\nVOCES EMPATARAM ESSE ROUND")

		if playerPerdido == 6:
			print("\nVOCE PERDEU A LUTA")
			return False

		elif inimigoPerdido == 6:
			print("\nVOCE VENCEU A LUTA")
			return True

	def bangBang(player, inimigo):

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

	def carBattle(carro, carroInimigo):
		missel =False
		rolldice = "\nROLANDO DADOS"

		while ((carro.getBlindagem()!=0) and (carroInimigo.getBlindagem()!= 0)) and missel == False:
			if carro.getMisseis() > 0:
				lancarMissel = input("Deseja lancar um missel? s/n")
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
				time.sleep(1.5)
				print("___________________________________________________________________")
				print("\nA sua blidnagem atual: {}".format(carro.getBlindagem()))
				print("\nblindagem do inimigo: {}".format(carroInimigo.getBlindagem()))
					
			elif forcaAtaquePlayer > forcaAtaqueInimigo:
				carroInimigo.tomaTiro()
				print("\nA sua blidnagem atual: {}".format(carro.getBlindagem()))
				print("\nblindagem do inimigo: {}".format(carroInimigo.getBlindagem()))
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

		










				

	























