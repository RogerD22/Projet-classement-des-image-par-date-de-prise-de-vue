from exif import Image as ExifImage
from pathlib import Path
from datetime import datetime
import shutil


repertoire_source = Path("photos")
repertoire_destination = Path("photos_organisees")


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


def creer_dossier_destination(repertoire_destination, date_prise_vue):
    """Crée un dossier basé sur l'année et le mois de la date."""
    year = date_prise_vue.year
    month = f"{date_prise_vue.month:02}"
    dossier_destination = repertoire_destination / str(year) / month
    dossier_destination.mkdir(parents=True, exist_ok=True)
    print(f"Dossier créé ou déjà existant : {dossier_destination}")
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

    print(f"Nom final après gestion des conflits : {chemin_destination}")
    return chemin_destination


def deplacer_image(image_path, dossier_destination):
    """Déplace une image vers le dossier de destination après avoir géré les conflits de noms."""
    print(f"Déplacement du fichier : {image_path}")
    chemin_destination = dossier_destination / image_path.name
    chemin_destination = gerer_conflits_noms(chemin_destination)
    
    try:
        shutil.move(str(image_path), chemin_destination)
        print(f"Image déplacée : {image_path} -> {chemin_destination}")
    except Exception as e:
        print(f"Erreur lors du déplacement de {image_path} : {e}")
        
        
def organiser_photos_par_date():
    """Organise les photos en sous-dossiers par année et mois."""
    if not repertoire_source.is_dir():
        print(f"Le répertoire source {repertoire_source} n'existe pas.")
        return
    elif not any(repertoire_source.iterdir()):
        print(f"Le répertoire source {repertoire_source} est vide.")
        return

    print(f"Traitement des fichiers dans {repertoire_source}...")

    for image_path in repertoire_source.glob("*.jpeg"):
        print(f"Fichier trouvé : {image_path}")
        date_prise_vue = extraire_date_prise_vue(image_path)
        if date_prise_vue:
            print(f"Date de prise de vue : {date_prise_vue}")
            dossier_destination = creer_dossier_destination(repertoire_destination, date_prise_vue)
            deplacer_image(image_path, dossier_destination)
        else:
            print(f"Aucune date EXIF pour {image_path}. Image ignorée.")
            
            
organiser_photos_par_date()
