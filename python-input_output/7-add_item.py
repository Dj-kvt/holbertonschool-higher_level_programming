#!/usr/bin/python3
"""Adds all arguments to a Python list and saves them to a file."""
import sys
import os

# Importation des fonctions fournies
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# 1. Charger la liste existante ou créer une nouvelle liste
if os.path.exists(filename):
    try:
        items = load_from_json_file(filename)
    except Exception:
        items = []
else:
    items = []

# 2. Ajouter les arguments de la ligne de commande (sauf le script lui-même)
items.extend(sys.argv[1:])

# 3. Sauvegarder la nouvelle liste
save_to_json_file(items, filename)
