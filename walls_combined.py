import arcade
import random

SCREEN_WIDTH = 420
SCREEN_HEIGHT = 700

INITIAL_PAGE = 0
GAME_RUNNING = 1
GAME_OVER = 2

WALLS_X_POSITION = (30,90,150,210,270,330,390)
"""
class Walls:
    def __init__(self, x, y, image, speed):
        self.wall_list = arcade.SpriteList()
        self.image = image
        self.speed = 2
        self.center_x = x
        self.center_y = y
    
    def update(self):
        self.center_y -= 2
"""
        
class WallsWindow(arcade.Window):
    """
    Main application class.
    """
    def make_wall(self, x, y, wall_list):
        self.walls = arcade.Sprite("images/walls.png")
        self.walls.center_x = x
        self.walls.center_y = y
        wall_list.append(self.walls)

    def gen_walls(self, wall_list):
        for i in range(7):
            for j in range(7):
                if j == 3:
                    continue
                self.make_wall(WALLS_X_POSITION[j], SCREEN_HEIGHT+50+(100*i), wall_list)

    def __init__(self, screen_width, screen_height):
        """ Constructor """
        # Call the parent constructor. Required and must be the first line.
        super().__init__(screen_width, screen_height)
        arcade.set_background_color(arcade.color.ALABAMA_CRIMSON)
        self.current_state = INITIAL_PAGE

        self.timer_text = None
        self.init_wall_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.total_time = 0.0

        # Set up the player
        self.dot_sprite = arcade.Sprite("images/full-circle.png")
        self.dot_sprite.center_x = 210
        self.dot_sprite.center_y = 150

        for i in range(3):
            for j in range(3):
                for k in range(i+1):
                    self.make_wall(WALLS_X_POSITION[k], ((i+j+3)*100)-50, self.init_wall_list)
                for l in range(i+1):
                    self.make_wall(WALLS_X_POSITION[6-l], ((i+j+3)*100)-50, self.init_wall_list)

        self.gen_walls(self.wall_list)              

        self.set_mouse_visible(True)

    def draw_initial_page(self):
        self.dot_sprite.draw()
        self.init_wall_list.draw()
        arcade.draw_text("Click the dot to start playing.",
                        50, self.height - 50,
                        arcade.color.WHITE, 20)      

    def draw_game(self):
        self.set_mouse_visible(False)
        self.init_wall_list.draw()
        self.wall_list.draw()
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
        arcade.draw_text(output, 150, 400, arcade.color.WHITE, 24)

        output = "Click to restart"
        arcade.draw_text(output, 110, 300, arcade.color.WHITE, 24)    

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        if self.current_state == INITIAL_PAGE:
            self.draw_initial_page()

        elif self.current_state == GAME_RUNNING:
            self.draw_game()
        
        elif self.current_state == GAME_OVER:
            self.draw_game_over()

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        # Change states as needed.
        if self.current_state == INITIAL_PAGE:
            self.current_state = GAME_RUNNING
        elif self.current_state == GAME_OVER:
            self.current_state = GAME_RUNNING

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        # Only move the user if the game is running.
        if self.current_state == GAME_RUNNING:
            self.dot_sprite.center_x = x
            self.dot_sprite.center_y = 150

    def update(self, delta):
        """ Movement and game logic """

        # Only move and do things if the game is running.
        if self.current_state == GAME_RUNNING:
            # Call update on all sprites (The sprites don't do much in this
            # example though.)
#            self.all_sprites_list.update()

            for self.walls in self.init_wall_list:
                self.walls.center_y -= 2
                if self.walls.top < 0:
                    self.walls.kill()
                
                if arcade.check_for_collision_with_list(self.dot_sprite,self.init_wall_list):
                    self.current_state = GAME_OVER

            for self.walls in self.wall_list:
                self.walls.center_y -= 2
                if self.walls.top < 0:
                    self.walls.kill()
                    self.gen_walls(self.wall_list)
                
                if arcade.check_for_collision_with_list(self.dot_sprite,self.wall_list):
                    self.current_state = GAME_OVER

        self.total_time += delta

if __name__ == '__main__':
    window = WallsWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
