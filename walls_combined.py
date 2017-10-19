import arcade
import random
import sys

SCREEN_WIDTH = 420
SCREEN_HEIGHT = 700

INITIAL_PAGE = 0
GAME_RUNNING = 1
GAME_OVER = 2

X_POSITION = (30,90,150,210,270,330,390)

class Walls(arcade.Sprite):
    def __init__(self, images, x, y):
        super().__init__(images)
        self.center_x = x
        self.center_y = y
        self.speed = 3

    def update(self):
        self.center_y -= self.speed
        if self.top < 0:
            self.kill()

class WallsWindow(arcade.Window):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)
        arcade.set_background_color(arcade.color.BITTERSWEET_SHIMMER)
        #arcade.set_background_color([random.randrange(255),random.randrange(255),random.randrange(255)])
        self.current_state = INITIAL_PAGE

        self.timer_text = None
        self.total_time = 0.0
        self.score = 0.0

        self.dot_sprite = arcade.Sprite("images/full-circle.png")
        self.dot_sprite.center_x = 210
        self.dot_sprite.center_y = 180

        self.init_wall_list = arcade.SpriteList()
        for i in range(3):
            for j in range(3):
                for k in range(i+1):
                    self.wall = Walls('images/walls.png', X_POSITION[k], ((i+j+3)*100)-50)
                    self.init_wall_list.append(self.wall)
                for l in range(i+1):
                    self.wall = Walls('images/walls.png', X_POSITION[6-l], ((i+j+3)*100)-50)
                    self.init_wall_list.append(self.wall)

        self.wall_row = arcade.SpriteList()
        self.beg_road = 3
        self.last_road = random.randrange(1,5)
        for i in range(7):
            if i == self.beg_road:
                continue
            self.wall = Walls('images/walls.png', X_POSITION[i], SCREEN_HEIGHT+50)
            self.wall_row.append(self.wall)
        for i in range(7):
            if (i>=self.beg_road and i<=self.last_road) or (i>=self.last_road and i<=self.beg_road):
                continue
            self.wall = Walls('images/walls.png', X_POSITION[i], SCREEN_HEIGHT+150)
            self.wall_row.append(self.wall)
        for i in range(7):
            if i == self.last_road:
                continue
            self.wall = Walls('images/walls.png', X_POSITION[i], SCREEN_HEIGHT+250)
            self.wall_row.append(self.wall)

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
        self.wall_row.draw()
        self.dot_sprite.draw()
        """
        minutes = int(self.total_time) // 60
        seconds = int(self.total_time) % 60
        output_t = f"{minutes:02d}:{seconds:02d}"
        if not self.timer_text or self.timer_text.text != output_t:
            self.timer_text = arcade.create_text(output_t, arcade.color.WHITE, 20)
        arcade.render_text(self.timer_text, self.width - 80, self.height - 40)
        """
        output = "{}".format(int(self.score))
        arcade.draw_text(output, self.width - 40, self.height - 40, arcade.color.WHITE, 20)

    def draw_game_over(self):
        self.set_mouse_visible(True)
        output = "GAME OVER."
        arcade.draw_text(output, 130, 400, arcade.color.WHITE, 24)
        """
        output = "Click to restart"
        arcade.draw_text(output, 110, 300, arcade.color.WHITE, 24)    
        """

    def on_draw(self):
        arcade.start_render()

        if self.current_state == INITIAL_PAGE:
            self.draw_initial_page()

        elif self.current_state == GAME_RUNNING:
            self.draw_game()
        
        elif self.current_state == GAME_OVER:
            self.draw_game_over()

    def on_mouse_press(self, x, y, button, modifiers):
        if self.current_state == INITIAL_PAGE:
            self.current_state = GAME_RUNNING
        elif self.current_state == GAME_OVER:
            self.current_state = GAME_RUNNING

    def on_mouse_motion(self, x, y, dx, dy):
        if self.current_state == GAME_RUNNING:
            self.dot_sprite.center_x = x
            self.dot_sprite.center_y = 180

    def update(self, delta):
        if self.current_state == GAME_RUNNING:
            self.init_wall_list.update()
            self.wall_row.update()
            if self.wall.center_y <= 652:
                self.beg_road = self.last_road
                self.last_road = random.randrange(1,5)
                for i in range(7):
                    if (i>=self.beg_road and i<=self.last_road) or (i>=self.last_road and i<=self.beg_road):
                        continue
                    self.wall = Walls('images/walls.png', X_POSITION[i], SCREEN_HEIGHT+50)
                    self.wall_row.append(self.wall)
                for i in range(7):
                    if i == self.last_road:
                        continue
                    self.wall = Walls('images/walls.png', X_POSITION[i], SCREEN_HEIGHT+150)
                    self.wall_row.append(self.wall)
            
            if len(self.init_wall_list) > 0:
                if arcade.check_for_collision_with_list(self.dot_sprite,self.init_wall_list):
                    self.current_state = GAME_OVER

            if arcade.check_for_collision_with_list(self.dot_sprite,self.wall_row):
                self.current_state = GAME_OVER
                
            self.total_time += delta
            self.score += 0.1

if __name__ == '__main__':
    window = WallsWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
