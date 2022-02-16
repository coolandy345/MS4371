
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSvg import *
import numpy as np
source = np.arange(20).reshape(10,2)
print(source)


add_source2 = np.arange(5,15).reshape(10,1)
print(add_source2)
source[0:10,0:1] =add_source2

print(source)
