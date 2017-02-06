from random import randrange

import arcade as arcade
from arcade import color, draw_text, run, Window


class MyGame(Window):

    def __init__(self, width: float, height: float, title: str = 'Arcade Window', resizable: bool = False):
        super().__init__(width, height, title, resizable)
        arcade.set_background_color(color.GRAY)
        self.score = 0
        self.all_sprites_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite('character_001.png', scale=0.5)
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 500
        self.all_sprites_list.append(self.player_sprite)
        self.coin_list  = arcade.SpriteList()
        for i in range(50):
            coin = arcade.Sprite("character_115.png", 0.2)
            coin.center_x = randrange(width)
            coin.center_y = randrange(height)
            self.all_sprites_list.append(coin)
            self.coin_list.append(coin)
        self.is_stopped = True

    def animate(self, delta_time: float):
        super().animate(delta_time)
        self.all_sprites_list.update()
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        self.score += len(hit_list)
        for coin in hit_list:
            coin.kill()

    def on_draw(self):
        arcade.start_render()
        if self.is_stopped:
            score_display = "Score : %.6f" % self.score
            draw_text("Hello zażółć gęślą jaźń", 100, 100, color.BROWN, font_size=26)
            draw_text(score_display, 200, 200, color.BROWN, font_size=26)
        self.is_stopped = True
        self.all_sprites_list.draw()

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        super().on_mouse_motion(x, y, dx, dy)
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y
        self.is_stopped = False


def main():
    MyGame(800, 600, 'My game')
    run()


if __name__ == '__main__':
    main()
