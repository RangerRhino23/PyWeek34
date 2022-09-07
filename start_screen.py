from fileinput import close
from ursina import *

app = Ursina()


def update():
    pass

def input(key):
    if key == 'q':
        quit()

def run_game():
    os.startfile('run_game.py')
    app.closeWindow()

def quit_game():
    app.closeWindow()

def options():
    pass

logo = Entity(model='quad', texture='assets/logo.png', scale=(8,4), y = 0.1)

start_button = Button(scale=(.875*.24, .05), x=(logo.x-0.05), y=(logo.y-0.2), text='Start Game', on_click=run_game)
options_menu = Button(scale=(.875*.24, .05), x=(start_button.x), y=(start_button.y-0.06), text='Options', on_click=options)
quit_button = Button(scale=(.875*.24, .05), x=(options_menu.x), y=(options_menu.y-0.06), text='Quit', on_click=quit_game)

app.run()