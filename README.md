# Projet : Classification d'Images par Date de Prise de Vue


## Les GOATs 🐐 sont composés de :

- Mohamed-Ousalem YAHIAOUI [RogerD22](https://github.com/RogerD22)
- Youssef BEN TANFOUS [YoussefBT0](https://github.com/YoussefBT0)


## Bibliothèques Utilisées

- `hashlib`
- `exif`
- `pathlib`
- `datetime`
- `shutil`
- `json`
- `argparse`

## Présentation de la Structure du Code
- **`src/utils.py`**: Contient les fonctions principales pour extraire les métadonnées EXIF, calculer les hashes des fichiers, vérifier les doublons, gérer les conflits de noms et déplacer les images.
- **`src/cache.py`**: Gère le chargement et la sauvegarde du cache des hashes des fichiers.
- **`src/organisateur_photos.py`**: Point d'entrée du programme avec une interface utilisateur en ligne de commande utilisant `argparse`.

## Répartition du Travail

### Travail de BEN TANFOUS Youssef
- **Fonction `creer_dossier_destination`**: Permet de créer les dossiers de destination selon le format d'organisation choisi (par année, mois, etc.).
- **Fonction `gerer_conflits_noms`**: Gère les conflits de noms en ajoutant un suffixe unique pour éviter les écrasements de fichiers.
- **Fonction `deplacer_image`**: Déplace les images dans les dossiers de destination après avoir vérifié les doublons et résolu les conflits de noms.
- **Mise en place de l'interface utilisateur avec `argparse`**: Implémente les options de ligne de commande permettant de spécifier le dossier source, le dossier de destination, et le format d'organisation.

### Travail de YAHIAOUI Mohamed-Ousalem
- **Fonction `extraire_date_prise_vue`**: Extrait la date de prise de vue des métadonnées EXIF des fichiers image.
- **Fonction `calculer_hash_fichier`**: Calcule le hash MD5 des fichiers pour identifier les doublons.
- **Fonction `fichier_est_dupliqué`**: Vérifie si un fichier identique existe déjà dans le dossier de destination en comparant les hashes.
- **Intégration dans `organiser_photos`**: Combine les différentes fonctions pour extraire les métadonnées, vérifier les doublons, et organiser les fichiers.
- **Création du cache**: Mise en place du système de cache pour éviter la réanalyse des photos déjà traitées.

## Premier rendu :

### Fonctionnalités du projet

#### Noyau minimal (Indispensables) :
1. **Lecture des métadonnées EXIF** :
   - Extraction de la date de prise de vue des images JPEG pour les classer correctement.

2. **Création d'une structure de répertoires basée sur des paramètres** :
   - Génération d’une arborescence de répertoires en fonction de la date de prise de vue, incluant l’année, le mois, le jour, l’heure, les minutes et les secondes (ex : `Photos/{year}/{month}/{basename}`).
   - *Dépend de 1.*

3. **Déplacement des fichiers vers les répertoires appropriés** :
   - Déplacement des fichiers JPEG vers les répertoires correspondants tout en conservant leur nom de base.
   - *Dépend de 4.*

4. **Gestion des conflits de noms** :
   - En cas de fichier portant le même nom dans le répertoire cible, un numéro incrémental est ajouté au fichier pour éviter l'écrasement (ex : `photo_01.jpg`, `photo_02.jpg`).
   - *Dépend de 3.*

5. **Détection et suppression des doublons exacts** :
   - Comparaison des fichiers source et cible pour vérifier s'ils sont identiques (via un hash ou une comparaison byte à byte ou pixel par pixel mais qui demande beaucoup plus de temps de traitement) et suppression du fichier source si identique.
   - Modifier #3 pour ajouter une vérification des doublons avant le déplacement des fichiers.

6. **Interface utilisateur (CLI ou GUI)** :
   - Ajout de paramètres configurables via une interface en ligne de commande (par exemple : chemin d'entrée, modèle de répertoire, etc.).
   - Modifier #2 pour permettre la configuration via une interface utilisateur.
   - *Dépend de #6 (support des formats)*

#### Fonctionnalités optionnelles (Compléments) :


7. **Support d'autres formats d'images** :
   - Support possible pour d'autres formats d'image (comme PNG, TIFF), si compatibles avec EXIF.
   - Modifier #1 pour lire les métadonnées EXIF d'autres formats d'images.
   - *Dépend de #5 (lecture des métadonnées)*


8. **Développement d’un cache pour éviter la réanalyse des photos déjà traitées** :
   - Mise en place d’un système de cache pour mémoriser les fichiers déjà analysés, en fonction de leur chemin et métadonnées.
   Ce cache permet d’améliorer les performances en ignorant les fichiers inchangés lors des exécutions suivantes.
   Modifier #3 pour intégrer un système de cache vérifiant les fichiers déjà traités.
   - Modifier #1 pour gérer les erreurs lors de la lecture des métadonnées et du déplacement des fichiers.
   - *Dépend de #5 et #7*


9. **Gestion des erreurs** :
   - Prise en charge des erreurs liées aux métadonnées manquantes, aux fichiers corrompus, etc.
   - Modifier #1 pour inclure une gestion des exceptions lors de la lecture des métadonnées et du déplacement des fichiers, afin de traiter les erreurs de manière appropriée.  
   - *Dépend de #5 et #6*

   
### Priorités et Dépendances

- **Priorité haute** : 
  - Lecture des métadonnées EXIF
  - Création des répertoires en fonction des dates
  - Déplacement des fichiers dans les répertoires appropriés
- **Priorité moyenne** : 
  - Gestion des conflits de noms
  - Gestion des erreurs (fichiers corrompus, métadonnées manquantes)
- **Priorité basse** : 
  - Détection et gestion des doublons
  - Support pour d'autres formats d'images


## Deuxieme rendu : Bibliothèques à garder pour le projet

### 1. **Pillow**
- **Service rendu** :  
    Permet d’accéder aux métadonnées EXIF d'images (JPEG notamment) et de manipuler des fichiers image.
- **Limites** :  
    - Ne couvre que les images compatibles avec EXIF (pas de PNG).  
    - Ne gère pas les conflits de noms ni le déplacement des fichiers.
- **Facilité d’installation** :  
    Installation simple via `pip install pillow`.
- **Facilité d’utilisation** :  
    API intuitive : `Image.open()._getexif()`.
- **Compatibilité** :  
    Bien intégré, sans problème majeur connu.
- **Communauté & documentation** :  
    Documentation complète et bien structurée disponible [ici](https://pillow.readthedocs.io/).



### 2. **os** (standard Python)
- **Service rendu** :  
    Gestion de fichiers et répertoires : création, suppression, détection de conflits de noms.
- **Limites** :  
    Nécessite `shutil` pour des opérations plus complexes.
- **Facilité d’installation** :  
    Inclus dans Python par défaut.
- **Facilité d’utilisation** :  
    Utilisation simple avec `os.path`, `os.listdir()`, `os.rename()`.
- **Compatibilité** :  
    Bien intégré, sans problème majeur connu.
- **Communauté & documentation** :
    Documentation complète et bien structurée disponible [ici](https://docs.python.org/3/library/os.html).




### 3. **hashlib** (standard Python)
- **Service rendu** :  
    Génération de hash pour détecter des doublons (SHA512).
- **Limites** :  
    Ne gère pas directement les conflits de noms.
- **Facilité d’installation** :  
    Inclus directement dans Python.

- **Facilité d’utilisation** :  
    Exemple d’utilisation :  
    ```python
    hashlib.SHA512(open(file, 'rb').read()).hexdigest()
    ```
    
- **Compatibilité** :  
    Bien intégré, sans problème majeur connu.
- **Communauté & documentation** :
    Documentation complète et bien structurée disponible [ici](https://docs.python.org/3/library/hashlib.html).



### 4. **argparse** (standard Python)
- **Service rendu** :  
    Fournit une interface en ligne de commande pour passer des arguments et options à l’exécution (ex. chemin source).
- **Limites** :  
    Interface limitée à l'utilisation en terminal, elle ne propose pas de gestion graphique.
- **Facilité d’installation** :  
    Installation simple via `pip install argparse`

- **Facilité d’utilisation** :  
    API simple et intuitive : 
    ```python
    import argparse
    parser = argparse.ArgumentParser(description='Description du script.')
    parser.add_argument('chemin', type=str, help='Chemin du répertoire source')
    args = parser.parse_args()
    ```

- **Compatibilité** :
    Bien intégré, sans problème majeur connu.
- **Communauté & documentation** :
    Documentation complète et bien structurée disponible [ici](https://docs.python.org/3/library/argparse.html).



### 5. **shutil** (standard Python)
- **Service rendu** :  
    Offre des fonctions de manipulation avancée de fichiers et répertoires, comme le déplacement, la copie et la suppression.
- **Limites** :  
    - Ne gère pas directement les conflits de noms (nécessite un traitement manuel avec `os`).  
    - Certaines opérations peuvent échouer si les permissions sont insuffisantes.
- **Facilité d’installation** :  
    Inclus par défaut avec Python, aucune installation supplémentaire nécessaire.
  
- **Facilité d’utilisation** :  
    Simple à utiliser :
    ```python
    import shutil

    # Déplacer un fichier
    shutil.move('source.jpg', 'destination/')

    # Copier un fichier
    shutil.copy('source.jpg', 'destination/')
    ```

- **Compatibilité** :
    Bien intégré, sans problème majeur connu.
- **Communauté & documentation** :
    Documentation complète et bien structurée disponible [ici](https://docs.python.org/3/library/shutil.html).


### 6. **logging** (standard Python)  
- **Service rendu** :  
    Fournit un système de gestion de journaux (logs) pour suivre l’exécution du programme et détecter les erreurs ou avertissements.
- **Limites** :  
    - L’analyse des journaux est manuelle (pas d’analyse automatisée).  
    - Ne permet pas nativement la rotation de fichiers volumineux (nécessite `RotatingFileHandler` pour cela).
- **Facilité d’installation** :  
    Inclus par défaut dans Python, aucune installation supplémentaire nécessaire.
- **Facilité d’utilisation** :  
    Facile à configurer et personnaliser
- **Compatibilité** :
    Bien intégré, sans problème majeur connu.
- **Communauté & documentation** :
    Documentation complète et bien structurée disponible [ici](https://docs.python.org/3/library/logging.html).

### Optionnelles :
   - pytest (pour tester le projet)
   - Tkinter (si on veut ajouter une interface graphique simple)
   - PyQt ou Kivy (pour une interface graphique plus avancée)


### Notes du prof :

    - A la place de pillow essayer : bibliotheque hachoir / exifread
    - pathlib a la place de os
    - pyside pour l'interface graphique
    - pour gere le cache utiliser DBM ou sqlit
    - Tkinter à oublier car pas fou
