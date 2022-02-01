


class World:

    def get_seed(self):
        nbtfile = nbt.NBTFile(self.world_dir / "level.dat", "rb")
        seed = nbtfile["Data"]["WorldGenSettings"]["seed"]
        return seed
    
    def get_spawn_biome(self):
        visited_biomes = self.advancements.get_overworld_biomes()
        
        return 