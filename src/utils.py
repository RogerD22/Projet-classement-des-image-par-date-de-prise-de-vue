from exif import Image as ExifImage
from pathlib import Path
from datetime import datetime
import shutil

def deplacer_photos_par_date():
    repertoire_source = Path("photos")
    repertoire_destination = Path("photos_organisees")

    if not repertoire_source.is_dir():
        print(f"Le répertoire source {repertoire_source} n'existe pas.")
        return None
    elif not any(repertoire_source.iterdir()):
        print(f"Le répertoire source {repertoire_source} est vide.")
        return None

    for image_path in repertoire_source.glob("*.jpeg"):
        try:
            with open(image_path, "rb") as image_file:
                image = ExifImage(image_file)
                if image.has_exif and hasattr(image, "datetime_original"):
                    date_prise_vue = datetime.strptime(image.datetime_original, "%Y:%m:%d %H:%M:%S")
                    year = date_prise_vue.year
                    month = f"{date_prise_vue.month:02}"  

                    dossier_destination = repertoire_destination / str(year) / month
                    dossier_destination.mkdir(parents=True, exist_ok=True)  

                    chemin_destination = dossier_destination / image_path.name
                    shutil.move(str(image_path), chemin_destination)
                    print(f"Date de prise de vue : {date_prise_vue}")
                    print(f"Image déplacée : {image_path} -> {chemin_destination}")
                else:
                    print(f"Aucune date de prise de vue trouvée dans {image_path}. Image non déplacée.")
        except Exception :
            print(f"Erreur lors de la lecture des métadonnées EXIF pour {image_path}")
deplacer_photos_par_date()
