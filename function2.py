import wrap
import random
wrap.world.create_world(1000,900)
a=random.randint(1,1000)
d=random.randint(1,900)
x=random.randint(30,120)
f=wrap.sprite.add('pacman',500,650,'player2')
wrap.sprite.add('pacman',a,d)
wrap.actions.set_angle_to_point(f,a,d)
#wrap.actions.move_to(f,a,d,)
wrap.sprite.add('pacman',a,d-30,'enemy_blue_left1')
wrap.sprite.set_size(f,x,x)
wrap.sprite.get_y()
