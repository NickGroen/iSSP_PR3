import matplotlib.pyplot as plt
import numpy as np
import math as m
import scipy
from scipy import integrate





list_vmin = []
list_tmin = []

list_hf = []
list_hw = []
list_tp = []
list_tp2 = []

list_tmin_cor = []
list_tmin_cor2 = []
integral_values = []

colour = ['b', 'r', 'g', 'c','m','y', 'orange', 'purple','brown', 'indigo']
d = [0.5, 1.0 ,1.5 ,2.0, 2.5, 3.0, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]
d_mm = [element *10**(-3) for element in d]
#d = [0.5, 1.0 ,1.5 ,2.0, 2.5, 3.0, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 11.5]
for i in range(4,7): # 4 tot 17
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
    
    
    if i != 1:
        
        voltage_min = min(list_i)
        list_vmin.append(voltage_min)
        time_of_min = time[list_i.index(min(list_i))]
        
        list_tmin.append(time_of_min)
        list_tmin_cor.append(time[list_i.index(min(list_i))-38]*10**(-6)) #correction offset
        list_tmin_cor2.append(time[list_i.index(min(list_i))]*10**(-6))



    t1 = np.linspace(0,1000, len(list_i)) 
    
    
    D_n = 2.99*10**(-3)
#    mu_n = 0.0935 #exp
    tau = 724*10**(-6)



#for r in range(0,3) :
    dp_list = []
    
    t_r =[]
    for s in range(1,len(t1)):
        t = t1[s]*10**(-6)
        t_r.append(t)
        dp = -(1/((4*m.pi*D_n*t)))*np.exp((-t/tau)-(((d_mm[i-4])-(mu_n*136.86*t))**2/(4*D_n*t)))
        dp_list.append(dp)
    scale = ((min(list_i)/min(dp_list)))
    dp_list_1 = [element *scale for element in dp_list]
    t_r_offset = [element +37E-6 for element in t_r]
    
    plt.plot(t_r, list_i[1:], alpha=0.8 , color = colour[i-4] ,  linewidth = 1 , label = 'd = '+str(d[i-4])+' mm' )
    plt.plot(t_r_offset, dp_list_1,':', color = colour[i-4], label = 'x = '+str(d[i-4])+' mm')
plt.xlabel('time [s]')    
plt.ylabel('Signal [V]')
plt.legend()
    
    
    
    
    