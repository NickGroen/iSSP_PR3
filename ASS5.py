import matplotlib.pyplot as plt
import numpy as np

list_vmin = []
list_tmin = []

list_hf = []
list_hw = []
list_tp = []
list_tp2 = []

list_tmin_cor = []


d = [0.5, 1.0 ,1.5 ,2.0, 2.5, 3.0, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 11.5]
for i in range(4,17): # 4 tot 17
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
    plt.plot(time, list_i, alpha=0.4 , linewidth = 1 , label = 'd= '+str(d[i-4]) )
    
    if i != 1:
        
        voltage_min = min(list_i)
        list_vmin.append(voltage_min)
        time_of_min = time[list_i.index(min(list_i))]
        
        list_tmin.append(time_of_min)
        list_tmin_cor.append(time[list_i.index(min(list_i))-38]*10**(-6)) #correction offset
    
    #nearest
    hf1 = voltage_min/2  # half maximum value
    hf = min(list_i[:list_i.index(min(list_i))], key = lambda x: abs(x-hf1)) # finding the value with minimal distance to the desired value
    
    
    hw = time[list_i.index(hf)] # getting the index of the half max value and gettings its time.
    
    list_hw.append(hw) # x
    list_hf.append(hf) # y 
    
    list_tp.append(abs(time_of_min-hw)*10**(-6))
    list_tp2.append((abs(time_of_min-hw)*10**(-6))**2)
    
#    plt.hlines(hf, hw, hw+abs(time_of_min-hw), linestyles = 'dotted', alpha = 0.4)
#    plt.vlines(time_of_min, 0, min(list_i), linestyles = 'dotted', alpha = 0.4)
    
    
    
## finding the right values
    
#plt.plot(list_hw, list_hf,'.', markersize = 10, color = 'r')
#plt.xlabel('Time [ \u03BCs]' )
#plt.ylabel('Voltage [V]' )
    
## plotting tp^2 as function of td
    

fit = []
a, b = np.polyfit(list_tmin_cor, list_tp2, 1)
for i in range(0, len(list_tmin_cor)):
    fit.append(list_tmin_cor[i]*a +b)

plt.plot(list_tmin_cor, list_tp2, '.', color = 'b')
plt.plot(list_tmin_cor, fit, ':', color = 'b', label= 'fit: '+str(round(a,6))+'x +'+str(round(b,8)))

plt.xlabel('$t_d$')
plt.ylabel('$t_p^2$')
plt.legend()

Dif_const = ((13.11**2)/(11.07))*a
print(Dif_const)

