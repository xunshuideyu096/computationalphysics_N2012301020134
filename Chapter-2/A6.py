# Author  : LIN Chun (chun.lin@hotmail.com)
# Date    : 2016-06-09 15:21:50

from pylab import *
import pickle

#global variables
theta = 0 #DEG
dt = 0
i = 0
r = 0
xl = 0
#fixed parameters
g = 9.8
B2_m = 4.0*10**(-5)
y0 = 1.0*10**4

v = []
x = [0]
y = [0]
t = [0]
ym = []
x1 = []
x2 = []
x3 = []
y1 = []
y2 = []
y3 = []

def initialize():
    global dt, theta
    v.append(float(700))
    dt = float(0.5)
    # v.append(float(raw_input('Input initial speed v(0):')))
    # dt = float(raw_input('Input time step:'))
    theta = float(raw_input('Input firing angle (DEG):'))
    return 0

def calculate():
	global i, r, xl
	vx = [n*cos(theta/180*pi) for n in v]
	vy = [n*sin(theta/180*pi) for n in v]
	while True:
		x.append(x[i] + vx[i]*dt)
		y.append(y[i] + vy[i]*dt)
		e = exp(-y[i]/y0)
		ax = B2_m*v[i]*vx[i]*e
		ay = B2_m*v[i]*vy[i]*e
		vx.append(vx[i] - ax*dt)
		vy.append(vy[i] - (g+ay)*dt)
		i += 1
		v.append(sqrt(vx[i]**2 + vy[i]**2))
		if y[i]<=0:
			break
	r = -y[i-1]/y[i]
	xl = (x[i-1]+r*x[i])/(r+1)
	return 0

def store():
	pickle_file = open("A6_60.pkl", "w")
	pickle.dump(x, pickle_file)
	pickle.dump(y, pickle_file)

def read():
    global x1, x2, x3, y1, y2, y3
    pickle_file1 = open("A6_30.pkl", "r")
    x1 = pickle.load(pickle_file1)
    y1 = pickle.load(pickle_file1)
	
    pickle_file2 = open("A6_45.pkl", "r")
    x2 = pickle.load(pickle_file2)
    y2 = pickle.load(pickle_file2)
	
    pickle_file3 = open("A6_60.pkl", "r")
    x3 = pickle.load(pickle_file3)
    y3 = pickle.load(pickle_file3)
    

initialize()
calculate()
store()
# read()

# print ym

# plot(x1, y1, color='black', linewidth=2, linestyle='-', marker='o', markerfacecolor="white", markeredgecolor="black", label="Firing angle = 30 ($^{\circ}$)")
# plot(x2, y2, color='black', linewidth=2, linestyle='-', marker='s', markerfacecolor="white", markeredgecolor="black", label="Firing angle = 45 ($^{\circ}$)")
# plot(x3, y3, color='black', linewidth=2, linestyle='-', marker='^', markerfacecolor="white", markeredgecolor="black", label="Firing angle = 60 ($^{\circ}$)")
# xlabel('Distance (m)')
# ylabel('Elevation (m)')
# margins(0,0)
# legend(loc="upper right", bbox_to_anchor=(0.98, 0.98), numpoints="2")
# plot([0, xl], [0, 0], linestyle=":", color="black", linewidth=2)
# # text(xl/3, max(y)/4, "The firing angle = %g $^{\circ}$\nInitial speed = %g m/s\nThe time step = %g s\n\nLanding position = %g m\nMaximum altitude = %g m" %(theta,v[0],dt,xl,max(y)), fontsize=14)
# savefig("A6.jpg")
# show()

		