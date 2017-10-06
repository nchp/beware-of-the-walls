import arcade

from models import Dot, World
 
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

INITIAL_PAGE = 0
GAME_RUNNING = 1
GAME_OVER = 2
 
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
        arcade.set_background_color(arcade.color.ALABAMA_CRIMSON)
        self.set_mouse_visible(False)

        self.total_time = 0.0
        self.timer_text = None

        self.world = World(width, height)
        self.dot_sprite = ModelSprite('images/full-circle.png',model=self.world.dot)
        self.block_1_sprite = ModelSprite('images/block.png',model=self.world.block_1)

    def on_draw(self):
        arcade.start_render()
        self.block_1_sprite.draw()
        self.dot_sprite.draw()   

        minutes = int(self.total_time) // 60
        seconds = int(self.total_time) % 60
        output = f"{minutes:02d}:{seconds:02d}"
        if not self.timer_text or self.timer_text.text != output:
            self.timer_text = arcade.create_text(output, arcade.color.WHITE, 20)
        arcade.render_text(self.timer_text, self.width - 80, self.height - 40)

    def update(self, delta):
        self.world.update(delta)
        self.block_1_sprite.set_position(self.world.block_1.x, self.world.block_1.y)

        self.total_time += delta

    def on_mouse_motion(self, x, y, dx, dy):
        self.world.on_mouse_motion(x, y, dx, dy)

if __name__ == '__main__':
    window = WallsWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
