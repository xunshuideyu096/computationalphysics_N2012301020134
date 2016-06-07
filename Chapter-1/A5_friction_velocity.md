**EXERCISE: 1.3** 

[Source Code: A4_freely_falling_velocity.py](https://github.com/ZQTXLC/computationalphysics_N2012301020134/blob/master/Chapter-1/A4_freely_falling_velocity.py)

###<p align="center">An application of Euler method on the velocity with a altering frictional force</p>
#####<p align="center">Chun lin</p>
#####<p align="center">Student ID: 2012301020134, Major: Physics Base Class</p>

**Abstract:**
Under the frame work of Euler method, this paper calculates the velocity of an object under a linearly increasing frictional force with a rising velocity.

<br /> 
**Introduction:**
<br>
&emsp;&emsp;With the Taylor expansion of a function __*f*(*v*)__, *Euler method* assumes *__Δt__* is very small but nonzero then the terms that involve second and higher powers of *__Δt__* can be ignored, and gives out the approximation form of __*f*(*v*)__:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$f(x+\Delta x) \approx f(x)+\frac{df(x)}{dx}\Delta x \qquad\qquad\qquad\qquad\qquad\qquad\qquad(5.1)$$)

Considering the case that a moving object with a nonzero frictional force __*f*(*v*)__, here, as we can image, this force is velocity dependent, that is __*f*(*v*)__ increase as the object moves faster. A typical example is a parachutist, who would be dragged when he open a parachute which produces an air resistance, and then the parachutist lands on the ground slowly and safely. The function form of air drag to moving velocity is quite complex and factors like the shape of the object, air temperature, air humidity, the velocity of air itself, even the atmosphere pressure have influences on it. Here, for the sake of simplicity, assuming the frictional fore increases linearly with increasing velocity, namely, the function form of object velocity when there is an applied driving force obeys:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\frac{dv(t)}{dt}=a-bv\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad(5.2)$$)

where both *a* and *b* are constants. Obviously, *a* comes from the applied driving force, like the gravity, while *b* arises from frictional force. The minus sign represents the fore direction is opposed to the motion direction. 

&emsp;&emsp;In this paper, a program using Euler method will be employed to compute the solution __*v*(*t*)__ to equation (5.2). Take convenient choice of parameters of *a* = 10 and *b* = 1 (both SI units), this program has performed different time steps and the results are consistent with exact solution which predicts a constant value of *__v__* at long time.

<br /> 
**Method:**
<br>
&emsp;&emsp;Apply Euler method, the velocity as a function of time could be easily obtained:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$v(t+\Delta t)\approx v(t)+(a-bv(t))\Delta t\qquad\qquad\qquad\qquad\qquad\qquad\qquad(5.3)$$)







&ensp;The pseudocode for applying Euler method to this problem consists of four basic tasks:

* Declare necessary variables and arrays.
* Initialize variables.
* Do the calculation according to equation (5.3).
* Store (Read, if necessary) the results.

To begin with, I declare the required variables, for convenience, the initial values of velocity and time have been assigned directly here.

    v = [0]
    t = [0]
    g = 9.8
    time = 10
    n = 0
    dt = 0

To initialize the time step, here defined a function: (here *n* is the calculation time which must be an integer. 
)

    def initialize():
        global n, dt
        dt = float(raw_input('Input time step:'))
        n = int(time / dt)
        return 0

Then is the core program which performs the calculation, which will repeat *n* times, and the new results will store in the original list using "append" method.

    def calculate():
        for i in range(1, n+1):
            v.append(v[i - 1] + g*dt)
            t.append(t[i - 1] + dt)
        return 0

To store or read the result, pickle module is a good option.

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

Using pylab module, the figure below has showed the results of two different time steps, as the figure has indicated, for this simple case, the result given by Euler method is exact solution and is independent of time steps.

<p align="center">![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-1/A4.jpg)</p>

<br /> 
**Conclusion:**
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For this simple case, i.e., the time dependence of velocity with a constant acceleration, the Euler method gives the exact solution and the solution is independent of time steps.

<br /> 
