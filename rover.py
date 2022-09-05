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
    global onrover
    if key == 'q':
        quit()
    if key == 'g':
        EditorCamera()
    if key == 'f':
        print(player.position)
    #Rover Movment
    if key == 'enter':
        if onrover == True:
            onrover = False
            player.x += 4
        elif onrover == False:
            onrover = True
#Player
player = FirstPersonController(speed=15, y=3, position=Vec3(90, -3.5, -90))

#Ground
ground = Entity(model='cube', scale=(1000,1,1000), y=-4, texture='assets/ground.png', collider='box')

rover = Entity(model='assets/models/rover.glb', scale=(15), position=(28,-0.5,-78), rotation_y=180, collider='box')

app.run()