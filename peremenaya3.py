import wrap

shirina = 400
visota = 900
y = 450
x1 = 150
x2 =350
put = x1 - 30
pol_puti = put / 2
seredidina = x1 - pol_puti
wrap.world.create_world(shirina, visota)
wrap.sprite.add('mario-items', 30, y, 'moving_platform1')
wrap.sprite.add('mario-items', x1, y, 'moving_platform1')
wrap.sprite.add('mario-items', x2, y, 'moving_platform1')
wrap.sprite.add('mario-items', shirina - 30, y, 'moving_platform1')
wrap.sprite.add('mario-1-small', 30, y - 25, 'walk1')
wrap.actions.move_to(4, seredidina, y - pol_puti - 25)
wrap.actions.move_to(4, x1, y - 25)

put = x2 - x1
pol_puti = put / 2
seredidina = x2 - pol_puti
wrap.actions.move_to(4, seredidina, y - pol_puti - 25)
wrap.actions.move_to(4, x2, y - 25)

put = shirina - 30 - x2
pol_puti = put / 2
seredidina = shirina - 30 - pol_puti
wrap.actions.move_to(4, seredidina, y - pol_puti - 25)
wrap.actions.move_to(4, shirina - 30, y - 25)

put=shirina-30-30
pol_puti=put/2
seredidina=shirina-30-pol_puti

wrap.actions.move_to(4,seredidina,y-pol_puti-25)
wrap.actions.move_to(4,30,y-25)




