import wrap
width=1000
height=900
seredina=width/2
seredina2=height/2
radom=seredina+100
radom2=seredina-100
radom3=seredina2-100
wrap.world.create_world(width,height)
wrap.sprite.add('mario-items',seredina,seredina2,'star')
wrap.sprite.add('pacman',20,25,'player2')
wrap.sprite.add('mario-enemies',30,height-30,'fish_red')
wrap.sprite.add('mario-enemies',seredina-185,seredina2+135,'duck_blue_go')
wrap.sprite.add('mario-enemies',width-30,height-30,'turtle_blue_throwing2')
wrap.sprite.add('mario-enemies',seredina-185,seredina2-135,'crab')
wrap.sprite.add('mario-enemies',width-30,30,'dragon_throw1')
wrap.sprite.add('pacman',radom2,radom3+170,'enemy_pink_left2')
wrap.sprite.add('pacman',radom,radom3+170,'enemy_yellow_left2')
wrap.sprite.add('mario-enemies',radom,radom3+30,'fish_red')
wrap.sprite.add('pacman',radom2,radom3+30,'player2')
wrap.sprite.add('pacman',width-100,height-70,'enemy_yellow_left2')
wrap.sprite.add('pacman',width-100,70,'enemy_pink_left2')





