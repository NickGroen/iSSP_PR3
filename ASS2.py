

import matplotlib.pyplot as plt
import numpy as np

list_vmin = []
list_tmin = []

voltage_i = ['7,5 V', '10 V', '3 V', '6 V']
time_i = [ '4 \u03BCs', '8 \u03BCs', '40 \u03BCs', '60 \u03BCs']
#for i in range(18,22): #2a
for i in range(22,26): #2b
    if i<10:
        correction = str("0"+str(i))
        file_i = str("TRAV8_"+str(correction)+".txt")
    if i>10:
        file_i = str("TRAV8_"+str(i)+".txt")
        
    list_i = []
    open_file = open(file_i,"r+").read().split(',')
    
    for j in range(1,len(open_file)): 
        list_i.append(float(open_file[j]))
        
    time = np.linspace(0, 1000, len(list_i))
#    plt.plot(time, list_i, alpha=0.4 , linewidth = 1 , label = voltage_i[i-18]) #2a
    plt.plot(time, list_i, alpha=0.4 , linewidth = 1 , label = time_i[i-22]) #2b
    if i != 1:
        
        voltage_min = min(list_i)
        list_vmin.append(voltage_min)
        time_of_min = time[list_i.index(min(list_i))]
        list_tmin.append(time_of_min)
        

#2a
plt.plot(list_tmin, list_vmin, '.',  linewidth = 5 , label = 'minimal values', color = 'r')
plt.xlabel('time [us]')
plt.ylabel('Voltage [V]')
#t_d = []
#d_list = []
plt.legend()

#2b

    
    
    
    
    
    
    
    
    