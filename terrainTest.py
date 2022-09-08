#Imports Ursina Engine
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()

terrain_entity = Entity(model=Terrain('heightmap_1', skip=8), scale=(400, 10, 400), texture='assets/ground.png')
#player = FirstPersonController(speed=15, y=3, position=Vec3(90, -3.5, -90))
player= Entity(True)
player.origin = Vec3(0,0,0)

terrain_entity.collider = MeshCollider(terrain_entity, mesh=terrain_entity.model, center=Vec3(0,0,0)) 
hv = terrain_entity.model.height_values

def update():
    camera.fov = 90
    camera.y = 0
    direction = Vec3(held_keys['d'] - held_keys['a'], 0, held_keys['w'] - held_keys['s']).normalized()
    #player.position += direction * time.dt * 4
    player.y = terraincast(player.world_position, terrain_entity, hv)

#Keyboard Dectection
def input(key):
    if key == 'q':
        quit()
    if key == 'g':
        EditorCamera()
    if key == 'f':
        print(player.position)

EditorCamera()
Sky(texture='assets/sky.png')
app.run()