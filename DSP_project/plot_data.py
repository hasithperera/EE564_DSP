


import matplotlib.pyplot as plt
import numpy as np


dump_file = 'dump.txt'

if __name__== '__main__':
    
    with open(dump_file,'rb') as fp:
        data = fp.read()
        
    print(data)
        
    int_array = np.frombuffer(data, dtype=np.uint8);
    
    plt.step(np.arange(0,255),int_array[0:255], where='mid', label='mid')