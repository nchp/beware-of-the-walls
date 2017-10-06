import arcade

from models import Dot, World, Block

SCREEN_WIDTH = 420
SCREEN_HEIGHT = 600

RECT_WIDTH = 70
RECT_HEIGHT = 100

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

        self.current_state = INITIAL_PAGE
        self.total_time = 0.0
        self.timer_text = None

        self.world = World(width, height)
        self.dot_sprite = ModelSprite('images/full-circle.png',model=self.world.dot)
        self.block_sprite = ModelSprite('images/block.png',model=self.world.block)

    def draw_initial_page(self):
        self.block_sprite.draw()
        self.dot_sprite.draw()

        arcade.draw_text("Click the dot to start playing.",
                        50, self.height - 50,
                         arcade.color.WHITE, 20)      

    def draw_game(self):
        self.set_mouse_visible(False)
        self.block_sprite.draw()
        self.dot_sprite.draw()   

        minutes = int(self.total_time) // 60
        seconds = int(self.total_time) % 60
        output = f"{minutes:02d}:{seconds:02d}"
        if not self.timer_text or self.timer_text.text != output:
            self.timer_text = arcade.create_text(output, arcade.color.WHITE, 20)
        arcade.render_text(self.timer_text, self.width - 80, self.height - 40)

    def draw_game_over(self):
        self.set_mouse_visible(True)
        output = "Game Over"
        arcade.draw_text(output, 240, 400, arcade.color.WHITE, 54)

        output = "Click to restart"
        arcade.draw_text(output, 310, 300, arcade.color.WHITE, 24)    

    def on_draw(self):
        arcade.start_render()

        if self.current_state == INITIAL_PAGE:
            self.draw_initial_page()

        elif self.current_state == GAME_RUNNING:
            self.draw_game()

        else:
            self.draw_game()
            self.draw_game_over()

    def update(self, delta):
        if self.current_state == GAME_RUNNING:
            self.world.update(delta)
            self.block_sprite.set_position(self.world.block.x, self.world.block.y)

            self.total_time += delta

    def on_mouse_press(self, x, y, button, modifiers):
        if self.current_state == INITIAL_PAGE:
            self.current_state = GAME_RUNNING
        elif self.current_state == GAME_OVER:
            self.current_state = GAME_RUNNING

    def on_mouse_motion(self, x, y, dx, dy):
        if self.current_state == GAME_RUNNING:
            self.world.on_mouse_motion(x, y, dx, dy)

if __name__ == '__main__':
    window = WallsWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
