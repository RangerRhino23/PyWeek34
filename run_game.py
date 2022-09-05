from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()

Sky(texture='assets/sky.png')

#variables
onrover = False

def update():
    camera.fov = 90
    camera.y = 0
    player.speed = 15
    if held_keys['r']:
        player.speed = 20
    if held_keys['left shift']:
        camera.y = -0.25
        player.speed = 10
    if held_keys['c']:
        camera.fov = 60
    #Rover Movement
    if onrover == True:
        player.gravity = 0
        player.x = rover.x
        player.y = rover.y+1
        player.z = rover.z
        if held_keys['a']:
            rover.rotation_y -= 50 * time.dt
        if held_keys['d']:
            rover.rotation_y += 50 * time.dt
        if held_keys['w']:
            rover.position += -rover.forward * 0.05
        if held_keys['s']:
            rover.position += rover.forward * 0.05
    if onrover == False:
        player.gravity = 1

def input(key):
    if key == 'q':
        quit()
    if key == 'g':
        EditorCamera()
    if key == 'f':
        print(player.position)
    if garage_door.hovered:
        if key == 'left mouse down':
            garage_door.y = 6
        if key == 'right mouse down':
            garage_door.y = 1.5
    #Rover Movment
    global onrover
    if key == 'enter':
        if onrover == True:
            onrover = False
            player.x += 4
        elif onrover == False:
            onrover = True

#Player
player = FirstPersonController(speed=15, y=3, position=Vec3(90, -3.5, -90))

#Ground
ground = Entity(model='cube', scale=(200,1,200), y=-4, texture='assets/ground.png', collider='box')

def build_base_walls():
    wall1 = Entity(model='cube', scale=(20,5,1), position=(90,-1,-100), texture='assets/wall4.png', collider='box')
    wall2 = Entity(model='cube', scale=(1,5,20), position=(100,-1,-90), texture='assets/wall2.png', collider='box')
    wall3 = Entity(model='cube', scale=(15,5,1), position=(92,-1,-80), texture='assets/wall3.png', collider='box')
    wall4 = Entity(model='cube', scale=(1,5,15), position=(80,-1,-92), texture='assets/wall.png', collider='box')
    wall5 = Entity(model='cube', scale=(1,5,10), position=(85,-1,-74.5), texture='assets/wall.png', collider='box')
    wall6 = Entity(model='cube', scale=(1,5,11), position=(80,-1,-74), texture='assets/wall2.png', collider='box')
    wall7 = Entity(model='cube', scale=(10,5,1), position=(74.5,-1,-85), texture='assets/wall3.png', collider='box')
    wall8 = Entity(model='cube', scale=(11,5,1), position=(75,-1,-80), texture='assets/wall2.png', collider='box')
    wall9 = Entity(model='cube', scale=(1,5,11), position=(70,-1,-91), texture='assets/wall.png', collider='box')
    wall10 = Entity(model='cube', scale=(20,5,1), position=(59.5,-1,-97), texture='assets/wall4.png', collider='box')
    wall11 = Entity(model='cube', scale=(1,5,20), position=(50,-1,-86.5), texture='assets/wall2.png', collider='box')
    wall12 = Entity(model='cube', scale=(20,5,1), position=(59.5,-1,-70), texture='assets/wall4.png', collider='box')
    wall13 = Entity(model='cube', scale=(1,5,10), position=(70,-1,-74.5), texture='assets/wall2.png', collider='box')
    wall14 = Entity(model='cube', scale=(10,5,1), position=(44.5,-1,-77), texture='assets/wall.png', collider='box')
    wall15 = Entity(model='cube', scale=(10,5,1), position=(44.5,-1,-70), texture='assets/wall3.png', collider='box')
    wall16 = Entity(model='cube', scale=(1,5,20), position=(40,-1,-87.5), texture='assets/wall2.png', collider='box')
    wall17 = Entity(model='cube', scale=(20,5,1), position=(29.5,-1,-97), texture='assets/wall4.png', collider='box')
    wall18 = Entity(model='cube', scale=(1,5,20), position=(19,-1,-87), texture='assets/wall2.png', collider='box')
    wall19 = Entity(model='cube', scale=(20,5,1), position=(29.5,-1,-59), texture='assets/wall4.png', collider='box')
    wall20 = Entity(model='cube', scale=(1,5,10), position=(40,-1,-64.5), texture='assets/wall2.png', collider='box')
    wall22 = Entity(model='cube', scale=(1,5,20), position=(80,-1,-58.5), texture='assets/wall2.png', collider='box')
    wall23 = Entity(model='cube', scale=(20,5,1), position=(90,-1,-48), texture='assets/wall4.png', collider='box')
    wall24 = Entity(model='cube', scale=(1,5,20), position=(100,-1,-58.5), texture='assets/wall2.png', collider='box')
    wall25 = Entity(model='cube', scale=(15,5,1), position=(92,-1,-69), texture='assets/wall3.png', collider='box')
build_base_walls()



garage_door = Button(color=color.white, model='cube', texture='assets/garage.png', position=(19,1.5,-68), scale=(1,5,18), parent=scene, origin_y=0.5)

rover = Entity(model='assets/models/rover.glb', scale=(13), position=(28,-0.5,-83), rotation_y=180, collider='box')

app.run()