import threading
import pandas as pd

save_lock = threading.Lock()


def get_global_df():
    global df
    if 'df' not in globals():
        df = pd.DataFrame()
    return df

def set_global_df(new_df):
    global df
    df = new_df

def save_to_disk():
    # print(get_global_df())
    get_global_df().to_csv('out.csv')

def save_world(world):
    world_dict = world.to_dict()
    world_series = pd.Series(world_dict)
    df = get_global_df()
    # print(world_series)
    set_global_df(df.append(world_series, ignore_index=True))
    # print(df)
    pass

def try_save_world(world):
    save_lock.acquire()
    save_world(world)
    save_lock.release()

def save_world_async(world):
    thread = threading.Thread(target=try_save_world, args=(world,))
    thread.start()
