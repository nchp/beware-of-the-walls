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
 
        self.dot = Dot(self, 200, 150)
        self.block_1 = Block_1(self, 200, 150)

        self.score = 0

    def on_mouse_motion(self, x, y, dx, dy):
        self.dot.x = x
        self.dot.y = 150
 
    def update(self, delta):
        self.block_1.update(delta)
 
class Dot(Model):
 
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)

class Block_1(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)

    def update(self, delta):
        self.y -= 2