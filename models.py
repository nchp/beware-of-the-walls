import arcade.key
from random import randint

class Model:
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0

    def hit(self, other, hit_size):
        return (abs(self.x - other.x) <= hit_size) and (abs(self.y - other.y) <= hit_size)

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.dot = Dot(self, 100, 100)
#        self.gold = Gold(self, 400, 400)

        self.score = 0
 
    def update(self, delta):
        self.dot.update(delta)
 
"""        if self.dot.hit(self.gold, 10):
            self.gold.random_location()
            self.score += 1

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.dot.switch_direction()
"""

class Dot(Model):
    DIR_HORIZONTAL = 0
    DIR_VERTICAL = 1
 
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)
        self.direction = Dot.DIR_VERTICAL
 
    def switch_direction(self):
        if self.direction == Dot.DIR_HORIZONTAL:
            self.direction = Dot.DIR_VERTICAL
            self.angle = 0
        else:
            self.direction = Dot.DIR_HORIZONTAL
            self.angle = -90
 
    def update(self, delta):
        if self.direction == Dot.DIR_VERTICAL:
            if self.y > self.world.height:
                self.y = 0
            self.y += 5
        else:
            if self.x > self.world.width:
                self.x = 0
            self.x += 5

"""class Gold(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)

    def random_location(self):
        self.x = randint(0, self.world.width - 1)
        self.y = randint(0, self.world.height - 1)
"""
