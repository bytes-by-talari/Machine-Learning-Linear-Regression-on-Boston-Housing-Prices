import numpy as np
import matplotlib.pyplot as plt

def estimatecoeff(x, y):
    n = np.size(x)
    m_x = np.mean(x)
    m_y = np.mean(y)
    
    