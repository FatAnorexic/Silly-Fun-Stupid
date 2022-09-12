#This program is designed to calculate the stresses and forces a squirell would experience
#falling from space.

import numpy as np

m=0.57    #Mass of the squirell

g=9.81    #While the acceleration will not be this strong at higher altitudes, it changes only
          #slightly. this calculator was merely designed as an estimate. Thus for simplicity sake
          #I decided to keep g constant.

C_d=0.993 #Co-efficient of drag of a squirell and its cross-sectional area
A=0.085

c_p=4200  #heat capacity of water-assuming squirell has a space suit that uses water cooling.

#Measures of air density from 80km to sea level:https://www.engineeringtoolbox.com/standard-atmosphere-d_604.html
rho=[0.00001846,0.00008283,0.0003097,0.001027,0.003996,0.01841,0.04008,0.08891,0.1948,0.4135,0.4671,0.5258,0.5900,
     0.6601,0.7364,0.8194,0.9093,1.007,1.112,1.225]

#Array of height in meters from 80km to sea level
h=[80000,70000,60000,50000,40000,30000,25000,20000,15000,10000,9000,8000,7000,6000,5000,4000,3000,2000,1000,1]


v_t=[]
#find the terminal velocity for each array of height and density(rho)
for i in range(len(rho)):
     v_terminal=np.sqrt((2*m*g)/(rho[i]*C_d*A))
     v_t.append(v_terminal)

print(np.array(v_t),"\n")

t=[]

#The time our squirell will fall through each measure in altitude
for i in range(len(v_t)-1):
     l=(g*(h[i]-h[i+1]))/(v_t[i]*v_t[i])
     time=v_t[i]/g*np.arccosh(np.exp(l))
     t.append(time)
print(np.array(t),"\n")

y=[]
v=[]

#the Velocity through each phase
for j in range(len(t)):
     velocity=v_t[j]*np.tanh((g*t[j]/v_t[j]))
     v.append(velocity)
#A check for the height, ensuring previous calculations are within line.
for n in range(len(t)):
     h=(v_t[n]*v_t[n])/g*np.log(np.cosh((g*t[n]/v_t[n])))
     y.append(h)
print(np.array(v),'\n\n',np.array(y),'\n')

rat=[]
#Ratio of given velocity to terminal velocity.
for k in range(len(v)):
     ratio = v[k]/v_t[k]
     rat.append(ratio)
print(np.array(rat),'\n')

for b in range(len(t)):
     print(format(rho[b], '.6f'), format(y[b], '.2f'), format(v_t[b], '.2f'), format(t[b], '.2f')
           , format(v[b], '.2f'), format(rat[b], '.2f'), sep=' ')

print('\n\n')

work=[]
delta_t=[]
#Measure of the change in energy and change in temperature.
for i in range(len(t)):
     w=0.5*C_d*A*rho[i]*v[i]*v[i]*y[i]
     work.append(w)
     dT=w/(m*c_p)
     delta_t.append(dT)
print("Work: ",np.array(work),'\n')
print("Change in Temperatur: ",np.array(delta_t),'\n')
print("Total change in temperature|assuming 100% heat absorbtion and 0% conduction:",np.sum(delta_t))