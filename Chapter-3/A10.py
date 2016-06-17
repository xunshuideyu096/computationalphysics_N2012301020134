# Author  : LIN Chun (chun.lin@hotmail.com)
# Date    : 2016-06-16 17:40:47

from pylab import *
import pickle

#global variables
dt = 0
r = 0
x = []
y = []
z = []
t = []
#fixed parameters
sigma = 10
b = 8/3.0

def initialize(x_0,y_0,z_0,dt_,r_):
    global dt, r, x, y, z, t
    x = [float(x_0)]
    y = [float(y_0)]
    z = [float(z_0)]
    t = [0]
    dt = float(dt_)
    r = r_
    return 0
def calculate(totaltime,s2,phase):
	global x, y, z, t
	for i in range(totaltime-1):
		x.append(x[i] + sigma*(y[i]-x[i])*dt)
		y.append(y[i] + (-x[i]*z[i]+r*x[i]-y[i])*dt)
		z.append(z[i] + (x[i]*y[i]-b*z[i])*dt)
		t.append(t[i] + dt)
	if s2==1:  #Poincare section
		ti = []
		for i in range(1,len(x)):
			if i>30/dt and x[i-1]*x[i]<=0:
				ti.append(i-1)
				ti.append(i)
		zi = []
		yi = []
		for i in ti:
			zi.append(z[i])
			yi.append(y[i])
		z = zi
		y = yi

# z vs t
# for ii in [5,10,25]:
# 	initialize(1,0,0,0.0001,ii)
# 	calculate(500000,0,0)
# 	plot(t, z, color='black', linewidth=0, linestyle='-', marker='.', markerfacecolor="white", markersize='0.1', markeredgecolor="black", label="")
# xlabel('Time (s)')
# ylabel('z')
# text(10, 6, "r = %g" %(5), fontsize=12)
# text(10, 12, "r = %g" %(10), fontsize=12)
# text(10, 32, "r = %g" %(25), fontsize=12)
# savefig("A10_zt.jpg", dpi=500)
# show()

# z vs x
# initialize(1,0,0,0.0001,25)
# calculate(500000,0,0)
# plot(x, z, color='black', linewidth=0, linestyle='-', marker='.', markerfacecolor="white", markersize='1', markeredgecolor="black", label="")
# xlabel('x')
# ylabel('z')
# text(5, 40, "r = %g" %(25), fontsize=12)
# savefig("A10_zx.jpg")
# show()

# z vs y 
for ii in range(0,120):
	initialize(1,0,0,0.0001,ii)
	calculate(5000000,1,0)
	plot(y, z, color='black', linewidth=0, linestyle='-', marker='.', markerfacecolor="white", markersize='2', markeredgecolor="black", label="")
	xlabel('y  (r = %g)' %(r))
	ylabel('z')
	margins(0.2,0.2)
	# text(max(y)*0.75, max(z)*1.02, "r = %g" %(r), fontsize=12)
	savefig("A10_yz_x=0_r=%g.jpg" %(r))
	close()

# r < 160 period-doubling
# for ii in range(150,160)
# initialize(1,0,0,0.0001,ii)
# calculate(300000,0,0)
# plot(t, z, color='black', linewidth=0, linestyle='-', marker='.', markerfacecolor="white", markersize='0.1', markeredgecolor="black", label="")
# xlabel('Time (s)')
# ylabel('z')
# # margins(0.2,0.2)
# text(5, 40, "r = %g" %(r), fontsize=12)
# savefig("A10_zt_r=%g.jpg" %(r), dpi=200)
# show()
