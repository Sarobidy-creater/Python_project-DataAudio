#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Importation des modules nécessaires
from mutagen.easyid3 import EasyID3  # Pour lire et écrire les métadonnées ID3 dans les fichiers MP3.
from mutagen.mp3 import MP3  # Pour gérer les fichiers audio MP3 et accéder à leurs métadonnées.
from mutagen.id3 import ID3, APIC  # Pour manipuler les balises ID3 et gérer les images intégrées comme les couvertures d'album.
from mutagen.flac import FLAC, Picture  # Pour travailler avec les fichiers audio FLAC et gérer les images intégrées.
import mimetypes  # Pour déterminer le type MIME des fichiers en fonction de leur extension.
import os  # Importe la bibliothèque os pour interagir avec le système de fichiers


"""
    Une classe qui permet d'explorer des dossiers et de gérer les fichiers audio.
"""
class Explorer():


    """
        Fonction qui explore un dossier donné et affiche les chemins des fichiers audio (MP3, FLAC) dans la console.

        Paramètre :
        - chemin_name : str : Le chemin du dossier à explorer. Utilisez "." pour indiquer le répertoire courant.

        Retour :
        - None : Cette méthode n'a pas de retour, elle affiche les chemins dans la console.
    """
    def explorer_dossier_console(self, chemin_name):
        try:
            # Si chemin_name est ".", on prend le répertoire courant
            chemin = os.getcwd() if chemin_name == "." else os.path.abspath(chemin_name)

            # Boucle à travers les dossiers, sous-dossiers et fichiers à partir du chemin donné
            for racine, sous_dossiers, fichiers in os.walk(chemin):
                # Boucle à travers chaque fichier dans la liste des fichiers du dossier courant
                for fichier in fichiers:
                    # Construit le chemin complet du fichier
                    chemin_complet = os.path.join(racine, fichier)
                    nom = os.path.basename(chemin_complet)

                    # Vérifie si le nom du fichier se termine par '.mp3' ou '.flac'
                    if nom.endswith(".mp3") or nom.endswith(".flac"):
                        # Vérifie le type MIME du fichier
                        type_mime, _ = mimetypes.guess_type(chemin_complet)

                        # Vérifie que le type MIME est valide
                        if type_mime in ['audio/mpeg', 'audio/flac']:
                            # Écrit le chemin complet dans la console
                            print(f"{chemin_complet}\n")
        except Exception as e:
            print(f"Une erreur est survenue lors de l'exploration du dossier : {e}")


    """
        Fonction qui explore un dossier donné et enregistre les chemins des fichiers audio (MP3, FLAC) dans un fichier temporaire.

        Paramètre :
        - chemin : str : Le chemin du dossier à explorer.

        Retour :
        - str : Le chemin du fichier temporaire contenant les chemins des fichiers audio, ou None en cas d'erreur.
    """
    def explorer_dossier_interface(self, chemin) -> str:
        fichier_sortie = os.path.abspath(r'python_project\FichierTemp\TempFile.txt')  
            
        out_dir = fichier_sortie.replace("\\", "/") 
        try:
            # Ouvre le fichier de sortie en mode écriture
            with open(out_dir, 'w', encoding='utf-8') as f:
                # Boucle à travers les dossiers, sous-dossiers et fichiers à partir du chemin donné
                for racine, sous_dossiers, fichiers in os.walk(chemin):
                    # Boucle à travers chaque fichier dans la liste des fichiers du dossier courant
                    for fichier in fichiers:
                        # Construit le chemin complet du fichier
                        chemin_complet = os.path.join(racine, fichier)

                        audio = None  # Initialise une variable audio à None.

                        # Vérifie l'extension du fichier
                        if chemin_complet.endswith('.mp3'):
                            try:
                                audio = MP3(chemin_complet, ID3=EasyID3)  # Crée un objet MP3.
                            except Exception as e:
                                print(f"Erreur lors de la lecture du fichier MP3 {chemin_complet}: {e}")

                        elif chemin_complet.endswith('.flac'):
                            try:
                                audio = FLAC(chemin_complet)  # Crée un objet FLAC.
                            except Exception as e:
                                print(f"Erreur lors de la lecture du fichier FLAC {chemin_complet}: {e}")

                        # Vérifie que l'audio a été chargé correctement
                        if audio:
                            # Vérifie le type MIME du fichier
                            type_mime, _ = mimetypes.guess_type(chemin_complet)

                            # Vérifie que le type MIME est valide
                            if type_mime in ['audio/mpeg', 'audio/x-flac']:
                                # Écrit le chemin complet dans le fichier
                                f.write(f"{chemin_complet}\n")
             
            return fichier_sortie
        except Exception as e:
            print(f"Une erreur est survenue lors de l'écriture dans le fichier : {e}")
            return None


    """
        Fonction qui explore un dossier donné et retourne le chemin du premier fichier audio (MP3, FLAC) trouvé.

        Paramètre :
        - chemin_name : str : Le chemin du dossier à explorer. Utilisez "." pour indiquer le répertoire courant.

        Retour :
        - str : Le chemin complet du premier fichier audio trouvé, ou None en cas d'erreur.
    """
    def explorer_dossier(self, chemin_name):
        try:
            # Si chemin_name est ".", on prend le répertoire courant
            chemin = os.getcwd() if chemin_name == "." else os.path.abspath(chemin_name)

            # Boucle à travers les dossiers, sous-dossiers et fichiers à partir du chemin donné
            for racine, sous_dossiers, fichiers in os.walk(chemin):
                # Boucle à travers chaque fichier dans la liste des fichiers du dossier courant
                for fichier in fichiers:
                    # Construit le chemin complet du fichier
                    chemin_complet = os.path.join(racine, fichier)
                    nom = os.path.basename(chemin_complet)

                    # Vérifie si le nom du fichier se termine par '.mp3' ou '.flac'
                    if nom.endswith(".mp3") or nom.endswith(".flac"):
                        # Vérifie le type MIME du fichier
                        type_mime, _ = mimetypes.guess_type(chemin_complet)

                        # Vérifie que le type MIME est valide
                        if type_mime in ['audio/mpeg', 'audio/flac']:
                            # Écrit le chemin complet dans la console
                            return chemin_complet
        except Exception as e:
            print(f"Une erreur est survenue lors de l'exploration du dossier : {e}")
            return None
        

    def explorer_dossier_gui(self, chemin) -> str:
        fichier_sortie = os.path.abspath(r'Python_project\FichierTemp\TempFile.txt')  
            
        out_dir = fichier_sortie.replace("\\", "/")  
        try:
            # Ouvre le fichier de sortie en mode écriture
            with open(out_dir, 'w', encoding='utf-8') as f:
                # Boucle à travers les dossiers, sous-dossiers et fichiers à partir du chemin donné
                for racine, sous_dossiers, fichiers in os.walk(chemin):
                    # Boucle à travers chaque fichier dans la liste des fichiers du dossier courant
                    for fichier in fichiers:
                        # Construit le chemin complet du fichier
                        chemin_complet = os.path.join(racine, fichier)

                        audio = None  # Initialise une variable audio à None.

                        # Vérifie l'extension du fichier
                        if chemin_complet.endswith('.mp3'):
                            try:
                                audio = MP3(chemin_complet, ID3=EasyID3)  # Crée un objet MP3.
                            except Exception as e:
                                print(f"Erreur lors de la lecture du fichier MP3 {chemin_complet}: {e}")

                        elif chemin_complet.endswith('.flac'):
                            try:
                                audio = FLAC(chemin_complet)  # Crée un objet FLAC.
                            except Exception as e:
                                print(f"Erreur lors de la lecture du fichier FLAC {chemin_complet}: {e}")

                        # Vérifie que l'audio a été chargé correctement
                        if audio:
                            # Vérifie le type MIME du fichier
                            type_mime, _ = mimetypes.guess_type(chemin_complet)

                            # Vérifie que le type MIME est valide
                            if type_mime in ['audio/mpeg', 'audio/x-flac']:
                                # Écrit le chemin complet dans le fichier
                                f.write(f"{chemin_complet}\n")
             
            return fichier_sortie
        except Exception as e:
            print(f"Une erreur est survenue lors de l'écriture dans le fichier : {e}")
            return None
        
