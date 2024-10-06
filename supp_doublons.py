# Ouvrir et lire le fichier
with open("Links5.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Supprimer les doublons en utilisant un set
unique_lines = list(set(lines))

# Optionnel : trier les lignes (pour les organiser de manière ordonnée)
unique_lines.sort()

# Écrire les lignes uniques dans un nouveau fichier ou écraser l'ancien
with open("fichier_sans_doublons.txt", "w", encoding="utf-8") as file:
    file.writelines(unique_lines)

print("Les doublons ont été supprimés et les lignes uniques ont été sauvegardées.")
