#!/usr/bin/env python3
import socket
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(('', 50000))	# Écoute sur le port 50000
serveur.listen(5)
while True:
	client, infosClient = serveur.accept()
	print("Client connecté. Adresse " + infosClient[0])
	requete = client.recv(255)	# Reçoit 255 octets. Vous pouvez changer pour recevoir plus de données
	print(requete.decode("utf-8"))
	reponse = "Bonjour, je suis le serveur"
	client.send(reponse.encode("utf-8"))
	print("Connexion fermée")
	client.close()
serveur.close()