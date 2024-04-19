import sqlite3
import os
from pathlib import Path
import pandas as pd
import socket
import threading 

def init_db():
   if(not os.path.isfile("banque.db")):
      Path('banque.db').touch()
   connection = sqlite3.connect("banque.db")
   print(connection.total_changes)
   c = connection.cursor()
   #Chargement des tables users / accounts / operations
   users = pd.read_csv('clients.csv')
   users.to_sql('users', connection, if_exists='replace', index = True, index_label ="NumeroClient")
   accounts = pd.read_csv('comptes.csv')
   accounts.to_sql('account', connection, if_exists='replace', index = True, index_label ="NumeroCompte")
   operations = pd.read_csv('operations.csv')
   operations.to_sql('operations', connection, if_exists='replace', index = True, index_label ="NumeroOperation")
   
def start_server():
   threadsClients = []
   def instanceServeur (client, infosClient):
      adresseIP = infosClient[0]
      port = str(infosClient[1])
      print("Instance de serveur prêt pour " + adresseIP + ":" + port)
      message = ""
      while message.upper() != "FIN":
         #PIN ACTION ACCOUNT_NB
         message = client.recv(255).decode("utf-8")
         print("Message reçu du client " + adresseIP + ":" + port + " : " + message)
         client.send("Message reçu".encode("utf-8"))
      print("Connexion fermée avec " + adresseIP + ":" + port)
      client.close()
   serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   serveur.bind(('', 50000))	# Écoute sur le port 50000
   serveur.listen(5)
   while True:
      client, infosClient = serveur.accept()
      threadsClients.append(threading.Thread(None, instanceServeur, None, (client, infosClient), {}))
      threadsClients[-1].start()
   serveur.close()

menu = int(input("Entrez 1 pour Initialiser la BDD\n2 pour lancer le serveur de la banque\n"))
match menu:
   case 1:
      init_db()
   case 2:
      start_server()
   case _:
      print("Erreur : choix non reconnu")


