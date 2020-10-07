import pandas as pd
import numpy as np
from multiprocessing import shared_memory
import time
start = time.time()

flag = 1

print("============= loading matrix... =============")
cat_sim = np.load('CBF_Matrix.npy')
item_sim_df = pd.read_csv('item_sim.csv')
item_sim = item_sim_df.values
cat_sim = cat_sim.argsort()[:, ::-1]

shm_cbf = shared_memory.SharedMemory(name= 'CBF_Matrix', create=True, size= cat_sim.nbytes)
shm_ibcf = shared_memory.SharedMemory(name= 'IBCF_Matrix', create=True, size= item_sim.nbytes)
b_cbf = np.ndarray(cat_sim.shape, dtype= cat_sim.dtype, buffer= shm_cbf.buf)
b_ibcf = np.ndarray(item_sim.shape, dtype= item_sim.dtype, buffer= shm_ibcf.buf)

print("============= Done! =============")

while(flag == 1):
    #print(type(b_cbf))
    #print(type(b_ibcf))
    #print(b_cbf)
    #print(b_ibcf)
    time.sleep(300)
    print('The matrices are in memory')
    print(time.time() - start)
    continue

shm_cbf.unlink()
shm_ibcf.unlink()
