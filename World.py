from Voxel import Voxel


class World:
    def __init__(self, world_size=30):
        for z in range(world_size):
            for x in range(world_size):
                new_voxel = Voxel(position=(x, 0, z))
