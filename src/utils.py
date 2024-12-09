import cache
import hashlib
from exif import Image as ExifImage
from pathlib import Path
from datetime import datetime
import shutil

CACHE_FILE = "cache_hachages.json"

"""Charger le cache au début"""
cache_hachages = cache.charger_cache_hachages(CACHE_FILE)

def extraire_date_prise_vue(image_path):
    """Extrait la date de prise de vue à partir des métadonnées EXIF."""
    try:
        with open(image_path, "rb") as image_file:
            image = ExifImage(image_file)
            if image.has_exif and hasattr(image, "datetime_original"):
                return datetime.strptime(image.datetime_original, "%Y:%m:%d %H:%M:%S")
    except Exception as e:
        print(f"Erreur lors de la lecture des métadonnées EXIF pour {image_path} : {e}")
    return None


def creer_dossier_destination(format_organisation, repertoire_destination, date_prise_vue):
    """Crée un dossier basé sur le format d'organisation spécifié par l'utilisateur."""
    format_organisation_str = date_prise_vue.strftime(format_organisation)
    dossier_destination = repertoire_destination / format_organisation_str
    dossier_destination.mkdir(parents=True, exist_ok=True)
    return dossier_destination

def gerer_conflits_noms(chemin_destination):
    """Gère les conflits de noms en ajoutant un suffixe numérique si nécessaire."""
    base_name = chemin_destination.stem  
    extension = chemin_destination.suffix  
    parent_folder = chemin_destination.parent  
    compteur = 1
    while chemin_destination.exists():
        nouveau_nom = f"{base_name}_{compteur}{extension}"  
        chemin_destination = parent_folder / nouveau_nom
        compteur += 1
    return chemin_destination


def calculer_hash_fichier(image_path):
    """Calcule le hash MD5 d'un fichier."""
    # Vérifiez si le hash est déjà dans le cache
    if str(image_path) in cache_hachages:
        return cache_hachages[str(image_path)]

    hash_md5 = hashlib.md5()
    try:
        with open(image_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        # Ajouter le hash au cache
        hash_value = hash_md5.hexdigest()
        cache_hachages[str(image_path)] = hash_value
        cache.sauvegarder_cache_hachages(CACHE_FILE, cache_hachages)  
        return hash_value
    except Exception as e:
        print(f"Erreur lors du calcul du hash pour {image_path} : {e}")
        return None

def fichier_est_dupliqué(image_path, dossier_destination):
    """Vérifie si un fichier identique existe déjà dans le dossier de destination."""
    image_hash = calculer_hash_fichier(image_path)
    if image_hash is None:
        return False

    for fichier in dossier_destination.iterdir():
        if fichier.is_file() and calculer_hash_fichier(fichier) == image_hash:
            print(f"Doublon trouvé : {image_path} est identique à {fichier}")
            return True
    return False


def deplacer_image(image_path, dossier_destination):
    """Déplace une image vers le dossier de destination après avoir géré les conflits de noms et vérifié les doublons."""
    chemin_destination = dossier_destination / image_path.name

    """Vérifier si un fichier identique existe déjà"""
    if fichier_est_dupliqué(image_path, dossier_destination):
        print(f"Fichier en double détecté : {image_path} est déjà présent dans {dossier_destination}. Ignoré.")
        return

    """Gérer les conflits de noms"""
    chemin_destination = gerer_conflits_noms(chemin_destination)

    try:
        shutil.move(str(image_path), chemin_destination)
        print(f"Image déplacée : {image_path} -> {chemin_destination}")
    except Exception as e:
        print(f"Erreur lors du déplacement de {image_path} : {e}")

def organiser_photos(format_organisation, repertoire_source, repertoire_destination):
    """Organise les photos en sous-dossiers basés sur le format d'organisation choisi par l'utilisateur."""
    repertoire_source = Path(repertoire_source)
    repertoire_destination = Path(repertoire_destination)

    if not repertoire_source.is_dir():
        print(f"Le répertoire source {repertoire_source} n'existe pas.")
        return
    if not any(repertoire_source.iterdir()):
        print(f"Le répertoire source {repertoire_source} est vide.")
        return
    if not repertoire_destination.exists():
        print(f"Le répertoire destination {repertoire_destination} n'existe pas. Création du répertoire...")
        repertoire_destination.mkdir(parents=True, exist_ok=True)

    for image_path in repertoire_source.glob("*"):
        if image_path.suffix.lower() in {".jpg", ".jpeg"}:
            print(f"Fichier trouvé ! : {image_path}")
            date_prise_vue = extraire_date_prise_vue(image_path)
            if date_prise_vue:
                dossier_destination = creer_dossier_destination(format_organisation, repertoire_destination, date_prise_vue )
                deplacer_image(image_path, dossier_destination)
            else:
                print(f"Aucune date EXIF trouvée pour {image_path}. Fichier ignoré.")
                
"""Sauvegarder le cache à la fin"""
cache.sauvegarder_cache_hachages(CACHE_FILE, cache_hachages)
