import time
from advancements import Advancements, parse_time
from pathlib import Path
from saver import save_world, save_to_disk
from nbt import nbt


class World:
    def __init__(self, path):
        self.creation_time = None
        self.exited_time = None
        self.advancements = None
        self.path = path
        self.check()

    def mark_active(self):
        self.creation_time = time.time()
    
    def mark_dead(self):
        self.exited_time = time.time()
    
    def check(self):
        if self.exited_time is not None:
            return
        self.advancements = Advancements()
        adv_dir = (self.path / 'advancements')
        if not adv_dir.exists():
            return
        for fil in adv_dir.iterdir():
            self.advancements.file = fil
        self.advancements.check()

    def get_seed(self):
        nbtfile = nbt.NBTFile(self.path / "level.dat", "rb")
        seed = nbtfile["Data"]["WorldGenSettings"]["seed"]
        return seed

    def get_first_biome(self, visited_biomes):
        min_visit_time = None
        first_biome = None
        for inner_dict in visited_biomes:
            for key, val in inner_dict.items():
                visit_time = parse_time(val)
                if min_visit_time is None or visit_time < min_visit_time:
                    min_visit_time = visit_time
                    first_biome = key
        return first_biome

    def get_spawn_biome(self):
        if self.advancements.get_overworld_biomes() is None:
            return None
        return self.get_first_biome(self.advancements.get_overworld_biomes().get_value())
    
    def get_nether_spawn_biome(self):
        if self.advancements.get_nether_biomes() is None:
            return None
        return self.get_first_biome(self.advancements.get_nether_biomes().get_value())

    def get_time_for_advancement(self, name):
        if self.advancements.get_advancement_with_name(name) is None:
            return None
        return self.advancements.get_advancement_with_name(name).get_value()
    
    def get_wood_time(self):
        return self.get_time_for_advancement('wood')
    
    def get_iron_pick_time(self):
        return self.get_time_for_advancement('iron_pick')
    
    def get_nether_entry_time(self):
        return self.get_time_for_advancement('entered_nether')
    
    def get_bastion_entry_time(self):
        return self.get_time_for_advancement('bastion')
    
    def get_fortress_entry_time(self):
        return self.get_time_for_advancement('fortress')
    
    def get_eye_craft_time(self):
        return self.get_time_for_advancement('craft_eyes')
    
    def get_eye_spy_time(self):
        return self.get_time_for_advancement('eye_spy')
    
    def get_end_entry_time(self):
        return self.get_time_for_advancement('end_entry')


    def to_dict(self):
        return {
            'created_time': self.creation_time,
            'spawn_biome': self.get_spawn_biome(),
            'wood_time': self.get_wood_time(),
            'iron_pick_time': self.get_iron_pick_time(),
            'entry_time': self.get_nether_entry_time(),
            'nether_spawn_biome': self.get_nether_spawn_biome(),
            'bastion_time': self.get_bastion_entry_time(),
            'fortress_time': self.get_fortress_entry_time(),
            'exit_time': self.get_eye_craft_time(),
            'eye_spy_time': self.get_eye_spy_time(),
            'enter_end_time': self.get_end_entry_time(),
            'quit_time': self.exited_time,
            'seed': self.get_seed()
        }

