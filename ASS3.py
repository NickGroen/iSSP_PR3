import matplotlib.pyplot as plt
import numpy as np

list_vmin = []
list_tmin = []
d = [0.5, 1.0 ,1.5 ,2.0, 2.5, 3.0, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 11.5]
for i in range(4,17):
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
        

#plt.plot(list_tmin, list_vmin, '.',  linewidth = 5 , label = 'minimal values', color = 'r')
#plt.grid()
plt.xlabel('Time [\u03BCs]')
plt.ylabel('Voltage [V]')
#plt.xlim(40, 600)
#plt.legend()
# plot y = d and x = t_d




d = [0.5, 1.0 ,1.5 ,2.0, 2.5, 3.0, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 11.5]
v_d = []
u_e = []
for k in range(0, len(d)-1):
    v_d1 = (d[k+1]/((list_tmin[k]-40)*10**(-3)))
    v_d.append(d[k+1]/((list_tmin[k]-40)*10**(-3)))
    u_e.append(v_d1 * (40*10**(-3))/5.4738)
#    

#opgave 3:
t_d = []
d_list = []

d = [ 1.0 ,1.5 ,2.0, 2.5, 3.0, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 11.5]

for m in range(0, len(list_tmin)):
    t_d.append((list_tmin[m]-40)*10**(-6))
    d_list.append(d[m]*10**(-3))
    
#plt.plot(t_d, d,'.', color = 'b')
plt.plot(t_d[:6], d_list[:6],'.', color = 'b')
plt.plot(t_d[7:], d_list[7:],'.', color = 'b')    
m, b = np.polyfit(t_d, d_list, 1)
time_fit = np.linspace(0, max(t_d), len(t_d))
fit = []
for p in range(0, len(time_fit)):
    fit.append(time_fit[p]*m+b)
    
plt.plot(time_fit, fit, label = "fit: "+str(round(m,2))+"x + "+str(round(b,4)))
plt.xlabel('time to peak [s]')
plt.ylabel('distance [m]')
plt.legend()
    
    
    
    
    
    
    
    
    