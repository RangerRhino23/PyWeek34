from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()

Sky(texture='assets/sky.png')


def update():
    pass

def input(key):
    if key == 'q':
        quit()
    if key == 'g':
        print(player.position)

#Player
player = FirstPersonController(speed=20, y=3, position=Vec3(90, -3.5, -90))

#Ground
ground = Entity(model='cube', scale=(200,1,200), y=-4, texture='assets/ground.png', collider='box')

def build_base():
    #wall = Entity(model='cube', scale=(5,5,1), position=(10,-1,10), texture='assets/wall.png', collider='box')
    starter_wall1 = Entity(model='cube', scale=(20,5,1), position=(90,-1,-100), texture='assets/wall.png', collider='box')
    starter_wall2 = Entity(model='cube', scale=(1,5,20), position=(100,-1,-90), texture='assets/wall2.png', collider='box')
    starter_wall3 = Entity(model='cube', scale=(15,5,1), position=(92,-1,-80), texture='assets/wall.png', collider='box')
    starter_wall4 = Entity(model='cube', scale=(1,5,20), position=(80,-1,-90), texture='assets/wall.png', collider='box')
    hallway_spawn_main_wall1 = Entity(model='cube', scale=(1,5,10), position=(85,-1,-74.5), texture='assets/wall.png', collider='box')
    hallway_spawn_main_wall2 = Entity(model='cube', scale=(1,5,10), position=(80,-1,-74.5), texture='assets/wall2.png', collider='box')
    test = Entity(model='assets/models/tinker.obj', position=Vec3(93, -3.5, -93))
build_base()

basetemplate = Entity(model='quad', scale=2, position=(5,-1,5), texture='assets/basetemplate.png')

app.run()