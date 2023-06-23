from ursina import Entity, camera, Vec3, Vec2, held_keys
from ursina.prefabs.first_person_controller import FirstPersonController

from Textures import Textures


class Hand(Entity):
    def __init__(self):
        self.vec_active = (0.3, -0.5)
        self.vec_passive = (0.4, -0.6)
        super().__init__(
            parent=camera.ui,
            model='assets/arm',
            texture=Textures.create_texture('arm'),
            scale=0.2,
            rotation=Vec3(150, -10, 0),
            position=Vec2(self.vec_passive)
        )

    def active(self):
        self.position = self.vec_active

    def passive(self):
        self.position = self.vec_passive

    def update(self):
        if held_keys['left mouse'] or held_keys['right mouse']:
            self.active()
        else:
            self.passive()


class Player(FirstPersonController):
    def __init__(self):
        super().__init__()
        self.hand = Hand()
