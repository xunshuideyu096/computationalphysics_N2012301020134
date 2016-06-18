# Author  : LIN Chun (chun.lin@hotmail.com)
# Date    : 2016-06-17 21:04:47

from pylab import *
import pickle

#### Be very careful to the units #####

#global variables
dt = 0
r = {'m1':[],'m2':[]}
x = {'m1':[],'m2':[]}
y = {'m1':[],'m2':[]}
vx = {'m1':[],'m2':[]}
vy = {'m1':[],'m2':[]}
t = []
r0 = 1
m1 = 0
m2 = 0
#fixed parameters
# G = 6.674*10**(-11)
G = 1

def initialize(x_0,y_0,vx_0,vy_0,dt_,m1_,m2_,s1):
	global dt, r, x, y, vx, vy, t, r0, m1, m2
	if s1 == 0:
	    x['m1'] = [float(x_0[0])]
	    y['m1'] = [float(0)]
	    vx['m1'] = [float(0)]
	    vy['m1'] = [float(vy_0)]
	    t = [0]
	    dt = float(dt_)
	    r['m1'] = [float(sqrt(x['m1'][0]**2+y['m1'][0]**2))]
    # if s1 == 1:  # considering the mass of sun
	if s1 == 1:
		m1 = float(m1_)
		m2 = float(m2_)
		r0 = float(abs(x_0[0]) + abs(x_0[1]))
		x['m1'] = [float(x_0[0])]
		y['m1'] = [float(0)]
		vx['m1'] = [float(0)]
		# vy['m1'] = [float(sqrt(G/r0*m2**2/(m1+m2)))]
		vy['m1'] = [float(2*pi/sqrt(x_0[0]))]
		r['m1'] = [float(sqrt(x['m1'][0]**2+y['m1'][0]**2))]
		x['m2'] = [float(x_0[1])]
		y['m2'] = [float(0)]
		vx['m2'] = [float(0)]
		# vy['m2'] = [float(-sqrt(G/r0*m1**2/(m1+m2)))]
		vy['m2'] = [float(pi/sqrt(x_0[0]))]
		r['m2'] = [float(sqrt(x['m2'][0]**2+y['m2'][0]**2))]
		t = [0]
		dt = float(dt_)

def calculate(totaltime,s1):
	global x, y, vx, vy, r, t
	if s1 == 0:  # AU unit
		for i in range(totaltime-1):
			vx['m1'].append(vx['m1'][i] - 4*pi**2*x['m1'][i]/r['m1'][i]**3*dt)
			vy['m1'].append(vy['m1'][i] - 4*pi**2*y['m1'][i]/r['m1'][i]**3*dt)
			x['m1'].append(x['m1'][i] + vx['m1'][i+1]*dt)
			y['m1'].append(y['m1'][i] + vy['m1'][i+1]*dt)
			t.append(t[i] + dt)
			r['m1'].append(sqrt(x['m1'][i]**2+y['m1'][i]**2))
	if s1 == 1:
		for i in range(totaltime-1):
			vx['m1'].append(vx['m1'][i] - 4*pi**2*x['m1'][i]/r['m1'][i]**3*dt)
			vy['m1'].append(vy['m1'][i] - 4*pi**2*y['m1'][i]/r['m1'][i]**3*dt)
			x['m1'].append(x['m1'][i] + vx['m1'][i+1]*dt)
			y['m1'].append(y['m1'][i] + vy['m1'][i+1]*dt)
			r['m1'].append(sqrt(x['m1'][i]**2+y['m1'][i]**2))
			# vx['m2'].append(vx['m2'][i] - 4*pi**2*x['m2'][i]/r['m2'][i]**3*dt)
			# vy['m2'].append(vy['m2'][i] - 4*pi**2*y['m2'][i]/r['m2'][i]**3*dt)
			x['m2'].append(x['m1'][i+1]*(-0.5))
			y['m2'].append(y['m1'][i+1]*(-0.5))
			# x['m2'].append(x['m2'][i] + vx['m2'][i+1]*dt)
			# y['m2'].append(y['m2'][i] + vy['m2'][i+1]*dt)
			# r['m2'].append(sqrt(x['m2'][i]**2+y['m2'][i]**2))
			t.append(t[i] + dt)

s2 = 3   # choose which program to run

if s2 == 2:
	initialize([2,-1],0,0,0,0.002,100,100,1)
	calculate(1500,1)
	figure(figsize=(6.0,6.0), dpi=100)
	plot(x['m1'], y['m1'], color='black', linewidth=0, linestyle='-', marker='o', markerfacecolor="white", markersize='6', markeredgecolor="black", label="")
	plot(x['m2'], y['m2'], color='black', linewidth=0, linestyle='-', marker='o', markerfacecolor="black", markersize='6', markeredgecolor="black", label="")
	xlabel('x (AU)')
	ylabel('y (AU)')
	xlim(-2.0,2.0)
	ylim(-2.0,2.0)
	savefig("A11_xy_m1m2.jpg")
	show()


if s2 == 3:
	initialize([2,-1],0,0,0,0.002,100,100,1)
	calculate(1500,1)
	for i in range(1,284):
		n = i*5-1
		figure(figsize=(6.0,6.0), dpi=100)
		plot(x['m1'][n], y['m1'][n], color='black', linewidth=0, linestyle='-', marker='o', markerfacecolor="white", markersize='6', markeredgecolor="black", label="")
		plot(x['m2'][n], y['m2'][n], color='black', linewidth=0, linestyle='-', marker='o', markerfacecolor="black", markersize='6', markeredgecolor="black", label="")
		xlabel('x (AU)')
		ylabel('y (AU)')
		xlim(-2.0,2.0)
		ylim(-2.0,2.0)
		savefig("A11_xy_m1m2_%.4d.jpg" %(n))
		close()
# print x,y,vx,vy,r,r0,vy['m1'][0]



# x vs y
if s2 == 0:
	initialize([2],0,0,sqrt(2)*pi,0.002,0,0,0)
	calculate(4800,0)
	figure(figsize=(6.0,6.0), dpi=100)
	plot(x['m1'], y['m1'], color='black', linewidth=0, linestyle='-', marker='.', markerfacecolor="white", markersize='2', markeredgecolor="black", label="")
	xlabel('x (AU)')
	ylabel('y (AU)')
	xlim(-2.0,2.0)
	ylim(-2.0,2.0)
	# plot([-1.0,-1.0],[1.0,-1.0])
	# plot([-1.0,1.0],[-1.0,-1.0])
	# plot([-1.0,1.0],[1.0,1.0])
	# plot([1.0,1.0],[1.0,-1.0])
	savefig("A11_xy1.jpg")
	# close()
	show()

# x vs y.gif
if s2 == 1:
	initialize([1],0,0,2*pi,0.002,0,0,0)
	calculate(500,0)
	for i in range(1,101):
		n = i*5-1
		figure(figsize=(6.0,6.0), dpi=100)
		plot(x[n], y[n], color='black', linewidth=0, linestyle='-', marker='o', markerfacecolor="white", markersize='6', markeredgecolor="black", label="The earth")
		plot(0, 0, color='black', linewidth=0, linestyle='-', marker='o', markerfacecolor="black", markersize='10', markeredgecolor="black", label='The sun')
		legend(loc=(0.75,1.01), numpoints='1', fontsize=10)
		xlabel('x (AU)')
		ylabel('y (AU)')
		xlim(-1.0,1.0)
		ylim(-1.0,1.0)
		savefig("A11_xy_%.3d.jpg" %(n))
		close()
	# show()

