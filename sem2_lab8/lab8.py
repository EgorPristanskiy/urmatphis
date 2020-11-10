#!/usr/bin/env python
# coding: utf-8

# # Фильтрование

# In[36]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', None)


# In[37]:


class Lab8(object):
    def __init__(self, v, s, dp, m, r, t, x, rfp, iterations=361):
        self._s = s
        self._dp = dp
        self._m = m
        self._r = r
        self._t = t
        self._x = x
        self._rfp = rfp
        
        self._v = [v]
        self._w = [0.0]
        
        self._iterations = iterations
    
    def _calculate_new_v(self):
        value = self._v[-1]
        value += self._t * (
            (self._s * self._dp) / \
            (self._m * (
                self._r*self._x*self._v[-1] / self._s + self._rfp
            )
        )
        )
        return value
    
    @staticmethod
    def plot_data(message, data):
        plt.figure(dpi=300)
        plt.title(message)
        plt.grid(True)
        plt.plot(data)
        plt.show()
    
    def print_data(self):
        data = pd.DataFrame(list(zip(self._v, self._w)))
        data.columns = ["V, M3", "W, м/сек"]
        display(data)
    
    def _calculate_new_w(self):
        value = self._v[-1] - self._v[-2]
        return value / (self._s * self._t)
    
    def main(self):
        for i in range(1, self._iterations):
            self._v.append(self._calculate_new_v())
            self._w.append(self._calculate_new_w())
        self.plot_data("Фильтрованиеб М3", self._v)
        self.plot_data("Скорость фильтрования, м/сек", self._w)
        self.print_data()


# In[38]:


v = 0.0
s = 1.0
dp = 30.0
m = 10.0
t = 1.0
x = 1.0
rfp = 20.0
r = 20.0
lab8 = Lab8(v, s, dp, m, r, t, x, rfp)
lab8.main()


# In[ ]:




