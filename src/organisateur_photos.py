import utils
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organise les photos selon leurs métadonnées EXIF.")
    parser.add_argument("source", type=str, help="Chemin du dossier source contenant les photos.")
    parser.add_argument("destination", type=str, help="Chemin du dossier destination où organiser les photos.")
    
    # Rendre l'argument 'format' optionnel
    parser.add_argument("format", type=str, nargs="?", help="Format d'organisation des photos (utilisez des tokens strftime). Exemple : '%Y/%m/%d' pour année/mois/jour.")
    
    # Groupe pour l'option exclusive de tri
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("-m", "--mois", action="store_true", help="Organiser les photos par mois.")
    group.add_argument("-a", "--annee", action="store_true", help="Organiser les photos par année.")
    group.add_argument("-am", "--annee_mois", action="store_true", help="Organiser les photos par année et mois.")
    
    args = parser.parse_args()

    
    if args.format:
        format_organisation = args.format  
    elif args.mois:
        format_organisation = "%Y/%m"  
    elif args.annee:
        format_organisation = "%Y"  
    elif args.annee_mois:
        format_organisation = "%Y/%m"
   

    # Lancer l'organisation avec le format spécifié par l'utilisateur
    utils.organiser_photos(args.source, args.destination, format_organisation)
