# Author  : LIN Chun (chun.lin@hotmail.com)
# Date    : 2016-06-11 14:07:54

from pylab import *
import pickle

#global variables
theta = 0 #DEG
dt = 0
i = 0
r = 0
xl = 0
xl_1 = 0
#fixed parameters
g = 9.8
B2_m = 4.0*10**(-5)
w = 2000/60*2*pi
S_0_m = 4.1*10**(-4)

v = []
x = []
y = []
t = []
lib = {'x':[],'y':[],'x_hit':[]}
lib1 = dict()
lib2 = dict()

def initialize():
    global dt, theta, lib, v, x, y, t
    v = [float(30)]
    x = [0]
    y = [1]
    t = [0]
    lib = {'x':[],'y':[],'x_hit':[]}
    dt = float(0.001)
    # v.append(float(raw_input('Input initial speed v(0):')))
    # dt = float(raw_input('Input time step:'))
    theta = float(theta)#raw_input('Input firing angle (DEG):'))
    return 0

def calculate():
	global i, r, xl
	i = 0
	vx = [n*cos(theta/180*pi) for n in v]
	vy = [n*sin(theta/180*pi) for n in v]
	while True:
		x.append(x[i] + vx[i]*dt)
		y.append(y[i] + vy[i]*dt)
		ax = -B2_m*v[i]*vx[i]
		ay = S_0_m*w*vx[i] 
		#ay = S_0_m*w*vx[i] - B2_m*v[i]*vy[i]
		#ay = -B2_m*v[i]*vy[i]
		vx.append(vx[i] + ax*dt)
		vy.append(vy[i] + (-g+ay)*dt)
		i += 1
		v.append(sqrt(vx[i]**2 + vy[i]**2))
		if y[i]<=0:
			break
	r = -y[i-1]/y[i]
	xl = (x[i-1]+r*x[i])/(r+1)
	return 0

def store():
	global lib
	lib['x']=x
	lib['y']=y
	lib['x_hit']=[xl] #.append(xl)
	pickle_file = open("A7.pkl", "a") 
	pickle.dump(lib, pickle_file)
def read():
    global lib, lib1, lib2
    pickle_file = open("A7.pkl", "r")
    lib = pickle.load(pickle_file)
    lib1 = pickle.load(pickle_file)
    lib2 = pickle.load(pickle_file)

initialize()
# calculate()
# store()
read()
# print lib, lib1, lib2

x = lib['x']
y = lib['y']
x1 = lib1['x']
y1 = lib1['y']
x2 = lib2['x']
y2 = lib2['y']
xl = lib['x_hit']
xl_1 = lib1['x_hit']
plot(x, y, color='red', linewidth=2, linestyle=':', marker='o', markerfacecolor="white", markersize='0', markeredgecolor="black", label="Consider spin-denpendent force")
plot(x1, y1, color='black', linewidth=2, linestyle='--', marker='s', markerfacecolor="white", markersize='0', markeredgecolor="black", label="Consider y coordinate air drag force")
plot(x2, y2, color='black', linewidth=2, linestyle='-.', marker='^', markerfacecolor="white", markersize='0', markeredgecolor="black", label="Consider both spin-denpendent force\nand y coordinate air drag force")
xlabel('Distance (m)')
ylabel('Elevation (m)')
margins(0,0)
legend(loc="upper right", numpoints="2", fontsize=10.5)
text(1, 0.1, "The firing angle = %g $^{\circ}$\nThe initial speed = %g m/s\nThe time step = %g s\nAngular velocity = 2000 rpm\n\nHitting coordinate:\n(with spin):     %g m\n(without spin):%g m\nRelative error = 14 %%" %(theta,v[0],dt,15.77,13.56), fontsize=14, bbox={'facecolor':'white', 'alpha':1, 'pad':10})
# annotate('Sea level', xy=(6000, 0), xytext=(10000, 2000), arrowprops=dict(facecolor='black', shrink=0.05))

savefig("A7.jpg")
show()