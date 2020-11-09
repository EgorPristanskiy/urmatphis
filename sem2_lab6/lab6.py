#!/usr/bin/env python
# coding: utf-8

# In[73]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', None)


# In[78]:


class Lab6(object):
    def __init__(self, u, s, p, start_m, end_m, delta_step):
        self._s = s
        self._u = u
        self._p = p
        self._start_m = start_m
        self._end_m = end_m
        self._delta_m_per_sec = u * s * p
        self._delta_step = delta_step
        
        self._mass = [self._start_m]
        self._a = [0]
        self._v = [0]
        self._l = [0]
    
    def _calculate_mass(self):
        return self._mass[-1]-self._delta_m_per_sec * self._delta_step
    
    def _calculate_a(self):
        return self._u * self._delta_m_per_sec / self._mass[-1] 
    
    def _calculate_v(self):
        return self._v[-1] + self._delta_step * self._a[-1]
    
    def _calculate_l(self):
        return self._l[-1] + self._delta_step * self._v[-1]
    
    def _print_results(self):
        time = np.arange(0, len(self._mass))
        result = pd.DataFrame(list(zip(
            time, self._mass, self._a, self._v, self._l
        )))
        result.columns = ['t', 'M', 'A', 'V', 'L']
        display(result)
    
    def _plot_results(self):
        fig = plt.figure(dpi=200)
        ax = fig.add_subplot(111)
        ax.grid(which='major')
        ax.grid(which='minor')
        ax.grid(True)
        ax.plot(self._mass, label='M')
        ax.plot(self._a, label='A')
        ax.plot(self._v, label='V')
        ax.plot(self._l, label='L')        
        leg = plt.legend(
            bbox_to_anchor=(0.795,1.01), bbox_transform=plt.gcf().transFigure, ncol=4
        
        )
        leg_lines = leg.get_lines()
        leg_texts = leg.get_texts()
        plt.setp(leg_lines, linewidth=2)
        plt.show()
    
    def main(self):
        while self._mass[-1] > self._end_m:
            self._a.append(self._calculate_a())
            self._mass.append(self._calculate_mass())
            self._v.append(self._calculate_v())
            self._l.append(self._calculate_l())
        self._plot_results()
        self._print_results()


# In[79]:


start_m = 400.0
end_m = 50.0
s = 5e-5
p=10**4
u=2.0
delta_step=1
lab6 = Lab6(u, s, p, start_m, end_m, delta_step)
lab6.main()

