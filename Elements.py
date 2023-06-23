from ursina import *


class test_cube(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model="cube",
            texture="brick",
            rotation=(45, 45, 45),
        )


class test_button(Button):
    def __init__(self):
        super().__init__(
            parent=scene,
            model="cube",
            texture="brick",
            rotation=(45, 45, 45),
            highlight_color=color.red,
            pressed_color=color.lime
        )


def update():
    if held_keys['a']:
        t.x -= 1*time.dt
    if held_keys['d']:
        t.x += 1*time.dt


if __name__ == '__main__':
    app = Ursina()
    t = test_button()
    app.run()
