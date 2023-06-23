from ursina import Entity
from Textures import Textures


class Sky(Entity):
    def __init__(self, scale=150):
        super().__init__(
            parent=scale,
            model='sphere',
            texture=Textures.create_texture('sky'),
            scale=scale,
            double_sided=True,
        )


