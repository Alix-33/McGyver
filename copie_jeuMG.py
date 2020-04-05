from random import randint

def ouvrir_dos(fichier):    
    maze = []
    with open(fichier) as f:
        #f est une liste de lignes -> boucle pour rajouter les lignes 1 par 1, sans le "\n", dans la liste labyrinthe
        for line in f:
            line = line.replace('\n','')
            # labyrinthe = liste de liste
            maze.append(list(line))
    return maze

# trouver les coordonnées d'une tuile dans le labyrinthe
def find_tile(tile, maze):
    for i in range(len(maze)):     
        for j in range(len(maze[i])): 
            if maze[i][j] == tile:
                return [i,j]
    return None

# mettre à jour la position après réponse joueur:
def update_position(maze, modifs, items):
    # position de départ + modifs demandées, dans la limite du labyrinthe.
    pos = find_tile("M", maze)
    lin = pos[0] + modifs[0]
    lin = min(lin,14)
    col = pos[1] + modifs[1]
    col = min(col, 14)
    # si nvle posiiton = item: remplacer par vide dans la liste items.
    if maze[lin][col] in items:
        maze[lin][col] = " "
    # si nvle position = G: check victoire
    if maze[lin][col] == "G":
        check_victory(maze, items)
        # return True à la place de none: condition arrêt du jeu dans fonction main
        return True
    # si nvle position = vide, remplacer nvle position par M, et ancienne par vide.
    if maze[lin][col] == " ":
        maze[pos[0]][pos[1]] = " "
        maze[lin][col] = "M"

def check_victory(maze, items):
    # definir victoire ou défaite à la fin de la boucle for, pas à chaque item: victory = flag variable 
    victory = True
    # dans la liste items:
    for it in items:
        # s'il y a encore un item de la liste dans le labyrinthe (= si fonction find_tile trouve un item, is not None): victory = false.
        if not find_tile(it, maze):
            victory = False
            break
    if not victory:
        print("You're dead!")
    else:
        print("You win!")


# donner une position aléatoire aux items, que si la place est vide
def get_random_empty_tile(maze):
    while True:
        row = randint(0, len(maze)-1)
        col = randint(0, len(maze)-1)
        tile = maze[row][col]
        if tile == " ":
            return [row, col]

# dessiner le labyrinthe, avec A, T et E à la place des positions aléatoires, Macgyver au départ et gardien à l'arrivée.
def draw_maze(maze):
    for row_data in maze:
        for tile in row_data:
            if tile == "G":
                print(" ⟁", end = "")
            elif tile == "M":
                print("⚪", end = "")
            elif tile == "#":
                print("⬜", end = "")
            elif tile == " ":
                print("⬛", end = "")
            else:
                # mettre l'item aléatoire défini dans get_random_empty_tile.
                print(f" {tile}", end = "")
        print()
    print()


def main():

    maze = ouvrir_dos("d:/Alix/FormationAlix/formationDAPython/Projet03/lab_mcgyver.txt")
    items = ("A","T","E")

    for item in items:
        pos = get_random_empty_tile(maze)
        maze[pos[0]][pos[1]] = item

    while True:

        draw_maze(maze)
        joueur = input("(Droite = D, Gauche = G, Haut = H, Bas = B, Quitter = Q) Votre choix?: ").upper()
        
        if joueur == "D":
            #verifier la nouvelle position_M avec la fonction verif_position et avancer que si la nvle case est vide
            modifs = (0, 1)
        elif joueur == "G":
            modifs = (0, -1)
        elif joueur == "H":
            modifs = (-1, 0)
        elif joueur == "B":
            modifs = (1, 0)
        elif joueur == "Q":
            print("Vous avez choisi de quitter... à bientôt!")
            break

        if update_position(maze, modifs, items):
            break



if __name__ == "__main__":
    main()