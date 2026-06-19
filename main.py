from ursina import *
from math import sin, cos, radians
import random

app = Ursina()

window.color = color.black
window.title = "3D Solar System"

# ================= CAMERA =================

EditorCamera()

camera.position=(0,30,-90)
camera.rotation_x=20

# ================= SUN =================

sun = Entity(
    model='sphere',
    scale=3,
    color=color.rgb(255,220,50),
    position=(0,0,0),
    unlit=True
)

Text(
    text='Sun',
    world_parent=sun,
    y=1.7,
    scale=8
)

Entity(
    parent=sun,
    model='sphere',
    scale=3.8,
    color=color.rgba(
        255,
        180,
        0,
        70
    ),
    unlit=True
)

# ================= STARS =================

for i in range(1200):

    Entity(
        model='sphere',
        scale=.03,
        color=color.white,
        unlit=True,
        position=(
            random.uniform(-300,300),
            random.uniform(-300,300),
            random.uniform(-300,300)
        )
    )

# ================= PLANETS =================

planet_data=[

{"name":"Mercury","radius":5,"size":0.25,"speed":4.7,"color":color.rgb(140,140,140)},
{"name":"Venus","radius":8,"size":0.40,"speed":3.5,"color":color.rgb(230,190,138)},
{"name":"Earth","radius":12,"size":0.45,"speed":3,"color":color.rgb(40,110,255)},
{"name":"Mars","radius":16,"size":0.35,"speed":2.4,"color":color.rgb(210,80,40)},
{"name":"Jupiter","radius":24,"size":1.2,"speed":1.3,"color":color.rgb(214,181,138)},
{"name":"Saturn","radius":32,"size":1,"speed":1,"color":color.rgb(224,202,144)},
{"name":"Uranus","radius":40,"size":0.8,"speed":0.7,"color":color.rgb(180,255,255)},
{"name":"Neptune","radius":48,"size":0.75,"speed":0.55,"color":color.rgb(50,70,255)},
{"name":"Pluto","radius":56,"size":0.15,"speed":0.4,"color":color.rgb(180,160,150)}
]

planets=[]

for p in planet_data:

    planet=Entity(
        model='sphere',
        scale=p["size"],
        color=p["color"],
        unlit=True
    )

    Text(
        text=p["name"],
        world_parent=planet,
        y=1.3,
        scale=7,
        billboard=True
    )

    p["entity"]=planet
    p["angle"]=random.randint(0,360)

    planets.append(p)

    # Orbit rings

    orbit=[]

    for a in range(361):

        x=p["radius"]*cos(radians(a))
        z=p["radius"]*sin(radians(a))

        orbit.append(
            Vec3(x,0,z)
        )

    Entity(
        model=Mesh(
            vertices=orbit,
            mode='line'
        ),
        color=color.rgba(
            130,
            130,
            130,
            100
        ),
        unlit=True
    )

    # Saturn rings

    if p["name"]=="Saturn":

        Entity(
            parent=planet,
            model='circle',
            scale=2.8,
            rotation_x=90,
            color=color.rgba(
                220,
                200,
                150,
                180
            ),
            unlit=True
        )

# ================= UPDATE =================

def update():

    # WASD movement

    speed=30*time.dt

    if held_keys["w"]:
        camera.position += camera.forward*speed

    if held_keys["s"]:
        camera.position -= camera.forward*speed

    if held_keys["a"]:
        camera.position -= camera.right*speed

    if held_keys["d"]:
        camera.position += camera.right*speed

    if held_keys["q"]:
        camera.y += speed

    if held_keys["e"]:
        camera.y -= speed

    sun.rotation_y += 5*time.dt

    for p in planets:

        p["angle"] += (
            p["speed"]
            *time.dt
            *20
        )

        x = p["radius"]*cos(
            radians(p["angle"])
        )

        z = p["radius"]*sin(
            radians(p["angle"])
        )

        p["entity"].position=(
            x,
            0,
            z
        )

app.run()