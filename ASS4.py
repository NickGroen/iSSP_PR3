import matplotlib.pyplot as plt
import numpy as np

L = 40*10**(-3)

list_vmin = []
list_tmin = []



# volt 9



volt_9= [ 1.1813, 1.5589, 1.9732, 2.5700, 3.0211, 3.5591, 3.9675, 4.3375, 5.8585, 6.979, 8.458, 9.637, 10.742 ]
volt_75 = [ 1.3484, 1.7119, 2.1775, 2.5188, 2.9196, 3.9820, 4.7158, 5.5463, 6.558, 7.533, 8.451 ]
volt_25 = [ 5.4730, 5.7354, 5.9530, 6.5500, 7.111, 7.539, 2.5991, 3.4289, 4.3661, 7.292, 7.947 ]
E = []
#d = [0.5, 1.0 ,1.5 ,2.0, 2.5, 3.0, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 11.5]

#start = 50 #volt 75
#start = 26 # volt 25
start = 37 # volt_9
for i in range(start, start+len(volt_9)):
#for i in range(50, 61):
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

    
    E.append(volt_9[i-start]/L)
    print(volt_9[i-start])
    if i != 1:
        
        voltage_min = min(list_i)
        list_vmin.append(voltage_min)
        time_of_min = time[list_i.index(min(list_i))]
        list_tmin.append(time_of_min)
        
plt.xlabel('E [V/m]')
plt.ylabel('V drift [m/s]')

d = [0.5, 1.0 ,1.5 ,2.0, 2.5, 3.0, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 11.5]
v_d = []
for k in range(0, len(d)-1):
    v_d1 = (d[k+1]/((list_tmin[k]-40)*10**(-3)))
    v_d.append(d[k+1]/((list_tmin[k]-40)*10**(-3)))

    

plt.plot(E, v_d, '.')

fit = []
a, b = np.polyfit(E, v_d, 1)
for i in range(0, len(E)):
    fit.append(E[i]*a +b)

plt.plot(E, fit, 'b', label = 'fit +'+str(round(a,4))+"x + "+str(round(b,6)))

##################################################################################
##################################################################################

    
    
    
    