import Tile

class Playground:
    def __init__(self):
        self.gridPlayer=[]
        self.gridAI=[]
        self.gridx=[]
        self.alphabet=["A","B","C","D","E","F","G","H","I","J"]
        self.ships=[("Flugzeugträger",5),("Kreuzer",4),("Zerstörer_1",3),("Zerstörer_2",3),("U-Boot",2)]
        self.grid_dimension=10
        for i in range(self.grid_dimension):
            for j in range(self.grid_dimension):
                self.gridx.append(Tile.Tile(x_coordinate=i, y_coordinate=j))
            self.gridPlayer.append(self.gridx)
        self.show_board()
        for i in range(len(self.ships)):
            self.create_ship_Player(*self.ships[i])
            self.show_board()

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

    def show_board(self):
        print("    A  B  C  D  E  F  G  H  I  J")
        for i in range(self.grid_dimension):
            outputx=f" {i} "
            for j in range(self.grid_dimension):
                if self.gridPlayer[i][j].get_ship_on_tile():
                    outputx=outputx+" # "
                else:
                    outputx=outputx+" ~ "
            print(outputx)