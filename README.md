# Audio Metadata Extractor

Ce projet est un script Python permettant d'explorer des dossiers à la recherche de fichiers audio (MP3 et FLAC), d'en extraire les métadonnées (titre, artiste, album, etc.) et d'afficher la couverture (cover art) si elle est présente. C'est un outil utile pour analyser et organiser des fichiers audio, notamment dans des collections musicales ou des bibliothèques audio.

## Fonctionnalités

### 1. **Exploration d'un dossier pour détecter les fichiers audio (MP3 et FLAC)**

- **But** : Parcourir un dossier et ses sous-dossiers pour rechercher et identifier les fichiers audio au format MP3 et FLAC.
- **Validation** : Le script vérifie non seulement l'extension du fichier (.mp3 ou .flac), mais aussi son type MIME, garantissant que seuls les fichiers réellement audio sont détectés.

### 2. **Extraction et affichage des métadonnées audio**

- **But** : Extraire et afficher les informations clés d'un fichier audio :
  - Titre
  - Artiste
  - Album
  - Genre
  - Date de sortie
  - Organisation (le label ou la maison de disque)
  - Durée du fichier (en minutes et secondes)

### 3. **Affichage de la couverture (Cover Art)**

- **But** : Si une couverture (cover art) est incluse dans le fichier audio (MP3 ou FLAC), elle est extraite et affichée dans une fenêtre. La couverture peut être une image de type JPEG ou PNG intégrée dans les métadonnées du fichier.

### 4. **Création de playlists au format XSPF**

- **But** : Le script permet également de créer et de gérer des playlists au format XSPF (XML Shareable Playlist Format). Ce format est largement utilisé pour décrire des listes de lecture audio.
- **Fonctionnalités** :
  - **Création d'un fichier playlist** : Le script génère un fichier XSPF vide dans un dossier spécifié.
  - **Ajout de pistes audio** : L'utilisateur peut ajouter des fichiers audio à la playlist en fournissant le chemin du fichier et le titre de la piste. Le script crée un élément `<track>` dans le fichier XSPF pour chaque piste ajoutée.
  - **Gestion des fichiers** : Il inclut des fonctions pour supprimer un fichier XSPF si nécessaire.

### 5. **Utilisation de la fonctionnalité de playlist**

1. **Créer un fichier playlist** : La fonction `creerUnFichierxspf` crée un fichier XSPF vide dans le dossier `Python_project/Playlist`. Si le dossier n'existe pas, il est créé automatiquement.
2. **Ajouter des pistes** : L'utilisateur peut ajouter des pistes audio à la playlist en appelant la fonction `ecritureFichierxspf` et en spécifiant le chemin du fichier audio et le titre de la piste.
3. **Supprimer une playlist** : Utilisez la fonction `delete_un_fichier_xspf` pour supprimer une playlist existante en spécifiant le chemin du fichier.

## Classes du projet

### 1. **Explorer**

La classe `Explorer` est responsable de l'exploration des dossiers pour détecter les fichiers audio. Elle contient trois méthodes principales :

- **`explorer_dossier_console(self, chemin_name)`** : Parcourt un dossier et affiche les chemins des fichiers audio dans la console.
- **`explorer_dossier_interface(self, chemin) -> str`** : Explore un dossier et écrit les chemins des fichiers audio dans un fichier temporaire.
- **`explorer_dossier(self, chemin_name)`** : Retourne le chemin complet du premier fichier audio trouvé dans le dossier.

### 2. **Extraction**

La classe `Extraction` est chargée de l'extraction des métadonnées des fichiers audio. Elle contient :

- **`audio_extraire_et_afficher_tag(self, fichier)`** : Extrait les métadonnées d'un fichier audio donné et les affiche à l'utilisateur.

### 3. **Playlist**

La classe `Playlist` est responsable de la création et de la gestion des playlists. Ses méthodes comprennent :

- **`creerUnFichierxspf(self)`** : Crée un fichier XSPF vide.
- **`ecritureFichierxspf(self, dossier_music: str, out_Fichier_nom: str)`** : Écrit les informations audio dans un fichier XSPF en utilisant les chemins de fichiers d'un dossier donné.

### 4. **Console**

