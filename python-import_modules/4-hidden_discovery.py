#!/usr/bin/python3
import importlib.util

if __name__ == "__main__":
    # Chemin vers le module compilé hidden_4.pyc présent dans /tmp
    pyc_path = "/tmp/hidden_4.pyc"

    # Charger le module depuis le fichier .pyc
    spec = importlib.util.spec_from_file_location("hidden_4", pyc_path)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # Récupérer toutes les clés (noms) dans le dictionnaire du module
    names = hidden_4.__dict__.keys()

    # Filtrer les noms pour ne garder que ceux qui ne commencent pas par "__"
    for name in sorted(n for n in names if not n.startswith("__")):
        print(name)
