from random import randint


class Maze:
    def __init__(self, file_name, items):
        self.data = self.load_maze(file_name)
        self.create_items(items)

    def find_tile(self, tile):
        for i in range(len(self.data)):     
            for j in range(len(self.data[i])): 
                if self.data[i][j] == tile:
                    return [i,j]
        return None

    def get_char (self, i, j):
        return self.data[i][j]
    
    def set_char( self, i, j, char):
        self.data[i][j] = char
    

    def load_maze (self,file_name):
        data = []
        with open(file_name) as f:
            #f est une liste de lignes -> boucle pour rajouter les lignes 1 par 1, sans le "\n", dans la liste labyrinthe
            for line in f:
                line = line.replace('\n','')
                # labyrinthe = liste de liste
                data.append(list(line))
        return data

    def create_items (self, items):
        for item in items:
            pos = self.get_random_empty_tile()
            self.data[pos[0]][pos[1]] = item
    
    # donner une position aléatoire aux items, que si la place est vide
    def get_random_empty_tile(self):
        while True:
            row = randint(0, len(self.data)-1)
            col = randint(0, len(self.data)-1)
            tile = self.data[row][col]
            if tile == " ":
                return [row, col]
    
    def draw_maze(self):
        for row_data in self.data:
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

class McGyver:
    def __init__(self):
        self.is_out = False

    def move(self, maze, items):
        direction = input("(Droite = D, Gauche = G, Haut = H, Bas = B, Quitter = Q) Votre choix?: ").upper()
        modifs = (0,0)
        if direction == "D":
            #verifier la nouvelle position_M avec la fonction verif_position et avancer que si la nvle case est vide
            modifs = (0, 1)
        elif direction == "G":
            modifs = (0, -1)
        elif direction == "H":
            modifs = (-1, 0)
        elif direction == "B":
            modifs = (1, 0)
        elif direction == "Q":
            print("Vous avez choisi de quitter... à bientôt!")
            self.is_out = True

        self.update_position(maze, modifs, items)

    def update_position(self, maze, modifs, items):
    # position de départ + modifs demandées, dans la limite du labyrinthe.
        pos = maze.find_tile("M")
        lin = pos[0] + modifs[0]
        lin = min(lin,14)
        col = pos[1] + modifs[1]
        col = min(col, 14)
        # si nvle posiiton = item: remplacer par vide dans la liste items.
        if maze.get_char(lin, col) in items:
            maze.set_char(lin,col, " ")
        # si nvle position = G: check victoire
        if maze.get_char(lin, col) == "G":
            self.check_victory(maze, items)
            # return True à la place de none: condition arrêt du jeu dans fonction main
            self.is_out = True
        # si nvle position = vide, remplacer nvle position par M, et ancienne par vide.
        if maze.get_char(lin, col) == " ":
            maze.set_char(pos[0], pos[1], " ")
            maze.set_char(lin,col,"M")

    def check_victory(self, maze, items):
    # definir victoire ou défaite à la fin de la boucle for, pas à chaque item: victory = flag variable 
        victory = True
        # dans la liste items:
        for it in items:
            # s'il y a encore un item de la liste dans le labyrinthe (= si fonction find_tile trouve un item, is not None): victory = false.
            if maze.find_tile(it):
                victory = False
                break
        if not victory:
            print("You're dead!")
        else:
            print("You win!")

    











def main():
    file_name = "d:/Alix/FormationAlix/formationDAPython/Projet03/lab_mcgyver.txt"
    items = ("A","T","E")
    maze = Maze(file_name, items)
    mg = McGyver()

    while mg.is_out == False:
        maze.draw_maze()
        mg.move(maze, items)


if __name__ == "__main__":
    main()