La classe `Console` sert d'interface utilisateur pour interagir avec le programme via la ligne de commande. Elle gère les options fournies par l'utilisateur et coordonne l'utilisation des autres classes :

- **`afficher_aide(self)`** : Affiche un message d'aide sur l'utilisation du programme.
- **`main(self)`** : Analyse les arguments de ligne de commande et appelle les méthodes appropriées des classes `Explorer`, `Extraction`, et `Playlist`.

## Importations

Le fichier `__init__.py` initialise le package `Python_project`. Il importe les classes suivantes pour un accès facile :

- **`Extraction`** : Importée depuis le module `audioTagExtraction`, elle permet d'extraire et d'afficher les métadonnées des fichiers audio.
- **`Playlist`** : Importée depuis le module `constitutionPlaylist`, elle gère la création et la modification des playlists au format XSPF.
- **`Explorer`** : Importée depuis le module `explorationDossier`, elle permet d'explorer les dossiers à la recherche de fichiers audio.

Les variables et constantes définies dans le fichier peuvent inclure la version du package, facilitant la gestion des mises à jour.

## Utilisation de la Console

Pour utiliser le script depuis la ligne de commande, assurez-vous d'abord d'être dans le dossier contenant le fichier `cli.py`. Ensuite, vous pouvez suivre les exemples ci-dessous :

- **Exécuter le script** :

    ```bash
    python3 cli.py
    ```

- **Afficher l'aide** :
  
    ```bash
    python3 cli.py -h
    ```

    ou

    ```bash
    python3 cli.py --help
    ```

- **Explorer le dossier courant** :
  
    ```bash
    python3 cli.py -d .
    ```

    ou

    ```bash
    python3 cli.py --directory .
    ```

- **Explorer un dossier spécifique** :
  
    ```bash
    python3 cli.py -d "chemin\vers\un\dossier"
    ```

    ou

    ```bash
    python3 cli.py --directory "chemin\vers\un\dossier"
    ```

- **Extraire les métadonnées d'un fichier audio dans le dossier music éxistant** :
  
    ```bash
    python3 cli.py -f music.mp3
    ```

    ou

    ```bash
    python3 cli.py --file music.mp3
    ```

- **Extraire les métadonnées d'un fichier audio en donnant un chemin spécifique** :
  
    ```bash
    python3 cli.py -f "chemin\vers\la\musique\music.mp3"
    ```

    ou

    ```bash
    python3 cli.py --file "chemin\vers\la\musique\music.mp3"
    ```

- **Générer une playlist à partir d'un dossier music éxistant et en spécifiant le nom de la playlist** :
  
    ```bash
    python3 cli.py -d ./music/ -o nom_de_votre_playlist.xspf
    ```

    ou
  
    ```bash
    python3 cli.py --directory ./music/ --output nom_de_votre_playlist.xspf
    ```

- **Générer une playlist à partir d'un dossier spécifique et en spécifiant le nom de la playlist** :
  
    ```bash
    python3 cli.py -d "chemin\vers\un\dossier" -o nom_de_votre_playlist.xspf
    ```

    ou

    ```bash
    python3 cli.py --directory "chemin\vers\un\dossier" --output nom_de_votre_playlist.xspf
    ```

- **Lancer l'interface graphique (si disponible)** :
  
    ```bash
    python3 gui.py
    ```

- **Ecouter un fichier audio donné** :
  
    ```bash
    python3 cli.py -l -f music.mp3
    ```

    ou

    ```bash
    python3 cli.py --listen --file music.mp3
    ```

- **Ecouter un fichier audio en donnant un chemin spécifique** :
  
    ```bash
    python3 cli.py -l -f "chemin\vers\la\musique\music.mp3"
    ```

    ou

    ```bash
    python3 cli.py --listen --file "chemin\vers\la\musique\music.mp3"
    ```

## Interface de Gestion des Fichiers Audio

Ce projet est une interface graphique qui permet d'explorer des fichiers audio sur votre ordinateur, d'en extraire les métadonnées, d'afficher la couverture d'album (cover art), et de créer des playlists. Il est conçu pour être simple d'utilisation grâce à des boutons et des fenêtres interactives.

### 1. Choix du dossier à explorer

