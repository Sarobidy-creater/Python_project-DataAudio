#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from lxml import etree
import os
import datetime
from explorationDossier import Explorer

class Playlist():

    """
        Crée un fichier XSPF vide dans le dossier spécifié.

        Paramètre :
        - Aucun

        Retour :
        - Le chemin du fichier XSPF créé.
    """
    def creerUnFichierxspf(self):  
        dossier = 'Python_project\\Playlist'
        # Vérifier si le dossier existe, sinon le créer
        if not os.path.exists(dossier):
            os.makedirs(dossier)

        # Création du fichier et écriture
        nom = os.path.join(dossier, 'fichierPlaylist.xspf')  # Spécifier le chemin complet
        fichier = open(nom, 'w')  # Ouverture du fichier en écriture

        # Écriture de plusieurs lignes dans le fichier
        fichier.write("<?xml version='1.0' encoding='UTF-8'?>\n""<playlist version=\"1\" xmlns=\"http://xspf.org/ns/0/\"></playlist>\n")

        fichier.close()  # Fermeture du fichier après écriture

        varfic = nom.replace("\\", "/")
        return varfic
    
    
    """
        Crée un fichier XSPF vide dans le dossier spécifié.

        Paramètre :
        - Aucun

        Retour :
        - Le chemin du fichier XSPF créé.
    """
    def creation_Specifique_Fichierxspf(self, chemin: str):  
        dossier = chemin
        # Vérifier si le dossier existe, sinon le créer
        if not os.path.exists(dossier):
            os.makedirs(dossier)

        # Création du fichier et écriture
        nom = os.path.join(dossier, 'fichierPlaylist.xspf')  # Spécifier le chemin complet
        fichier = open(nom, 'w')  # Ouverture du fichier en écriture

        # Écriture de plusieurs lignes dans le fichier
        fichier.write("<?xml version='1.0' encoding='UTF-8'?>\n""<playlist version=\"1\" xmlns=\"http://xspf.org/ns/0/\"></playlist>\n")

        fichier.close()  # Fermeture du fichier après écriture

        varfic = nom.replace("\\", "/")
        return varfic


    """
        Supprime le fichier XSPF spécifié.

        Paramètre :
        - chemin : Le chemin du fichier XSPF à supprimer.

        Retour :
        - Aucun
    """
    def deleteUnFichierxspf(self,chemin: str): 
        try:
            os.remove(chemin)
            print(f"Le fichier '{chemin}' a été supprimé avec succès.")
        except FileNotFoundError:
            print(f"Erreur : Le fichier '{chemin}' n'a pas été trouvé.")
        except Exception as e:
            print(f"Une erreur est survenue : {e}")


    """
        Écrit une nouvelle piste dans le fichier XSPF existant.

        Paramètres :
        - cheminFichier : Le chemin du fichier XSPF à modifier.
        - cheminAudio : Le chemin du fichier audio à ajouter à la playlist.
        - titrePlay : Le titre de la chanson à ajouter.

        Retour :
        - Aucun
    """
    def ecritureFichierxspf(self,out_cheminFichier: str,in_cheminFichier: str):

        if out_cheminFichier == None: 
            chemin_file = self.creerUnFichierxspf()
        else:
            chemin_file = self.creation_Specifique_Fichierxspf(out_cheminFichier) 
            
        """
        Parse le fichier .xspf existant
        """
        # Charge et analyse le fichier XML à partir du chemin donné
        tree = etree.parse(chemin_file) 
        # Récupère l'élément racine du document XML (la balise <playlist>) 
        root = tree.getroot() 

        # Crée un élément <title> pour indiquer le titre de la chanson
        date = etree.Element("date") 
        # Définit le titre de la chanson 
        date.text = datetime.datetime.today().strftime('%d-%m-%y %H:%M:%S')  
        # Ajoute l'élément <title> comme enfant de <track>
        root.append(date) 


        # Crée un élément <title> pour indiquer le titre de la chanson
        # title = etree.Element("title") 
        # Définit le titre de la chanson 
        # title.text = titrePlay  
        # Ajoute l'élément <title> comme enfant de <track>
        # root.append(title) 

        """
        Crée de nouveaux éléments (par exemple, une liste de pistes avec une seule piste)
        """
        # Crée un nouvel élément <trackList> qui contiendra les pistes
        tracklist = etree.Element("trackList") 

        # Chemin du fichier 
        fichier_lire_chemin = Explorer.explorer_dossier_interface(in_cheminFichier)

        with open(fichier_lire_chemin, 'r', encoding='utf-8') as f:
            for ligne in f:
                cheminAudio = ligne.strip()
                # Crée un nouvel élément <track> pour une piste spécifique 
                track = etree.Element("track")  

                """
                Définit les détails de la piste
                """
                # Crée un élément <location> pour spécifier l'emplacement du fichier audio
                location = etree.Element("location")  
                # Remplace les antislashs par des barres obliques pour le chemin audio
                cheminVar = cheminAudio.replace("\\", "/")
                # Définit l'URL ou le chemin du fichier audio pour cette piste
                location.text = f"file:///{cheminVar}" 
                    # Ajoute l'élément <location> comme enfant de <track>
                track.append(location)  
                # Ajoute l'élément <title> comme enfant de <track>
                #track.append(title)  
                # Ajoute l'élément <track> à l'élément <trackList>
                tracklist.append(track)   
 

        """
        Ajoute la liste de pistes à la racine du document XML
        """
        # Ajoute l'élément <trackList> à l'élément racine <playlist>
        root.append(tracklist)  

        """
        Écrit le fichier XML mis à jour
        """
        # Ouvre le fichier en mode binaire (écriture)
        with open(chemin_file, 'wb') as f:  
            # Écrit le contenu XML dans le fichier avec un formatage lisible, la déclaration XML et un encodage UTF-8
            f.write(etree.tostring(tree, pretty_print=True, xml_declaration=True, encoding='UTF-8'))











"""
Exemple d'utilisation
"""

# Crée d'abord le fichier XSPF vide
# chemin_fichier = r"C:\Users\nelly\Desktop\projet python\Python_project\FichierTemp"

 

# Ajoute du contenu au fichier XSPF
# Appelle la fonction pour ajouter une piste à la playlist
# Playlist().ecritureFichierxspf(chemin_fichier)  
# C:\Users\nelly\Desktop\projet python\Python_project\09 - RER D.mp3