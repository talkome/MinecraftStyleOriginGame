from ursina import *
from Block_type import Block
from Textures import Textures


class Voxel(Button):
    block = Block.grass

    def __init__(self, position=(0, 0, 0), texture_name="grass"):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=0.5,
            texture=Textures.create_texture(texture_name),
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=0.5
        )

    def input(self, key):
        if held_keys['1']:
            Voxel.block = Block.grass
        if held_keys['2']:
            Voxel.block = Block.stone
        if held_keys['3']:
            Voxel.block = Block.brick
        if held_keys['4']:
            Voxel.block = Block.dirt

        if self.hovered:
            if key == 'left mouse down':
                if Voxel.block == Block.grass:
                    new_voxel = Voxel(position=self.position + mouse.normal, texture_name='grass')
                if Voxel.block == Block.stone:
                    new_voxel = Voxel(position=self.position + mouse.normal, texture_name='stone')
                if Voxel.block == Block.brick:
                    new_voxel = Voxel(position=self.position + mouse.normal, texture_name='brick')
                if Voxel.block == Block.dirt:
                    new_voxel = Voxel(position=self.position + mouse.normal, texture_name='dirt')

            if key == 'right mouse down':
                destroy(self)
