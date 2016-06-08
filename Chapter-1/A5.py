# Author  : LIN Chun (chun.lin@hotmail.com)
# Date    : 2016-06-07 17:29:20

from pylab import *
import pickle

v = []
t = [0]
a = 10
b = 1
total_time = 0
dt = 0
n = 0

def initialize():
    global n, dt, total_time
    v.append(float(raw_input('Input initial velocity v(0):')))
    dt = float(raw_input('Input time step:'))
    total_time = float(raw_input('Input Total time:'))
    n = int(total_time / dt)
    return 0

def calculate():
    for i in range(1, n+1):
        v.append(v[i-1] + (a-b*v[i-1])*dt)
        t.append(t[i-1] + dt)
    return 0

def store():
    pickle_file = open("A5.pkl", "w")
    pickle.dump(t, pickle_file)
    pickle.dump(v, pickle_file)
    return 0

def read():
    pickle_file = open("A5.pkl", "r")
    t = pickle.load(pickle_file)
    v = pickle.load(pickle_file)
    print t
    print v

initialize()
calculate()
store()
read()

plot(t, v, color='black', linewidth=2, linestyle='-', marker='o', markerfacecolor="white", markeredgecolor="black", label="Time Step = %g s\nInitial velocity = %g m/s" %(dt,v[0]))
xlabel('Time (s)')
ylabel('Velocity (m/s)')
margins(0,0.05)
# legend(loc="upper right", bbox_to_anchor=(0.98, 0.9), numpoints="0")
plot([-0.5, total_time], [10, 10], linestyle=":", color="black", linewidth=2)
text(5.5, 8, "Time Step = %g s\nInitial velocity = %g m/s" %(dt,v[0]), fontsize=15)
text(2, 11, "Time dependence of velocity", fontsize=15)
savefig("A5.jpg")
show()


		