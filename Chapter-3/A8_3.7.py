# Author  : LIN Chun (chun.lin@hotmail.com)
# Date    : 2016-06-13 16:37:56

from pylab import *
import pickle

#global variables
dt = 0
i = 0
#fixed parameters
g = 9.8

l = 0
F_D = 0
Omega_D = 0
q = 0

theta = []
omega = []
Omega = []
q_list = []
t = []
T = []
a = []  #index for zero theta
b = []  #time for around zero theta
amp = [] #steday amplitude
dic = {'frequency':[],'amplitude':[],'q':[]}

def initialize(F_D_,Omega_D_,q_,dt_,l_):
    global dt, theta, dic, omega, t, T, a, b, F_D, Omega_D, q, l, amp
    theta = [float(0.2)]
    # theta = [float(raw_input('Input freeing angle:'))]
    omega = [0]
    t = [0]
    dic = {'frequency':[],'amplitude':[],'q':[]}
    dt = float(dt_)
    # dt = float(raw_input('Input time step:'))
    a = []
    b = []
    T = []
    F_D = F_D_
    l = l_
    # Omega_D = Omega_D_
    Omega_D = sqrt(g/l) #Resonance
    q = q_
    q_list = []
    return 0
def calculate(totaltime):
	global i, theta, omega, t, T, a, b, amp
	i = 0
	for i in range(totaltime):
		omega.append(omega[i] + (F_D*sin(Omega_D*t[i]) - (g/l)*theta[i] - q*omega[i])*dt)
		theta.append(theta[i] + omega[i+1]*dt)
		t.append(t[i] + dt)
	for n in range(1,totaltime+1):  
		if theta[n-1]*theta[n]<= 0:
			a.append(n-1)
	for n in a:
		b.append((t[n+1]+t[n])/2)
	for n in range(len(b)-1):
		T.append((b[n+1]-b[n])*2)
		if b[n] > 20:
			amp.append(max(theta[int(n/dt):]))
			break
def store():
	global dic
	dic['frequency']=Omega
	dic['amplitude']=amp
	dic['q']=q_list
	pickle_file = open("A8_frequency_dependence.pkl", "w") 
	pickle.dump(dic, pickle_file)
def read():
    global dic
    pickle_file = open("A8_frequency_dependence.pkl", "r")
    dic = pickle.load(pickle_file)

amp = []
initialize(0.2,2.0,0,0.01,1)
calculate(10000)
# print amp
plot(t, theta, color='black', linewidth=2, linestyle='-', marker='o', markerfacecolor="white", markersize='0', markeredgecolor="black", label="")
xlabel('Time (s)')
ylabel('${\\theta}$ (radians)')
text(25, 0, "Length = %g m, $\Omega_D=\Omega$ = %g, $F_D$ = %g, q = %g\nTime step = %g s, T(steady) $\\approx$ %g s" %(l,Omega_D,F_D,q,dt,T[-1]), fontsize=12, bbox={'facecolor':'white', 'alpha':1, 'pad':12})
ylabel('Resonance amplitude')
# savefig("A.jpg")
show()


#frequency dependence
# amp = []
# for n in range(10,101):
# 	initialize(0.2,2.0,0.2,0.01,1)
# 	l = float(n/10.0)
# 	Omega_D = sqrt(g/l)
# 	Omega.append(Omega_D)
# 	calculate(10000)
# plot(Omega, amp, color='black', linewidth=2, linestyle='--', marker='s', markerfacecolor="white", markersize='0', markeredgecolor="black", label="")
# text(2.5, 1, "$F_D$ = %g, q = %g" %(F_D,q), fontsize=12, bbox={'facecolor':'white', 'alpha':1, 'pad':12})
# xlabel('Driving frequency $\Omega_D $')
# ylabel('Resonance amplitude')
# savefig("A8_damp_force_resonance_frequency_dependence.jpg")
# show()


# q dependence
# amp = []
# for n in range(1,60):
# 	initialize(0.2,2.0,0.2,0.01,1)
# 	q = float(n/100.0)
# 	q_list.append(q)
# 	calculate(10000)
# plot(q_list, amp, color='black', linewidth=2, linestyle='--', marker='s', markerfacecolor="white", markersize='0', markeredgecolor="black", label="")
# xlabel('Friction parameter q')
# text(0.3, 40, "$\Omega_D=\Omega$ = %g, $F_D$ = %g" %(Omega_D,F_D), fontsize=12,bbox={'facecolor':'white', 'alpha':1, 'pad':12})
# ylabel('Resonance amplitude')
# savefig("A8_damp_force_resonance_q_dependence.jpg")
# show()









