##assignment 6:

import matplotlib.pyplot as plt
import numpy as np
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

d = [0.5, 1.0 ,1.5 ,2.0, 2.5, 3.0, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]
d_mm = [element *10**(-3) for element in d]
#d = [0.5, 1.0 ,1.5 ,2.0, 2.5, 3.0, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 11.5]
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
#    plt.plot(time, list_i, alpha=0.4 , linewidth = 1 , label = 'd= '+str(d[i-4]) )
    
    if i != 1:
        
        voltage_min = min(list_i)
        list_vmin.append(voltage_min)
        time_of_min = time[list_i.index(min(list_i))]
        
        list_tmin.append(time_of_min)
        list_tmin_cor.append(time[list_i.index(min(list_i))-38]*10**(-6)) #correction offset
        list_tmin_cor2.append(time[list_i.index(min(list_i))]*10**(-6))
    
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
    
    #integrating the fucker: i suck at integration so i'll hand select everything.
    list_i_select = []
    time_i_select = []
    for p in range(list_i.index(min(list_i))-2,list_i.index(min(list_i))+2):
        list_i_select.append(list_i[p])
        time_i_select.append(time[p])
        
        
    y_int = integrate.cumtrapz(list_i_select, time_i_select)
    print(sum(y_int))
    integral_values.append(abs(sum(y_int)))
## fuck. hieronder werkt niet
#    list_i_select = []
#    time_i_select = []
#    for p in range(list_i.index(hf),list_i.index(min(list_i))):
#        list_i_select.append(list_i[p])
#        time_i_select.append(time[p])
#        
#    y_int = integrate.cumtrapz(list_i_select, time_i_select)
#    print(sum(y_int))
    

    
#plt.plot(list_hw, list_hf,'.', markersize = 10, color = 'r')
#plt.xlabel('Time [ \u03BCs]' )
#plt.ylabel('Voltage [V]' )
plt.plot(list_tmin_cor2, integral_values, '.')
plt.xlabel(' Transit time Td [s]')
plt.ylabel(' Integral of measured intensity [-]')

#np.polyfit(np.log(d_mm), integral_values, 1)
a, b = scipy.optimize.curve_fit(lambda t,a,b: a*np.exp(b*t),  list_tmin_cor2,  integral_values,  p0=(1, 0))
exp_fit = []
exp_fit_2 = []
for n in range(len(integral_values)):
#    exp_fit.append(a[0]*np.exp(1.1*a[1]*n)+0.07)
    
    exp_fit.append(a[0]*np.exp(0.00005*a[1]*n))
    
#    exp_fit.append(a[0]*np.exp(a[1]*n))

plt.plot(list_tmin_cor, exp_fit, label = 'fit: '+str(round(1.1*a[0],2))+'*exp('+str(round(a[1],2))+'*d)+0.07')
#plt.plot(d_mm, exp_fit_2, label = '2')
plt.legend()

