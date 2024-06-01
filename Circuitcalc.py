import math as m
import matplotlib.pyplot as plt

Vab = 208
f = 60
L = 0.0025
R = 5
E = 20
n = 100

vo = []
vR = []
io = []

Vm = m.sqrt(2/3)*Vab
w = 2*m.pi*f

Z = m.sqrt(R**2+(w*L)**2)
THETA = m.atan(w*L/R)

#Corriente estable de carga:
I0 = (m.sqrt(2)*Vab/Z)*(m.sin(2*m.pi/3-THETA)-m.sin(m.pi/3)*m.exp(-R*m.pi/(L*3*w)))/(1-m.exp(-R*m.pi/(L*3*w)))-E/R

vo.append(3*m.sqrt(3)*Vm/m.pi)
vR.append(vo[0]-E)
io.append(vR[0]/R)

for i in range(n):
    i+=1
    z = m.sqrt(R**2+(6*i*w*L)**2)
    vo.append((-(-1)**i)*6*m.sqrt(3)*Vm/(m.pi*(36*(i**2)-1)))
    vR.append(vo[i])
    io.append(vR[i]/z)

#Valor medio del voltaje de salida:
Vas = vo[0]

#Valor medio de la corriente de salida:
Ia = io[0]

#Valor medio del voltaje en la resistencia:
Va = Ia*R

Vsrms = Vas**2
Irms = Ia**2

for i in range(n):
    Vsrms += (vo[i+1]**2)/2
    Irms += (io[i+1]**2)/2

#Voltaje rms de salida:
Vsrms = m.sqrt(Vsrms)

#Corriente rms de salida:
Irms = m.sqrt(Irms)

#Voltaje rms de la resistencia:
Vrms = Irms*R


Iad = Ia/3
Irmsd = Ia/m.sqrt(3)
Irmsl = m.sqrt(2/3)*Irms

Pabs = R*Irms**2
S = m.sqrt(3)*Vab*Irmsl

fp = Pabs/S

x = list(range(1000))
voy = []
vRy = []
ioy = []

for i in range(1000):
    aux1 = 0
    aux2 = 0
    aux3 = 0
    x[i] = x[i]/(f*750)
    for j in range(n+1):
        aux1 += vo[j]*m.cos(6*2*m.pi*j*i/750)
        aux3 += io[j]*m.cos(6*2*m.pi*j*i/750)
        aux2 += io[j]*m.cos(6*2*m.pi*j*i/750)*R
    voy.append(aux1)
    vRy.append(aux2)
    ioy.append(aux3)

sub1 = plt.subplot(2, 1, 1) 
sub2 = plt.subplot(2, 1, 2) 
sub1.plot(x, voy)
sub1.plot(x, vRy)
sub1.set_yticks(list(range(0, 361,60)))
sub2.plot(x, ioy)
sub2.set_yticks(list(range(0, 90,20)))

print("I0 = ",I0)
print("")
print("Vas = ",Vas)
print("Vsrms = ",Vsrms)
print("")
print("Ia = ",Ia)
print("Irms = ",Irms)
print("")
print("Va = ",Va)
print("Vrms = ",Vrms)
print("")
print("Iad = ", Iad)
print("Irmsd = ", Irmsd)
print("")
print("fp = ",fp)
