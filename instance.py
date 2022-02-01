from saver import save_world_async

class Instance:

    def __init__(self, path):
        
        self.mcdir = path
        self.current_world = None

    def check(self):
        updated_current_world = self.get_current_world()
        if updated_current_world != self.current_world:
            self.update_current_world(updated_current_world)

    def update_current_world(self, updated_current_world):
        self.current_world.mark_dead()
        save_world_async(current_world)
        self.current_world = updated_current_worldd
        
    def get_current_world(self):
        max_time = 0.0
        latest_world = None
        for world in (self.mcdir / "saves").iterdir():
            if not world.exists():
                continue
            world_time = world.stat().st_mtime
            if world_time > max_time:
                if settings.get_version() == '1.8':
                    if world.is_dir() and not (world / 'stats').exists():
                        max_time = world_time
                        latest_world = world
                else:
                    if world.is_dir() and not (world / 'advancements').exists():
                        max_time = world_time
                        latest_world = world
        return latest_world
    