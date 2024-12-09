import utils
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Organise les photos selon leurs métadonnées EXIF, permettant de les trier dans des dossiers basés sur la date de prise de vue. "
                    "Vous pouvez choisir d'organiser les photos par année, mois, ou année et mois. "
                    "Pour plus d'informations sur les tokens `strftime`, veuillez consulter la documentation officielle : https://docs.python.org/3/library/datetime.html")

    
    parser.add_argument("source", type=str, help="Chemin du dossier source contenant les photos à organiser.")

    parser.add_argument("destination", type=str, help="Chemin du dossier destination où organiser les photos.")
    
    parser.add_argument("format", type=str, nargs="?", help="Format d'organisation des photos (utilisez des tokens strftime). Exemple : '%%Y/%%m/%%d' pour année/mois/jour. "
             "Si non spécifié, vous pouvez choisir entre l'option mois, année ou année/mois. "
             "Pour plus d'informations sur les tokens strftime, consultez la documentation officielle : https://docs.python.org/3/library/datetime.html")
    
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("-m", "--mois", action="store_true", help="Organiser les photos par mois, avec le format '%%B'.")
    group.add_argument("-a", "--annee", action="store_true", help="Organiser les photos par année, avec le format '%%Y'.")
    group.add_argument("-am", "--annee_mois", action="store_true", help="Organiser les photos par année et mois, avec le format '%%Y/%%B'.")
    
    
    args = parser.parse_args()

    if args.format:
        format_organisation = args.format  
    elif args.mois:
        format_organisation = "%B"  
    elif args.annee:
        format_organisation = "%Y"  
    elif args.annee_mois:
        format_organisation = "%Y/%B"
    else:
        format_organisation = "%Y/%B"

    utils.organiser_photos(args.source, args.destination, format_organisation)
