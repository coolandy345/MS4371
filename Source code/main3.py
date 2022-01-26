import numpy as np
import time
source = np.arange(20).reshape(10,2)
print(source)


add_source2 = np.arange(5,15).reshape(10,1)
print(add_source2)
source[0:10,0:1] =add_source2

print(source)
