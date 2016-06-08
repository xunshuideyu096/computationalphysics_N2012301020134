**EXERCISE: 1.1** 

[Source Code: A4.py](https://github.com/ZQTXLC/computationalphysics_N2012301020134/blob/master/Chapter-1/A4.py)

###<p align="center">An application of Euler method on a simple first-order differential equation</p>
#####<p align="center">Chun lin</p>
#####<p align="center">Student ID: 2012301020134, Major: Physics Base Class</p>

**Abstract:**
Ordinary differential equations are highly common in many scientific problems, using an example of solving a simple first-order differential equation concerning a constant acceleration, this paper has showed the basic idea of Euler method.

<br /> 
**Introduction:**
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Considering a radioactive decay, a typical example is the nuclear isotope 
![](http://latex.codecogs.com/gif.latex?$$^{235}U$$), which has a small probability for decaying into two nuclei. Assuming ![](http://latex.codecogs.com/gif.latex?$$N_{U}(t)$$) is the number of uranium nuclei that are present in a sample at time ![](http://latex.codecogs.com/gif.latex?$$t$$), the behavior is governed by the differential equation: 

![](http://latex.codecogs.com/gif.latex?$$\\frac{dN_U(t)}{dt}=-\\frac{N_U}{\\tau}\\qquad(a)$$)

where ![](http://latex.codecogs.com/gif.latex?$$\\tau$$) is the time constant for this decay or so call the mean lifetime of a nucleus. The result through applying integral to equation (a) is:

![](http://latex.codecogs.com/gif.latex?$$N_U(t)=N_U(0)e^{-t/\\tau}\\qquad(b)$$)

In accordance to Taylor expansion, and assuming ![](http://latex.codecogs.com/gif.latex?$$\\Delta t$$) is very small but nonzero then the terms that involve second and higher powers of ![](http://latex.codecogs.com/gif.latex?$$\\Delta t$$) can be ignored, we can obtain the approximation form of *Euler method*:

![](http://latex.codecogs.com/gif.latex?$$N_U(t+\\Delta t) \\approx N_U(t)+\\frac{dN_U(t)}{dt}\\Delta t \\qquad(c)$$)

substituted by equation(a), we have:

![](http://latex.codecogs.com/gif.latex?$$N_U(t+\\Delta t) \\approx N_U(t)-\\frac{N_U(t)}{\\tau}\\Delta t \\qquad(d)$$)

This approximation forms the basis for a numerical solution of the radioactive decay problem. For a particular, we know the value of ![](http://latex.codecogs.com/gif.latex?$$N_U(t)$$) at some time *t*, usually the initial value of the function, we can then apply equation (d) to estimate its value at *t = Δt, 2Δt, 3Δt*, etc., and therefore lead to an approximation solution ![](http://latex.codecogs.com/gif.latex?$$N_U(n\\Delat t) $$) at times ![](http://latex.codecogs.com/gif.latex?$$n\\Delta t$$) where ![](http://latex.codecogs.com/gif.latex?$$n$$) is a large integral.
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For a much simpler case,  the velocity of a freely falling object from a rest state near Earth's surface is:

![](http://latex.codecogs.com/gif.latex?$$\\frac{dv(t)}{dt}=-g\\qquad(e)$$)

where *v* is the velocity and *g* is gravitational acceleration. In this paper, a program using Euler method will be employed to compute the solution *v*(*t*) to equation (e), and assume the initial velocity is zero, calculate the solution for times from *t*=0 to *t*=10 *s*, repeat the calculation for several different values of the time step and compare the results with the exact solution to equation (e). It turns out that for this simple case, the Euler method gives the exact result.

<br /> 
**Method:**
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Similar to equation(c), the solution to equation (e) is:

![](http://latex.codecogs.com/gif.latex?$$v(t+\\Delta t)=v(t)+\\frac{dv(t)}{dt} \\Delta t=v(t)-g\\Delta t \\qquad(f)$$)

while here is an equal sign instead of an approximately equal sign, since the Taylor expansion of *v*(*t*) gives the exact result and the second and higher order derivatives of *v*(*t*) is zero. That's why the numerical method, i.e. the Euler method, gives the exact solution of *v*(*t*).

The pseudocode for applying Euler method to this simple problem consists of four basic tasks:

* Declare necessary variables and arrays.
* Initialize variables.
* Do the calculation according to equation (f).
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

![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-1/A4.jpg)

<br /> 
**Conclusion:**
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For this simple case, i.e., the time dependence of velocity with a constant acceleration, the Euler method gives the exact solution and the solution is independent of time steps.

<br /> 
