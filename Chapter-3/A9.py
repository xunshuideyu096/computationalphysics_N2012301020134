# Author  : LIN Chun (chun.lin@hotmail.com)
# Date    : 2016-06-15 19:35:55

from pylab import *
import pickle

#global variables
dt = 0
l = 0
F_D = 0
Omega_D = 0
q = 0
theta = []
omega = []
t = []
#fixed parameters
g = 9.8

def initialize(dt_,l_,F_D_,Omega_D_,q_,theta0):
    global dt, l, F_D, Omega_D, q, theta, omega, t
    theta = [float(theta0)]
    omega = [0]
    t = [0]
    dt = float(dt_)
    F_D = F_D_
    l = l_
    Omega_D = Omega_D_
    q = q_
    return 0
def calculate(totaltime,s1,s2,phase):
	global theta, omega, t
	for i in range(totaltime):
		omega.append(omega[i] + (F_D*sin(Omega_D*t[i]) - (g/l)*sin(theta[i]) - q*omega[i])*dt)
		theta.append(theta[i] + omega[i+1]*dt)
		t.append(t[i] + dt)
		if s1==1 and theta[i+1]>pi:
			theta[i+1] -= 2*pi
		if s1==1 and theta[i+1]<-pi:
			theta[i+1] += 2*pi
	if s2==1:  #Poincare section
		ti = []
		for n in range(int((totaltime+1)*dt*Omega_D/2/pi)):
			for i in range(len(t)):
				if abs(t[i]-(2*n*pi+phase)/Omega_D)<=dt/2:
					ti.append(i)
		thetai = []
		omegai = []
		for i in ti:
			thetai.append(theta[i])
			omegai.append(omega[i])
		theta = thetai
		omega = omegai



# #Chaotic behavior
# initialize(0.01,9.8,1.2,2/3.0,0.5,0.2)
# calculate(9999,0)
# plot(t, theta, color='black', linewidth=2, linestyle='-', marker='o', markerfacecolor="white", markersize='0', markeredgecolor="black", label="")
# xlabel('Time (s)')
# ylabel('${\\theta}$ (radians)')
# text(60, 0.15, "$F_D$ = %g\n$l$ = %g m, $\Omega_D$= %s\nq = %g,$\Delta t$ = %g s\n$\\theta(0)=$ %g, $\omega(0)=$ 0" %(F_D,l,'2/3',q,dt,theta[0]), fontsize=12, bbox={'facecolor':'white', 'alpha':1, 'pad':12})
# savefig("A9_F=%g.jpg" %(F_D))
# show()

#omega vs theta Poincare
initialize(0.04,9.8,1.2,2/3.0,0.5,0.2)
calculate(99999,1,1,pi/4)
plot(theta, omega, color='black', linewidth=0, linestyle='-', marker='o', markerfacecolor="white", markersize='1', markeredgecolor="black", label="")
xlabel('${\\theta}$ (radians)')
ylabel('$\Omega$ (radians/s)')
text(1.5, 0.7, "$F_D$ = %g\n$t\\approx (2n\pi+\pi/4)/\Omega_D$" %(F_D), fontsize=12, bbox={'facecolor':'white', 'alpha':1, 'pad':12})
savefig("A9_Poincare_phase=pi_4.jpg")
show()
