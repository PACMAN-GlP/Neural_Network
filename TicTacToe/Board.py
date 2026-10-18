import Tile

class Board:
    def __init__(self):
        self.boardSize=3
        self.board=[]

        for y in range(self.boardSize):
            self.row=[]
            for x in range(self.boardSize):
                self.row.append(Tile.Tile())
            self.board.append(self.row)

        self.show_board()

    def show_board(self):
        print("-"*(self.boardSize*2+1))
        for y in range(self.boardSize):
            output=""
            for x in range(self.boardSize):
                output=f"{output}|{self.board[x][y].tileStatus}"
            print(""+output+"|")
        print("-"*(self.boardSize*2+1))

    def is_it_a_win(self):
        #Test vertical:
        for x in range(self.boardSize):
            if self.board[x][0]==self.board[x][1] and self.board[x][0]==self.board[x][2]:
                return True

        #Test horizontal:
        for y in range(self.boardSize):
            if self.board[0][y]==self.board[1][y] and self.board[0][y]==self.board[2][y]:
                return True

        #Test diagonal:
        for i in range(self.boardSize):
            if self.board[i][i] == self.board[i+1][i+1] and self.board[i][i] == self.board[i+2][i+2]:
                return True
            if self.board[i][self.boardSize-i]==self.board[i+1][self.boardSize-i+1] and self.board[i][self.boardSize-i]==self.board[i+2][self.boardSize-i+2]:
                return True

        return False