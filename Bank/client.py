#!/usr/bin/env python3
import socket

adresseIP = "127.0.0.1"	# Ici, le poste local
port = 50000	# Se connecter sur le port 50000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((adresseIP, port))
print("Connecté au serveur")

pin = int(input("Entrez votre code PIN : "))
action = str(input("\nEntrez l action à effectuer : \nR pour RETRAIT \nD pour DEPOT \nT pour TRANSFERT \nS pour SOLDE \nH pour HISTORIQUE\nP pour TESTPIN\n"))
message = ""
match action:
	#case "R":
		
   #case "D":

   #case "T":

   #case "S":

   #case "H":

   case _:
      account_nb = str(input("Entrez votre numéro de compte : "))
      message = str(pin)+";"+"TESTPIN"+";"+account_nb
      client.send(message.encode("utf-8"))
      reponse = client.recv(255)
      print(reponse.decode("utf-8"))

#RETRAIT numeroCompte montant (C→S) : Demande un retrait du montant défini.
#DEPOT numeroCompte montant (C→S) : Demande un dépôt du montant défini.
#TRANSFERT numeroCompteSource numeroCompteDestination montant (C→S) : Demande un transfert du montant défini entre deux comptes.
#SOLDE numeroCompte (C→S) : Demande le solde du compte
#HISTORIQUE numeroCompte (C→S) : Demande les 10 dernières opérations du compte
#ERROPERATION (S→C) : Signale que l'opération demandée n'est pas valide.")
#print("Tapez FIN pour terminer le programme. ")

#while message.upper() != "FIN":
	#message = input("> ")
	#client.send(message.encode("utf-8"))
	#reponse = client.recv(255)
	#print(reponse.decode("utf-8"))
print("Connexion fermée")
client.close()