import Tile

class Playground:
    def __init__(self):
        self.gridPlayer=[]
        self.gridAI=[]
        self.gridx=[]
        self.alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.grid_dimension=10
        for i in range(self.grid_dimension):
            for j in range(self.grid_dimension):
                self.gridx.append(Tile.Tile(x_coordinate=i, y_coordinate=j))
            self.gridPlayer.append(self.gridx)
        self.show_board()



    def player_attack(self, x_coordinate, y_coordinate):
        tile=self.gridPlayer[y_coordinate][x_coordinate]
        if tile.get_already_been_hit():
            hit=tile.get_ship_on_tile()

    def create_ships(self):
        cmdValid=False
        while cmdValid==False:
            cmdxA=input("Enter command for x-Axis: ")
            cmdyA=input("Enter command for y-Axis: ")

    def show_board(self):
        print("    0  1  2  3  4  5  6  7  8  9")
        for i in range(self.grid_dimension):
            outputx=f" {self.alphabet[i]} "
            for j in range(self.grid_dimension):
                if self.gridPlayer[j][i].get_ship_on_tile():
                    outputx=outputx+" # "
                else:
                    outputx=outputx+" ~ "
            print(outputx)