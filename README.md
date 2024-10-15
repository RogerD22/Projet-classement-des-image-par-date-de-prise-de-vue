# Projet : Classification d'Images par Date de Prise de Vue


## Les GOATs 🐐 sont composés de :

- Mohamed-Ousalem YAHIAOUI [RogerD22](https://github.com/RogerD22)
- Youssef BEN TANFOUS [YoussefBT0](https://github.com/YoussefBT0)


### Fonctionnalités du projet

#### Noyau minimal (Indispensables) :
1. **Lecture des métadonnées EXIF** :
   - Extraction de la date de prise de vue des images JPEG pour les classer correctement.

2. **Création d'une structure de répertoires basée sur des paramètres** :
   - Génération d’une arborescence de répertoires en fonction de la date de prise de vue, incluant l’année, le mois, le jour, l’heure, les minutes et les secondes (ex : `Photos/{year}/{month}/{day}/{hour}_{minute}_{second}/{basename}`).
   - *Dépend de 1.*

3. **Déplacement des fichiers vers les répertoires appropriés** :
   - Déplacement des fichiers JPEG vers les répertoires correspondants tout en conservant leur nom de base.
   - *Dépend de 2.*

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


