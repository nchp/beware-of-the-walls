import arcade

from models import Dot, World
 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
 
class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
 
        super().__init__(*args, **kwargs)
 
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
            self.angle = self.model.angle
 
    def draw(self):
        self.sync_with_model()
        super().draw()

class WallsWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.set_mouse_visible(False)
 
        arcade.set_background_color(arcade.color.ALABAMA_CRIMSON)

        self.world = World(width, height)
        self.dot_sprite = ModelSprite('images/full-circle.png',model=self.world.dot)
        self.block_1_sprite = ModelSprite('images/block_1.png',model=self.world.block_1)
    
    def on_draw(self):
        arcade.start_render()
        self.block_1_sprite.draw()
        self.dot_sprite.draw()   

        arcade.draw_text(str(self.world.score),
                         self.width - 30, self.height - 30,
                         arcade.color.WHITE, 20)

    def update(self, delta):
        self.world.update(delta)
        self.block_1_sprite.set_position(self.world.block_1.x, self.world.block_1.y)


    def on_mouse_motion(self, x, y, dx, dy):
        self.world.on_mouse_motion(x, y, dx, dy)

if __name__ == '__main__':
    window = WallsWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
