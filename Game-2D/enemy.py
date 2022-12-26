from models import Graphic, levels


class Enemy(Graphic):
    def __init__(self, SPEED, TYPE, HP, DAMAGE, **kwargs):
        super().__init__(**kwargs)
        self.SPEED = SPEED
        self.TYPE = TYPE
        self.HP = HP
        self.DAMAGE = DAMAGE
        self.enemy_counter = 0

    def enemy_move(self):
        if self.enemy_counter <= 10:
            self.rect.x -= self.SPEED
            self.enemy_counter += 1
        if self.enemy_counter <= 20 and self.enemy_counter > 10:
            self.rect.x += self.SPEED
            self.enemy_counter += 1
        if self.enemy_counter >= 21:
            self.enemy_counter = 0    
                






enemy_settings = Enemy(SPEED = 5, TYPE = "swordsman", HP = 50, DAMAGE = 10, x = 450, y = 30, width = 70, height = 70, img_path = 'images/enemy_image.png' )
