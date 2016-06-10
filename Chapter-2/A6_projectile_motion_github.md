**EXERCISE: 2.9** 

[Source Code: A6.py](https://github.com/ZQTXLC/computationalphysics_N2012301020134/blob/master/Chapter-2/A6.py)

###<p align="center">The application of Euler method on the trajectory of a shell</p>
#####<p align="center">Chun lin</p>
#####<p align="center">Student ID: 2012301020134, Major: Physics Base Class</p>


**Abstract:**
When dealing with the realistic motion of objects through the air, it's impossible to only concentrate on simplest case ig-noring the *external factors* like the air resistance. Fortunately, these problems,involving complex air contribution, are all described by ordinary differential equations in which initial values are given and can be solve by the Euler method. In this paper, the realistic projectile motion, specifically speaking, the realistic trajectory of a shell fired by a cannon is investigated, a key aspect is the variation of air resistance with elevation. The result shows a maximum landing point with an angle of ![](http://latex.codecogs.com/gif.latex?$$46^{\\circ}$$) or so.

<br /> 
**Introduction:**
<br>
&emsp;&emsp; The realistic motion involving complex air contribution are good examples of interesting physics including the mechanics of macroscopic objects, which usually can not be solved analytically, but can be easily tackled with a computer program. For a reali-stic projectile motion, like the figure 6.1 has shown, the ideal trajectory, i.e., ignoring air resistance, is always higher and further than actual path with all kinds of air contribution. In addition to that, we all know that the maximum landing range occurs for a firing angle of ![](http://latex.codecogs.com/gif.latex?$$\\theta=45^{\\circ} $$) without air resistance, while when air drag is involved indeed, the maximum range happens typically at a lower fi-ring angle.

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-2/Projectile%20_motion_with_air_resistance.png)
<p align="center">Figure 6.1, The realistic trajectory of a shell fired by a cannon</p>

&emsp;&emsp;Specifically speaking, let's consider a projectile, that is a shell shot by a cannon, and take the air resistance into account. The physics of air resistance is a quite complex problem, which, in general, can be written in a fairly innocent form:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$F_{drag}\\approx-B_1v-B_2v^{2}\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad(6.1)$$)

where the first dominates at extremely low velocities and its coefficient ![](http://latex.codecogs.com/gif.latex?$$B_1$$) can be calculated for objects with simple shapes while at any reasonable velocity the ![](http://latex.codecogs.com/gif.latex?$$v^2$$) term dominates for most objects. To make matters worse, ![](http://latex.codecogs.com/gif.latex?$$B_2$$) can not be computed exactly for objects even as simple as a round ball. The best way to determine the drag coefficient of any particular object is via experiments like wind tunnel measurements, as shown in figure 6.2.

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-2/A6_wind_tunnel.png)
<p align="center">Figure 6.2, Wind tunnel measurement for a plane</p>

<br /> 
**Method:**
<br>
&emsp;&emsp; When overlooking air resistance, the equations of projectile motion according to Newton's second law is:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\frac{d^2x}{dt^2}=0\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad(6.2a)$$)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\frac{d^2y}{dt^2}=-g\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\quad\\ (6.2b)$$)

Equation group (6.2) are second-order differential equations as opposed to the first-order equations, so the treatment approach should alter a litter bit. Splitting the differential equations into two first-order differential equation respectively and then using standard Euler method to solve each equation, that is writing each derivative in finite difference form, which leads to:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&nbsp;![](http://latex.codecogs.com/gif.latex?$$x_{i+1}=x_i+v_{x,i}\\Delta t\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad(6.3a)$$)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;![](http://latex.codecogs.com/gif.latex?$$v_{x,i+1}=v_{x,i}\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\ \\ \\ (6.3b)$$)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$y_{i+1}=y_i+v_{y,i}\\Delta t\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad(6.3c)$$)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;![](http://latex.codecogs.com/gif.latex?$$v_{y,i+1}=v_{y,i}-g\\Delta t\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad(6.3d)$$)

When taking the air resistance into account, and given that the velocity of a shell is usually pretty large, so it's reasonable to assume that the magnitude of the drag force on the cannon shell can be written as:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$F_{drag}^0=-B_2v^{2}\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\ \\ (6.4)$$)

here __*v*__ is the speed of the shell. Physically speaking, this force should be always directed opposite to the velocity, considering the vector components yields:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;![](http://latex.codecogs.com/gif.latex?$$F_{drag,x}^0=F_{drag}^0cos\\theta=F_{drag}^0(v_x/v)=-B_2vv_x\\qquad\\qquad\\qquad\\qquad\\qquad\\quad\\ \\ \\ (6.5)$$)

with a similar expression for ![](http://latex.codecogs.com/gif.latex?$$F_{drag,y}^0 $$).

&emsp;&emsp;Another crucial piece of physics involving in this problem is the air density which becomes lower at high elevation than at sea level. The air density influences dramatically the air drag without question, and the drag force will be less  at higher altitudes than at sea level. So here comes a issue, how the magnitude of air density depends on the elevation. The simplest model, that ignores the variance of temperature, is to treat the atmosphere as an isothermal ideal gas, which yields a result of elevation dependence of pressure *p* in the following form:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$p(h)=p(0)e^{-mgy/k_BT} \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\quad\\ \\ (6.6)$$)

where *y* is the altitude, *T* is the absolute temperature, *m* is the average mass of an air molecule and ![](http://latex.codecogs.com/gif.latex?$$k_B$$) is Boltzmann's constant. An evident property of ideal gas is that p is proportional to the density ρ, resulting:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&nbsp;&nbsp;![](http://latex.codecogs.com/gif.latex?$$\\rho=\\rho_0e^{-y/y_0} \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\quad\\; \\; \\; (6.7)$$)

where ![](http://latex.codecogs.com/gif.latex?$$y_0=k_BT/mg \\approx 1.0\\times 10^4 m, \\rho_0 $$) is density at h=0. What deserves attention is this isothermal model of atmosphere is not very realistic, since the aire temperature varies significantly over height changes of a few kilometers. Some other model such as adiabatic model can predict a totally different result. Here, the isothermal approximation is a decent treatment. The drag force duo to air resistance is proportional to the density, that means:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;![](http://latex.codecogs.com/gif.latex?$$F_{drag}=\\frac{\\rho}{\\rho_0}F_{drag}^0 \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\quad\\ \\ \\ \\ \\ (6.8)$$)

Substituting equation (6.8) with equation (6.5) and (6.7) yields:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;![](http://latex.codecogs.com/gif.latex?$$F_{drag,x}=-B_2vv_xe^{-y/y_0}\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad(6.9a)$$)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;![](http://latex.codecogs.com/gif.latex?$$F_{drag,y}=-B_2vv_ye^{-y/y_0}\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad(6.9b)$$)

Adding equation (6.9) to equation (6.3) leads to:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&nbsp;![](http://latex.codecogs.com/gif.latex?$$x_{i+1}=x_i+v_{x,i}\\Delta t\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\quad\\ \\ (6.10a)$$)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$y_{i+1}=y_i+v_{y,i}\\Delta t\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\quad\\ \\ (6.10b)$$)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;![](http://latex.codecogs.com/gif.latex?$$v_{x,i+1}=v_{x,i}-\\frac{B_2v_iv_{x,i}e^{-y_i/y_0}}{m}\\Delta t \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad(6.10c)$$)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;![](http://latex.codecogs.com/gif.latex?$$v_{y,i+1}=v_{y,i}-(g+\\frac{B_2v_iv_{y,i}e^{-y_i/y_0}}{m})\\Delta t \\qquad\\qquad\\qquad\\qquad\\quad\\ \\ \\ (6.10d)$$)

Mathematically speaking, the time evolution according to equation (6.10) is continued forever, however, as ![](http://latex.codecogs.com/gif.latex?$$y_{i+1} $$) becomes negative, which means the shell struck the ground somewhere during the *i* th ![](http://latex.codecogs.com/gif.latex?$$\\Delta t $$) time step, and that means we should stop this loop, since this is the physics of this problem. By interpolating between the last two calculated positions, ![](http://latex.codecogs.com/gif.latex?$$y_i,y_{i+1}$$), to estimate where the shell hit the ground. Take ![](http://latex.codecogs.com/gif.latex?$$r=-y_i/y_{i+1} $$) then a linear interpolation gives the landing point of the shell (*l*):

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&nbsp;&nbsp;&nbsp;![](http://latex.codecogs.com/gif.latex?$$x_l=\\frac{x_i+rx_{i+1}}{r+1} \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\ \\ \\ (6.11)$$)

and it's worth noticing that the *y* coordinates of landing point, ![](http://latex.codecogs.com/gif.latex?$$y_l $$) may *not* be zero.


&emsp;&emsp;The pseudocode for the cannon shell projectile using Euler method is described as follows:

* Declare and initialize necessary variables, store position as (![](http://latex.codecogs.com/gif.latex?$$x_i,y_i $$)) and velocity as(![](http://latex.codecogs.com/gif.latex?$$v_{x,i},v_{y,i} $$)).
* For each time step *i*, calculate positions, the accelerations due to air drag forces and velocities at step *i*+1:

&emsp;![](http://latex.codecogs.com/gif.latex?$$\\bigtriangledown$$) Positions:

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\rhd\\quad x_{i+1}=x_i+v_{x,i}\\Delta t$$)
      
&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\rhd\\quad y_{i+1}=y_i+v_{y,i}\\Delta t$$)

&emsp;![](http://latex.codecogs.com/gif.latex?$$\\bigtriangledown$$) The accelerations due to air drag forces:

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\rhd\\quad \\frac{F_{drag,x}}{m}=-B_2vv_xe^{-y/y_0}/m$$)

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\rhd\\quad \\frac{F_{drag,y}}{m}=-B_2vv_ye^{-y/y_0}/m$$)

&emsp;![](http://latex.codecogs.com/gif.latex?$$\\bigtriangledown$$) Velocities:

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\rhd\\quad v_{x,i+1}=v_{x,i}+\\frac{F_{drag,x}}{m}\\Delta t $$)

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\rhd\\quad v_{y,i+1}=v_{y,i}+(-g+\\frac{F_{drag,y}}{m})\\Delta t$$)

&emsp;![](http://latex.codecogs.com/gif.latex?$$\\bigtriangledown$$) Stop when ![](http://latex.codecogs.com/gif.latex?$$y_{i+1}\\leq 0 $$).

* Estimate landing point using equation (6.11).

-----
&emsp;&emsp;The core program for calculation is described as follows: the program obtains the components of *v* and stores as lists. The next `while` loop will continue running until ![](http://latex.codecogs.com/gif.latex?$$y_{i+1}$$)≤0. The program is based on the pseudocode stated above, one thing should be noted is *v* needs to be updated as well for each calculation.

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

**Results:**
<br>
&emsp;&emsp;In figure 6.3, a realistic trajectory of a shell considering air drag with different altitudes. The firing angle is ![](http://latex.codecogs.com/gif.latex?$$45^{\\circ}$$), initial speed is 700 m/s. Obviously, the maximum altitude and the landing position are much smaller than the ideal case without air resistance. Performing the program with different angles can yield a variety of landing points, some of which have been shown in figure 6.4. Figure 6.5 shows directly the angle dependence of landing positions, from which we can see clearly that the maximum landing distance appears with an angle of ![](http://latex.codecogs.com/gif.latex?$$46^{\\circ}$$) or so (error within ![](http://latex.codecogs.com/gif.latex?$$1^{\\circ}$$)).

&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-2/A6_45_2.jpg)<p align="center">Figure 6.3, The realistic trajectory of a shell considering air drag with different altitudes</p>

&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-2/A6.jpg)<p align="center">Figure 6.4, The realistic trajectory of a shell with different firing angles</p>

&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-2/A6_30-60_1.jpg)<p align="center">Figure 6.5, The landing points of different firing angles</p>

<br /> 

**Conclusion:**
<br>
&emsp;&emsp;The motion of a shell fired by a cannon has two key aspects which influence a lot on the shape of its flying path. One is air resistance and the another is the variation of air resistance with elevation. The result shows the maximum altitude and the landing position are much smaller than the ideal case without air resistance and a maximum landing distance appears with an angle of ![](http://latex.codecogs.com/gif.latex?$$46^{\\circ}$$) or so.

<br /> 