- **But** : Sélectionner un dossier contenant des fichiers audio (MP3 et FLAC) sur votre ordinateur pour les analyser.
- **Fonctionnement** : Un explorateur de fichiers s'ouvre pour naviguer et choisir le dossier. Les fichiers audio trouvés sont ensuite listés dans l'interface.
- **Code associé** : La méthode `exploration_dossier()` ou `AZEexploration_dossier()` est utilisée pour parcourir le système de fichiers et charger les fichiers audio dans une Listbox.

### 2. Affichage des fichiers audio détectés

- **But** : Après avoir sélectionné un dossier, une liste de fichiers audio détectés (formats MP3 et FLAC) est affichée.
- **Fonctionnalité additionnelle** : L'utilisateur peut sélectionner un fichier audio pour afficher ses métadonnées.
- **Code associé** : La méthode `exploration_dossier()` peuple la Listbox avec les fichiers audio. La fonction `affiche_path_label()` extrait les informations du fichier sélectionné.

### 3. Extraction et affichage des métadonnées

- **But** : Afficher les métadonnées (titre, artiste, album, genre, etc.) des fichiers audio sélectionnés.
- **Fonctionnement** : Lorsqu'un fichier est cliqué dans la liste, ses métadonnées sont extraites et affichées dans l'interface.
- **Code associé** : La méthode `affiche_path_label()` appelle `extraction_et_afficher_tag()` pour extraire les métadonnées du fichier audio sélectionné.

### 4. Affichage de la couverture (Cover Art)

- **But** : Afficher l'image de couverture d'un fichier audio s'il en contient une.
- **Fonctionnement** : Si une image de couverture est détectée dans le fichier audio, elle est affichée dans une zone dédiée. Sinon, une image par défaut est utilisée.
- **Code associé** : La méthode `cover_image()` gère l'extraction et l'affichage de la couverture d'album.

### 5. Création de playlists

- **But** : Créer des playlists au format XSPF en sélectionnant plusieurs fichiers audio.
- **Fonctionnalité** : L'utilisateur peut enregistrer la playlist sous un nom spécifique ou restaurer la liste par défaut.
- **Code associé** : Les fonctions `open_new_fenetre()`, `par_defaut()`, et `specifier()` permettent la création, la spécification, et la réinitialisation des playlists. Le fichier est enregistré grâce à `gui_ecritureFichierxspf()`.

### 6. Contrôle de lecture (Play/Pause/Next/Previous)

- **But** : Contrôler la lecture des fichiers audio depuis l'interface.
- **Fonctionnalité** :
  - **Play/Pause** : Lire ou mettre en pause la chanson sélectionnée.
  - **Next/Previous** : Passer à la piste suivante ou précédente.
- **Code associé** :
  - `lire_audio()` pour la lecture.
  - `toggle_pause()` pour basculer entre pause et lecture.
  - `next_audio()` et `prev_audio()` pour changer de piste.

### 7. Navigation et interaction améliorée

- **But** : Permettre une navigation fluide entre les fichiers audio.
- **Fonctionnement** : Lorsqu'une nouvelle piste est sélectionnée, les informations affichées sont mises à jour, et les boutons "suivant" et "précédent" permettent de naviguer rapidement.
- **Code associé** : Les méthodes `next_item()` et `prev_item()` gèrent les changements de sélection dans la Listbox.

## Prérequis

Avant d'exécuter ce script, vous devez installer les bibliothèques suivantes :

- [mutagen](https://mutagen.readthedocs.io/en/latest/installation.html) : Bibliothèque utilisée pour extraire les métadonnées des fichiers MP3 et FLAC.
- [Pillow](https://python-pillow.org/) : Bibliothèque Python pour manipuler et afficher des images, utilisée ici pour afficher la couverture des fichiers audio.
- [Pygame](https://www.pygame.org/) : Bibliothèque pour créer des jeux en Python et jouer des fichiers audio.
- [Pydub](https://github.com/jiaaro/pydub) : Bibliothèque pour manipuler les fichiers audio.
- [lxml](https://lxml.de/) : Bibliothèque pour traiter les fichiers XML et HTML, souvent utilisée avec Pydub pour gérer les métadonnées.

Pour installer les dépendances, exécutez la commande suivante dans votre terminal :

```bash
pip install mutagen 
pip install Pillow 
pip install pygame
pip install pydub
pip install lxml
