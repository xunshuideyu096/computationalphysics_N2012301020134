# Author  : LIN Chun (chun.lin@hotmail.com)
# Date    : 2016-06-13 16:37:56

from pylab import *
import pickle

#global variables
dt = 0
#fixed parameters
g = 9.8
l = 1

theta = []
omega = []
t = []
T = []
a = []  #index for zero theta
b = []  #time for around zero theta
amp = [] #steday amplitude
dic = {'frequency':[],'amplitude':[],'q':[]}

def initialize(dt_,theta_0):
    global dt, theta, dic, omega, t, T, a, b
    theta = [float(theta_0)]
    # theta = [float(raw_input('Input freeing angle:'))]
    omega = [0]
    t = [0]
    dic = {'frequency':[],'amplitude':[],'q':[]}
    dt = float(dt_)
    # dt = float(raw_input('Input time step:'))
    a = []
    b = []
    T = []
    return 0
def calculate(totaltime):
	global i, theta, omega, t, T, a, b, amp
	i = 0
	for i in range(totaltime):
		omega.append(omega[i] - (g/l)*sin(theta[i])*dt)
		theta.append(theta[i] + omega[i+1]*dt)
		t.append(t[i] + dt)
	for n in range(1,totaltime+1):  
		if theta[n-1]*theta[n]<= 0:
			a.append(n-1)
	for n in a:
		b.append((t[n+1]+t[n])/2)
	for n in range(len(b)-1):
		T.append((b[n+1]-b[n])*2)

theta0 = []
T0 = []
for n in range(1,int(50*pi)):
	theta_0 = n/100.0
	theta0.append(theta_0)
	initialize(0.001,theta_0)
	calculate(10000)
	T0.append(T[0])
plot(theta0, T0, color='black', linewidth=0, linestyle='-', marker='o', markerfacecolor="white", markersize='5', markeredgecolor="black", label="")
xlabel('Amplitude $\\theta(0)$ (radians)')
ylabel('Period T (s)')
text(0.2, 2.35, "Length = %g m, Time step = %g s" %(l,dt), fontsize=12, bbox={'facecolor':'white', 'alpha':1, 'pad':12})
plot([0.09,0.09], [2,2.03], color='black', linestyle=':', linewidth=2,)
annotate('$\\theta(0)=0.09\\approx 5^{\circ}$', xy=(0.09, 2.02), xytext=(0.2, 2.05), arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5))
savefig("A8_nonlinear.jpg")
show()







