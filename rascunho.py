import numpy as np
from math import sin

def build_senoide(freq,t):
    A=1
    return A*sin(2*freq*t)

myFn = np.vectorize(build_senoide, excluded=['freq'])

t=np.linspace(0,1,44101)

print(myFn(1,t))