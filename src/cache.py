import utils
import json
def charger_cache_hachages(cache_file):
    if utils.Path(cache_file).exists():
        with open(cache_file, 'r') as f:
            return json.load(f)
    return {}


def sauvegarder_cache_hachages(cache_file, cache_hachages):
    """Sauvegarde le cache des hachages dans un fichier JSON."""
    try:
        with open(cache_file, "w") as f:
            json.dump(cache_hachages, f, indent=4)
        print(f"Cache sauvegardé dans {cache_file}")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde du cache : {e}")