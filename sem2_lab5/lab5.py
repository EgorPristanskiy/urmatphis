#!/usr/bin/env python
# coding: utf-8

# # Решение уравнения теплопроводности стержня 

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[30]:


class Lab5(object):
    def __init__(self, input_data):
        self._init_matrix = input_data
        self._n = self._init_matrix.shape[0]
        self._m = self._init_matrix.shape[1]
    
    def _calculate_cell_value(self, i, j):
        value = self._init_matrix[i, j+1] + 4 * self._init_matrix[i,j]
        value += self._init_matrix[i, j-1]
        return value / 6.0
    
    def _calculate_final_matrix(self):
        for i in range(self._n - 1):
            for j in range(1, self._m-1):
                self._init_matrix[i+1, j] = self._calculate_cell_value(i, j)
    
    def _plot_matrix(self):
        fig = plt.figure(dpi=200)
        ax = fig.add_subplot(111)
        ax.grid(which='major')
        ax.grid(which='minor')
        ax.grid(True)
        for i in range(self._n):
            ax.plot(self._init_matrix[i, :], label="Ряд "+str(i))        
        leg = plt.legend(
            bbox_to_anchor=(0.795,1.01), bbox_transform=plt.gcf().transFigure, ncol=3
        
        )
        leg_lines = leg.get_lines()
        leg_texts = leg.get_texts()
        plt.setp(leg_lines, linewidth=2)
        plt.show()
    
    def _print_matrix(self, message):
        print(message)
        data = pd.DataFrame(self._init_matrix)
        display(data)
    
    def main(self):
        self._print_matrix("Исходные данные")
        self._calculate_final_matrix()
        self._plot_matrix()
        self._print_matrix("Результат")


# ## Решение уравнения из лабораторной работы

# In[31]:


input_matrix = np.zeros((11, 11), dtype="float")
top_edge = np.array([20, 23, 25, 28, 30, 33, 35, 37, 38, 39, 50], dtype="float")
left_edge = np.array([20, 40, 50, 60, 70, 80, 90, 100, 100, 100, 100], dtype="float")
right_edge = np.ones(11) * 40.0

input_matrix[0, :] = top_edge
input_matrix[:, 0] = left_edge
input_matrix[:, -1] = right_edge

lab5 = Lab5(input_matrix)
lab5.main()


# ## Решение уравнения из лекции

# In[32]:


input_matrix = np.zeros((11, 11), dtype="float")
top_edge = np.array([10, 15, 20, 25, 30 ,33, 35, 37, 38, 39, 40], dtype="float")
left_edge = np.array([10, 20, 30, 40, 60, 70, 80, 90, 100, 105, 110], dtype="float")
right_edge = np.array([40, 35, 33, 32, 31, 30, 30, 30, 30, 30, 30], dtype="float")

input_matrix[0, :] = top_edge
input_matrix[:, 0] = left_edge
input_matrix[:, -1] = right_edge

lab5 = Lab5(input_matrix)
lab5.main()

