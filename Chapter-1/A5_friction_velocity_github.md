**EXERCISE: 1.3** 

[Source Code: A5.py](https://github.com/ZQTXLC/computationalphysics_N2012301020134/blob/master/Chapter-1/A5.py)

###<p align="center">An application of Euler method on the velocity with a altering frictional force</p>
#####<p align="center">Chun lin</p>
#####<p align="center">Student ID: 2012301020134, Major: Physics Base Class</p>

**Abstract:**
Under the frame work of Euler method, this paper calculates the velocity of an object under a linearly increasing frictional force. It turns out the velocity will get close to a terminal velocity infinitely as long as passing time is larger enough.

<br /> 
**Introduction:**
<br>
&emsp;&emsp;With the Taylor expansion of a function __*f*(*x*)__, *Euler method* assumes *__Δx__* is very small but nonzero then the terms that involve second and higher powers of *__Δx__* can be ignored, and gives out the approximation form of __*f*(*x*)__:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$f(x+\\Delta x) \\approx f(x)+\\frac{df(x)}{dx}\\Delta x \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad(5.1)$$)

Considering the case that a moving object with a nonzero frictional force __*f*(*v*)__, here, as we can image, this force is velocity dependent, that is __*f*(*v*)__ increase as the object moves faster. A typical example is a parachutist, who would be dragged when he open a parachute which produces an air resistance, and then the parachutist lands on the ground slowly and safely. The function form of air drag to moving velocity is quite complex and factors like the shape of the object, air temperature, air humidity, the velocity of air itself, even the atmosphere pressure have influences on it. Here, for the sake of simplicity, assuming the frictional fore increases linearly with increasing velocity, namely, the function form of object velocity when there is an applied driving force obeys:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\frac{dv(t)}{dt}=a-bv\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad(5.2)$$)

where both *a* and *b* are constants. Obviously, *a* comes from the applied driving force, like the gravity, while *b* arises from frictional force. The minus sign represents the fore direction is opposed to the motion direction. 

&emsp;&emsp;In this paper, a program using Euler method will be employed to compute the solution __*v*(*t*)__ to equation (5.2). Take convenient choice of parameters of *a* = 10 and *b* = 1 (both SI units), this program has performed different time steps and the results are consistent with exact solution which predicts a constant value of *__v__* at long time.

<br /> 
**Method:**
<br>
It's not so difficult to solve equation (5.2), first divide both side of it by ![](http://latex.codecogs.com/gif.latex?$$a-bv$$), that is ![](http://latex.codecogs.com/gif.latex?$$10-v$$), taking the parameter values indicated above. Definitely, this operation has assumed *v* to be smaller than 10 m/s, and then multiply both side of it with *dt*, the result is:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;![](http://latex.codecogs.com/gif.latex?$$\\frac{dv(t)}{10-v}=dt\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\ \\ (5.3)$$)

By integrating both side of equation (5.3) with its initial values, we have:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$v(t)=10(1-e^{-t})\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\quad\\ (5.4)$$)

Equation (5.4) indicates that the velocity increases very rapidly as time moving ahead then slows down due to exponentially decreasing time factor. Mathematically speaking, the velocity can not reach the theoretically terminal velocity, i.e., 10 m/s, until time approaches infinity. *However, from the point of view of reality, the difference between theoretically terminal velocity and actual velocity is so tiny that we can take the actual velocity as 10 m/s, as soon as time exceeds dozens of units.*

&emsp;&emsp;Apply Euler method, the velocity as a function of time could be easily obtained:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$v(t+\\Delta t)\\approx v(t)+(a-bv(t))\\Delta t\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad(5.5)$$)

The pseudocode for applying Euler method to this problem consists of four basic tasks:

* Declare necessary variables and arrays.
* Initialize variables.
* Do the calculation according to equation (5.3).
* Store (Read, if necessary) the results.

To begin with, program declares the required variables, for convenience, the initial values of *a, b* and time have been assigned directly here.

    v = []
    t = [0]
    a = 10
    b = 1
    total_time = 0
    dt = 0
    n = 0

To initialize the time step, total time and velocity, here defined a function: (*n* is the calculation time which must be an integer. 
)

    def initialize():
        global n, dt, total_time
        v.append(float(raw_input('Input initial velocity v(0):')))
        dt = float(raw_input('Input time step:'))
        total_time = float(raw_input('Input Total time:'))
        n = int(total_time / dt)
        return 0

The next is the core program that performs the calculation, and it will repeat *n* times. For each time, the new results will store in the original list using "append" method.

    def calculate():
        for i in range(1, n+1):
            v.append(v[i-1] + (a-b*v[i-1])*dt)
            t.append(t[i-1] + dt)
        return 0

To store or read the results, here employed the pickle *module*. With a *store* function, the program first opens or creates a new file with write mode and then writes *t* and *v* list into this file using *dump* method. With *read* function, the program opens the designated file with read-only mode and restore *t* and *v* list.

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

Using *pylab* module, as the code and figure shown below, the program plots time dependencet of velocity with different time steps and total time. Also, it gives out the difference between the theoretically terminal velocity and the actual final velocity, which *is completely negligible (the error is ![](http://latex.codecogs.com/gif.latex?$$3\\times10^{-5}$$)) as total time exceeds 10 seconds, when the initial velocity is 0 m/s and time step is 0.1 s.*

    plot(t, v, color='black', linewidth=2, linestyle='-', marker='o', markerfacecolor="white", markeredgecolor="black", label="Time Step = %g s\\nInitial velocity = %g m/s" %(dt,v[0]))
    xlabel('Time (s)')
    ylabel('Velocity (m/s)')
    margins(0,0.05)
    plot([-0.5, total_time], [10, 10], linestyle=":", color="black", linewidth=2)
    text(5.5, 8, "Time Step = %g s\\nInitial velocity = %g m/s" %(dt,v[0]), fontsize=15)
    savefig("A5.jpg")
    show()

&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-1/A5.jpg)

<br /> 
**Conclusion:**
<br>
&emsp;&emsp;For the case of the velocity of an object under a linearly increasing frictional force, Euler method gives a result that *the difference between the theoretically terminal velocity and the actual final velocity is completely negligible (the error is ![](http://latex.codecogs.com/gif.latex?$$3\\times10^{-5}$$)) as total time exceeds 10 seconds, when the initial velocity is 0 m/s and time step is 0.1 s, which is consistent with theoretical estimation.*

<br /> 
