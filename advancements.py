import json
from pathlib import Path

all_advancements = {
    'minecraft:recipes/misc/charcoal': 'wood',
    'minecraft:story/iron_tools': 'iron_pickaxe',
    'minecraft:nether/explore_nether': 'nether_biomes',
    'minecraft:nether/find_bastion': 'bastion',
    'minecraft:nether/find_fortress': 'fortress',
    'minecraft:recipes/decorations/ender_chest': 'has_ender_eye',
    'minecraft:story/follow_ender_eye': 'in_stronghold',
    'minecraft:adventure/adventuring_time': 'overworld_biomes',
    'minecraft:story/enter_the_end': 'end_entry',
}

class Advancement:
    def __init__(self):
        pass
    
    def is_relevant(self):
        return self.get_mc_name() in all_advancements.keySet()
    
    def get_mc_name(self):
        pass
    
    def get_internal_name(self):
        pass
    
    def get_value(self):
        pass
    
    def get_time(self):
        pass

def parse_advancement(advancement, value):
    print(advancement)
    print(value)
    pass

class Advancements:

    def __init__(self):
        self.file = None
        self.advancement_array = []
        pass
    
    def check(self):
        self.my_dict = json.load(self.file.open())
        # print(self.my_dict)
        self.advancement_array = None
        for entry in self.my_dict:
            advancement = parse_advancement(entry, self.my_dict[entry])
            self.advancement_array.append()
        pass

    def get_overworld_biomes(self):
        pass

adv = Advancements()
adv.file = Path.cwd() / 'test_advancements.json'
adv.check()
print(adv.advancement_array)