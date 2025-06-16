import requests
import csv
"""Désole pour mes commzntaires en français."""


def fetch_and_print_posts():
    """Récupère les posts et les affiche."""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()  # conversion en liste de dictionnaires
        for post in posts:
            print()
            print(post["title"])
            print(post["body"])
    else:
        print("Erreur lors de la récupération des posts.")


def fetch_and_save_posts():
    """Récupère les posts et les sauvegarde dans un fichier CSV."""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        posts = response.json()

        # On crée une liste contenant uniquement les champs demandés
        data = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]

        # On écrit les posts dans un fichier CSV
        with open('posts.csv', 'w', newline='') as file:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for post in posts:
                writer.writerow(post)
    else:
        print("Erreur lors de la récupération des posts.")
