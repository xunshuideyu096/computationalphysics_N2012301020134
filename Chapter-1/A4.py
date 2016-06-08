# Author  : LIN Chun (chun.lin@hotmail.com)
# Date    : 2016-06-05 12:59:29

from pylab import *
import pickle

v = []
v1 = [0]
t = [0]
t1 = [0]
g = 9.8
time = 10
n = 0
dt = 0
dt1 = 0.2
n1 = int(time/dt1)

def initialize():
    global n, dt
    v.append(float(raw_input('Input initial velocity v(0):')))
    dt = float(raw_input('Input time step:'))
    n = int(time / dt)
    return 0

def calculate():
    for i in range(1, n+1):
        v.append(v[i - 1] + g*dt)
        t.append(t[i - 1] + dt)
    for i in range(1, n1+1):
        v1.append(v1[i - 1] + g*dt1)
        t1.append(t1[i - 1] + dt1)
    return 0

def store():
    pickle_file = open("A4.pkl", "w")
    pickle.dump(t, pickle_file)
    pickle.dump(v, pickle_file)
    return 0

def read():
    pickle_file = open("A4.pkl", "r")
    t = pickle.load(pickle_file)
    v = pickle.load(pickle_file)
    print t
    print v

initialize()
calculate()
store()
read()

plot(t1, v1, color='black', linewidth=2.0, linestyle='-', marker='s', markerfacecolor="red", markeredgecolor="black", label="Time Step = 0.2 s")
xlabel('Time(s)')
ylabel('Velocity(m/s)')
margins(0.1,0.1)
plot(t, v, color='black', linewidth=2, linestyle='-', marker='o', markerfacecolor="white", markeredgecolor="black", label="Time Step = %g s" %(dt))

legend(loc="upper left")
# scatter(t, v)
savefig("A4.jpg", dpi=72)
show()


		
