class Tile:
    def __init__(self, x_coordinate, y_coordinate):
        self.ship_on_tile=False
        self.already_hit=False
        self.x_coordinate=x_coordinate
        self.y_coordinate=y_coordinate
        self.value=0.5

    def get_already_been_hit(self):
        return self.already_hit

    def get_value(self):
        return self.value

    def shoot_on_tile(self):
        self.already_hit=True
        if self.ship_on_tile:
            self.value=1
            return True
        else:
            self.value=0
            return False

    def get_ship_on_tile(self):
        return self.ship_on_tile

    def set_ship_on_tile(self, ship_on_tile=bool):
        self.ship_on_tile=ship_on_tile