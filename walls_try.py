import arcade
 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
 
class WallsGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.BLACK)

        self.dot = arcade.Sprite('images/full-circle.png')
        self.dot.set_position(100, 100)
 
    def on_draw(self):
        arcade.start_render()

        self.dot.draw()

if __name__ == '__main__':
    window = WallsGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
