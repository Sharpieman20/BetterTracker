import threading

save_lock = threading.Lock()




def save_world(world):

    pass

def try_save_world(world):
    save_lock.acquire()
    save_world(world)
    save_lock.release()

def save_world_async(world):
    thread = threading.Thread(target=try_save_world, args=(world))
    thread.start()
