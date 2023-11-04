import wrap
import random
width=1200
height=600
x1=700
y1=150
x2=500
y2=100
x3=600
y3=300
a=random.randint(1,1200)
b=random.randint(1,600)
v=random.randint(1,1200)
n=random.randint(1,600)
f=random.randint(1,1200)
y=random.randint(1,600)
wrap.world.create_world(width,height)
wrap.sprite.add('pacman',20,25,'enemy_red_left1')
wrap.sprite.add('pacman', width-30,height-30,'enemy_red_left1')
wrap.sprite.add('pacman',width-30,30,'enemy_red_left1')
wrap.sprite.add('pacman', 30,height-30, 'enemy_red_left1')
wrap.sprite.add('pacman',width/2,height/2,'player2')
wrap.sprite.add('pacman',a,b)
wrap.sprite.add('pacman',v,n)
wrap.sprite.add('pacman',f,y)
wrap.sprite.add_text('точка1',a,b-15,text_color=[255,255,255])
wrap.sprite.add_text('точка2',v,n-15,text_color=[255,255,255])
wrap.sprite.add_text('точка3',f,y-15,text_color=[255,255,255])
wrap.sprite.add('mario-enemies', width/2,height-30,'duck_blue_go')
wrap.sprite.add('mario-enemies', width/2,height-570,'turtle_blue_throwing2')
wrap.sprite.add('mario-enemies',width-30,height/2,'crab')

wrap.actions.move_to(4,a,b)
wrap.actions.move_to(4,v,n)
wrap.actions.move_to(4,f,y)
#wrap.actions.move_to(4,x2,y2)
#wrap.actions.move_to(4,x2,y3)
#wrap.actions.move_to(4,x3,y3)
# wrap.actions.move_to(14,x3,y3)
# wrap.actions.move_to(13,width-30,y2)
# wrap.actions.move_to(13,x2,y2)
# wrap.actions.move_to(11,x1,height-30)
# wrap.actions.move_to(11,x1,y1)