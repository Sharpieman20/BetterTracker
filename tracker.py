
import time
from pathlib import Path
from instance import Instance
from saver import save_to_disk

instances = []

instance_fil = Path.cwd() / 'instances.txt'


for ln in instance_fil.open('r'):
    instances.append(Instance(ln))


loop_delay = 0.2

last_save_time = time.time()
save_interval = 10.0

while (True):
    for instance in instances:
        instance.check()
    time.sleep(loop_delay)
    if time.time() - last_save_time > save_interval:
        save_to_disk()
