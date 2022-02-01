
import time
from pathlib import Path
from instance import Instance

instances = []

instance_fil = Path.cwd() / 'instances.txt'


for ln in instance_fil.open('r'):
    instances.append(Instance(ln))


loop_delay = 0.1

while (True):
    for instance in instances:
        instance.check()
    time.sleep(loop_delay)