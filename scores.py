import json

def enregistrer_score(nom, temps, niveau, grille):
    """
    Enregistre un score dans un fichier JSON.

    Args:
    nom (str): Le nom du joueur.
    temps (float): Le temps écoulé pour gagner la partie.
    niveau (str): Le niveau de difficulté de la partie.
    grille (list): La grille de jeu utilisée pour la partie.
    """
    score = {
        "nom": nom,
        "temps": temps,
        "niveau": niveau,
        "grille": grille
    }

    try:
        with open("scores.json", "r", encoding='utf-8') as file:
            scores = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        scores = []

    scores.append(score)

    with open("scores.json", "w", encoding='utf-8') as file:
        json.dump(scores, file, indent=4)

def lire_scores():
    """
    Lit les scores enregistrés dans le fichier JSON.

    Returns:
    List: Une liste des scores enregistrés.
    """
    try:
        with open("scores.json", "r", encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []