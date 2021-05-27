from tqdm import tqdm, trange
from time import sleep

for i in trange(50):
    sleep(0.1)

# OR

for i in tqdm(range(5)):
    sleep(0.4)
