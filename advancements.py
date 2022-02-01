import json
from pathlib import Path
from datetime import datetime

all_advancements = {
    'minecraft:recipes/misc/charcoal.has_log': 'wood',
    'minecraft:story/iron_tools.iron_pickaxe': 'iron_pick',
    'minecraft:story/enter_the_nether.entered_nether': 'entered_nether',
    'minecraft:nether/explore_nether': 'nether_biomes',
    'minecraft:nether/find_bastion.bastion': 'bastion',
    'minecraft:nether/find_fortress.find_fortress': 'fortress',
    'minecraft:recipes/decorations/ender_chest.has_ender_eye': 'craft_eyes',
    'minecraft:story/follow_ender_eye.follow_ender_eye': 'eye_spy',
    'minecraft:adventure/adventuring_time': 'overworld_biomes',
    'minecraft:story/enter_the_end.entered_end': 'end_entry',
}

def get_inner_map():
    my_map = {}
    names = []
    inners = []
    for advancement in all_advancements.keys():
        inner_val = None
        base_name = advancement
        if '.' in advancement:
            base_name = advancement[:advancement.index('.')]
            inner_val = advancement[advancement.index('.')+1:]
        my_map[base_name] = inner_val
    return my_map

def get_stems():
    return get_inner_map().keys()

class Advancement:
    def __init__(self):
        self.values = None
        self.mc_objective_name = 'default'
        pass
    
    def is_relevant(self):
        return self.get_value() is not None and self.get_mc_name() in get_stems()
    
    def get_mc_name(self):
        return self.mc_name
    
    def get_mc_name_of_objective(self):
        return self.mc_objective_name
    
    def get_name(self):
        if self.mc_objective_name is not None:
            return all_advancements['{}.{}'.format(self.get_mc_name(), self.get_mc_name_of_objective())]
        return all_advancements[self.get_mc_name()]
    
    def get_value(self):
        return self.values

    def get_time(self):
        return self.get_value()
    
    def __str__(self):
        return '{}'.format(self.get_name())
        # return f'{self.get_name()}'
    

def parse_time(time_to_parse):
    time_to_parse = ' '.join(time_to_parse.split(' ')[:2])
    return datetime.strptime(time_to_parse, '%Y-%m-%d %H:%M:%S')

def parse_advancement(adv_name, value):
    advancement = Advancement()
    advancement.mc_name = adv_name
    if adv_name in get_inner_map():
        advancement.mc_objective_name = get_inner_map()[adv_name]
    if advancement.mc_objective_name in value['criteria']:
        advancement.values = [parse_time(value['criteria'][advancement.mc_objective_name])]
    elif advancement.mc_objective_name is None:
        # for biome advancements
        outer = value['criteria']
        advancement.values = [*({entry: outer[entry]} for entry in outer)]
    return advancement

class Advancements:

    def __init__(self):
        self.file = None
        self.advancement_array = []
    
    def check(self):
        self.my_dict = json.load(self.file.open())
        # print(self.my_dict)
        self.advancement_array = []
        for entry in self.my_dict:
            if entry == 'DataVersion':
                continue
            advancement = parse_advancement(entry, self.my_dict[entry])
            if advancement.is_relevant():
                self.advancement_array.append(advancement)
    
    def get_advancement_with_name(self, name):
        for advancement in self.advancement_array:
            if advancement.get_name() == name:
                return advancement

    def get_overworld_biomes(self):
        return self.get_advancement_with_name('overworld_biomes')
    
    def get_nether_biomes(self):
        return self.get_advancement_with_name('nether_biomes')

# adv = Advancements()
# adv.file = Path.cwd() / 'test_advancements.json'
# adv.check()
# print([str(x) for x in adv.advancement_array])
# print(str(adv.advancement_array))