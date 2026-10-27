import Tile
import random as rand
from typing import List, Tuple

class Playground:
    def __init__(self):
        self.grid=[]
        self.alphabet=["A","B","C","D","E","F","G","H","I","J"]
        self.ships=[("Flugzeugträger",5),("Kreuzer",4),("Zerstörer_1",3),("Zerstörer_2",3),("U-Boot",2)]
        self.hitcounter=0
        self.grid_dimension=10
        self.scoreAI=0
        self.gridAI=[]

        #Calculate number of Hits on different Ship-tiles to win
        for i in range(len(self.ships)):
            self.hitcounter=self.hitcounter+self.ships[i][1]

        #print("\nCreate AI-grid")
        for i in range(self.grid_dimension):
            gridx=[]
            for j in range(self.grid_dimension):
                gridx.append(Tile.Tile(x_coordinate=j, y_coordinate=i))
            self.grid.append(gridx)

        #Place ships on AI-grid
        self.gen_rand_ships()

        self.get_AI_grid()

    def attack_AIL(self, x, y):
        """
        Ziel: KI soll in möglichst wenig Zügen möglichst viele Treffer erlangen,
        """
        cur_tile=self.grid[x][y]
        result=cur_tile.shoot_on_tile()
        if result and not cur_tile.get_already_been_hit():
            self.scoreAI=self.scoreAI+10
            self.hitcounter=self.hitcounter-1
        self.scoreAI=self.scoreAI-1

    def check_if_win(self):
        if self.hitcounter<=0:
            return True
        else:
            return False

    def get_AI_grid(self):
        for i in range(self.grid_dimension):
            values=[]
            for j in range(self.grid_dimension):
                values.append(self.grid[j][i].get_value())
            self.gridAI.append(values)
        print(self.gridAI)
        return self.gridAI

    def get_AI_input(self):
        values=[]
        for i in range(self.grid_dimension):
            for j in range(self.grid_dimension):
                values.append(self.grid[j][i].get_value())
        return values

    def set_tile(self, x, y):
        print(f"Change Tile at {self.alphabet[x]}{y}")
        self.grid[x][y].set_ship_on_tile(True)
        self.show_board(self.grid)

    def gen_rand_ships(self):
        for i in range(len(self.ships)):
            ship_created=False
            #print(f"Build ship {self.ships[i]}")
            while not ship_created:
                x=rand.randint(0,self.grid_dimension-1)
                y=rand.randint(0,self.grid_dimension-1)
                shipdir=rand.choice(["r", "l", "o", "u"])
                shiplen=self.ships[i][1]

                if self.check_ship_out_of_bound(x, y, shipdir, shiplen):
                    if self.check_if_ship_in_way(self.grid, x, y, shipdir, shiplen):
                        self.create_ship(self.grid, x, y, shipdir, shiplen)
                        ship_created=True
                        #print(f" --> Build {self.ships[i][0]} at ({self.alphabet[x]},{y}) in Direction {shipdir} with length {shiplen}")
                        #self.show_board(self.grid)
        #print("\nFinal Result:")
        self.show_board(self.grid)

    def create_ship(self, grid, shipstartx, shipstarty, shipdir, shiplen):
        #Check if input coordinates go out of grid boundaries
        if not self.check_ship_out_of_bound(shipstartx, shipstarty, shipdir, shiplen):
            print("Eingabe out of Bound!")
            return False

        #Check if ships are intersecting
        if not self.check_if_ship_in_way(grid, shipstartx, shipstarty, shipdir, shiplen):
            print("Schiff ist schon im Weg!")
            return False

        #Only if all checks succeed -> build ship
        if shipdir=="r":
            for i in range(shiplen):
                grid[shipstartx+i][shipstarty].set_ship_on_tile(True)
        elif shipdir=="l":
            for i in range(shiplen):
                grid[shipstartx-i][shipstarty].set_ship_on_tile(True)
        elif shipdir=="u":
            for i in range(shiplen):
                grid[shipstartx][shipstarty+i].set_ship_on_tile(True)
        elif shipdir=="o":
            for i in range(shiplen):
                grid[shipstartx][shipstarty-i].set_ship_on_tile(True)
        return True

    def check_ship_out_of_bound(self, shipstartx, shipstarty, shipdir, shiplen):
        if shipdir.lower() == "r":
            if shipstartx+shiplen>=self.grid_dimension:
                return False
        elif shipdir.lower() == "l":
            if shipstartx-shiplen<0:
                return False
        elif shipdir.lower() == "u":
            if shipstarty+shiplen>=self.grid_dimension:
                return False
        elif shipdir.lower() == "o":
            if shipstartx-shiplen<0:
                return False
        return True

    def check_if_ship_in_way(self, grid, shipstartx, shipstarty, shipdir, shiplen):
        #print(f"try to build ship created at {self.alphabet[shipstartx]}{shipstarty} with dir {shipdir} of len {shiplen}")
        if shipdir.lower() == "r":
            for i in range(shiplen):
                if grid[shipstartx+i][shipstarty].get_ship_on_tile():
                    return False
        elif shipdir.lower() == "l":
            for i in range(shiplen):
                if grid[shipstartx-i][shipstarty].get_ship_on_tile():
                    return False
        elif shipdir.lower() == "u":
            for i in range(shiplen):
                if grid[shipstartx][shipstarty+i].get_ship_on_tile():
                    return False
        elif shipdir.lower() == "o":
            for i in range(shiplen):
                if grid[shipstartx][shipstarty-i].get_ship_on_tile():
                    return False
        return True

    def show_board(self, grid):
        print("    A  B  C  D  E  F  G  H  I  J")
        for i in range(self.grid_dimension):
            outputx=f" {i} "
            for j in range(self.grid_dimension):
                if grid[i][j].get_ship_on_tile():
                    outputx=outputx+" # "
                else:
                    outputx=outputx+" ~ "
            print(outputx)

""""
    def player_attack(self, x_coordinate, y_coordinate):
        tile=self.gridPlayer[y_coordinate][x_coordinate]
        if tile.get_already_been_hit():
            hit=tile.get_ship_on_tile()

    def create_ship_Player(self, shipname, shipsize):
        cmdValid=False
        print(f"Erstelle {shipname} der Länge {shipsize} Kästchen:")
        while cmdValid==False:
            #Input command
            cmd1=input("Eingabe Anfangspunkt (zB. D5): ")
            cmd2=input("Richtung Befehle:\nrechts - r\nlinks - l\noben - o\nunten - u\n\nEingabe Richtung: ").lower()[0]
            try:
                cmda=int(self.alphabet.index(cmd1[0].upper()))
                cmdx=int(cmd1[1])
            except ValueError:
                print("Bitte korrekte Formateingabe! (z.B. B3)")
                continue

            #Validate command
            if cmd2 not in ["r","l","o","u"]:
                print("Bitte einen dieser korrekten Befehle für die Richtung angeben: r, l, o, oder u")
                continue
            if cmda not in self.grid_dimension or cmdx not in self.grid_dimension:
                print("Das Spielfeld geht nur von A bis J und von 0 bis 9.")
                continue

            #create ship
            if cmd2 == "r":
                for i in range(shipsize):
                    self.gridPlayer[cmda][cmdx+i].set_ship_on_tile(True)
            elif cmd2 == "l":
                for i in range(shipsize):
                    self.gridPlayer[cmda][cmdx-i].set_ship_on_tile(True)
"""