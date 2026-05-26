from typing import List

grille : List[list] = [
[0,0,1,0,0],
[1,0,1,0,2],
[0,0,0,0,1],
[0,1,1,0,0],
[0,0,0,0,0] 
]

def ia_recherche(grille: List[list], l: int, c: int):
    # 1) Vérifier les limites
    if l < 0 or l >= len(grille) or c < 0 or c >= len(grille[0]):
        return False
    # 2) Mur ou déjà visité → stop
    if grille[l][c] in (1, 3):
        return False
    # 3) Objectif trouvé
    if grille[l][c] == 2:
        print("Objectif trouvé en :", l, c)
        return True
    
    # 4) Marquer comme visité
    grille[l][c] = 3

    # 5) Explorer récursivement les 4 directions
    return (
    ia_recherche(grille, l+1, c) or
    ia_recherche(grille, l-1, c) or
    ia_recherche(grille, l, c+1) or
    ia_recherche(grille, l, c-1)
    )

# ia_recherche(grille, 4, 4)

# -------------------------------------------------
# --- Mise en application -------------------------
# -------------------------------------------------
"""
Implémentez une IA récursive qui cherche un trésor dans une carte 2D. Bonus : afficher la carte à
chaque étape pour voir l’exploration.
"""

carte : List[list] = [
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0] 
]

def afficher_carte():
    print(*carte, sep="\n")
    print("---")

nbTour : int = 0

def chercher_tresor(tresor_pos: tuple, pos: tuple) -> bool:
    global nbTour
    x: int = int(pos[0])
    y: int = int(pos[1])
    nbTour += 1

    # Check si il ne sort pas de la carte
    if x < 0 or x >= len(carte[0]) or y < 0 or y >= len(carte):
        return False

    # Déja visité
    if carte[y][x] == 3:
        return False

    # Trésor trouvé
    if (x, y) == tresor_pos:
        carte[y][x] = 2
        afficher_carte()
        print(f'Ahoy, tu as atteint le tresor situé en (x={x}, y={y}) en {nbTour} tour(s) !')
        return True

    # afficher comme visité
    carte[y][x] = 3
    afficher_carte()

    # explore recursivement les 4 pos
    return (
        chercher_tresor(tresor_pos, (x + 1, y)) or
        chercher_tresor(tresor_pos, (x - 1, y)) or
        chercher_tresor(tresor_pos, (x, y + 1)) or
        chercher_tresor(tresor_pos, (x, y - 1))
    )

init_pos: tuple = (0, 0)
tresor_pos: tuple = (2, 2)

chercher_tresor(tresor_pos, init_pos)