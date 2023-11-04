import time

import wrap

from wrap import sprite

wrap.world.set_back_color(41, 15, 179)
wrap.world.create_world(1500, 900)
wrap.sprite.add('mario-enemies', 750, 450, 'crab')
wrap.actions.move_to(0, 600, 400)
wrap.sprite.add('mario-enemies', 800, -50, 'dragon_throw1')
wrap.actions.move_to(1, 800, 450, 2000)
wrap.sprite.add('mario-enemies', 1550, 450, 'fish_red')
wrap.sprite.add_text('ты откуда взялся?', 600, 350)
time.sleep(2)
wrap.sprite.add_text('я свалился с луны!', 800, 350)
wrap.actions.move_to(2, 1000, 450, 3000)
wrap.sprite.set_reverse_x(1, True)
wrap.actions.set_size(2,200,200)
wrap.sprite.remove(4)
wrap.sprite.remove(3)
wrap.sprite.add_text('АААААА',800,300,font_size=50,text_color=[255,0,0])
wrap.actions.move_to(2,800,450)
wrap.sprite.remove(5)
wrap.sprite.set_reverse_y(1,True)
wrap.actions.move_to(1,800,1000)
