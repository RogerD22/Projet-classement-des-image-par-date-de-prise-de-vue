from exif import Image as ExifImage
from pathlib import Path
from datetime import datetime
import shutil

repertoire_source = Path("photos")
repertoire_destination = Path("photos_organisees")


def extraire_date_prise_vue(image_path):
    if not repertoire_source.is_dir():
        print(f"Le répertoire source {repertoire_source} n'existe pas.")
        return None
    elif not any(repertoire_source.iterdir()):
        print(f"Le répertoire source {repertoire_source} est vide.")
        return None
    
    try:
        with open(image_path, "rb") as image_file:
            image = ExifImage(image_file)
            if image.has_exif and hasattr(image, "datetime_original"):
                date_prise_vue = datetime.strptime(image.datetime_original, "%Y:%m:%d %H:%M:%S")
                return date_prise_vue
            else:
                print(f"Aucune date de prise de vue trouvée dans {image_path}.")
                return None
    except Exception as e:
        print(f"Erreur lors de la lecture des métadonnées EXIF pour {image_path} : {e}")
        return None

def creer_dossier_destination(repertoire_destination, date_prise_vue):
    year = date_prise_vue.year
    month = f"{date_prise_vue.month:02}"
    dossier_destination = repertoire_destination / str(year) / month
    dossier_destination.mkdir(parents=True, exist_ok=True)
    return dossier_destination

def deplacer_image(image_path, dossier_destination):
    chemin_destination = dossier_destination / image_path.name
    shutil.move(str(image_path), chemin_destination)
    print(f"Image déplacée : {image_path} -> {chemin_destination}")

def organiser_photos_par_date():


    for image_path in repertoire_source.glob("*.jpeg"):
        date_prise_vue = extraire_date_prise_vue(image_path)
        
        if date_prise_vue:
            dossier_destination = creer_dossier_destination(repertoire_destination, date_prise_vue)
            deplacer_image(image_path, dossier_destination)
        else:
            print(f"Image non déplacée : {image_path}")

organiser_photos_par_date()
