# Credits to whoever wrote this first
# Globals for the bearings
# Change the values as you see fit
EAST = (1, 0)
NORTH = (0, 1)
WEST = (-1, 0)
SOUTH = (0, -1)
WORLD = [NORTH, EAST, SOUTH, WEST]

class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.coordinates = x, y

    def turn_right(self):
        self.bearing = WORLD[WORLD.index(self.bearing) - 3]

    def turn_left(self):
        self.bearing = WORLD[WORLD.index(self.bearing) - 1]

    def advance(self):
        self.coordinates = self.coordinates[0] + self.bearing[0], self.coordinates[1] + self.bearing[1]

    def simulate(self, sequence):
        for i in sequence:
            if i == 'R':
                self.turn_right()
            elif i == 'L':
                self.turn_left()
            else:
                self.advance()
