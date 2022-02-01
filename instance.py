from saver import save_world_async
from pathlib import Path
from world import World

class Instance:

    def __init__(self, path):
        
        self.mcdir = Path(path)
        self.current_world = None

    def check(self):
        updated_current_world = self.get_current_world()
        if self.current_world is None or updated_current_world != self.current_world.path:
            print('{} to {}'.format(self.current_world, updated_current_world))
            self.update_current_world(updated_current_world)
        else:
            self.current_world.check()

    def update_current_world(self, updated_current_world):
        if self.current_world is not None:
            self.current_world.mark_dead()
            save_world_async(self.current_world)
        self.current_world = World(updated_current_world)
        self.current_world.mark_active()
        
    def get_current_world(self):
        max_time = 0.0
        latest_world = None
        for world in (self.mcdir / 'saves').iterdir():
            if not world.exists():
                continue
            world_time = world.stat().st_mtime
            if world_time > max_time:
                if world.is_dir():
                    max_time = world_time
                    latest_world = world
        return latest_world
    