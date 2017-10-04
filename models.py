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

        self.score = 0

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.dot.x = x
        self.dot.y = 200
 
    def update(self, delta):
        self.dot.update(delta)
 
class Dot(Model):
 
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)
  
    def update(self, delta):
        self.wait_time += delta
 
        if self.wait_time < Dot.MOVE_WAIT:
            return

        if self.x > self.world.width:
            self.x = 0
        if self.x < 0:
            self.x = self.world.width
        if self.y > self.world.height:
            self.y = 0
        if self.y < 0:
            self.y = self.world.height

        self.x += DIR_OFFSET[self.direction][0]
        self.y += DIR_OFFSET[self.direction][1]
 
        self.wait_time = 0