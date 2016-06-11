**EXERCISE: 2.19** 

[Source Code: A7.py](https://github.com/ZQTXLC/computationalphysics_N2012301020134/blob/master/Chapter-2/A7.py)

###<p align="center">The effect of backspin on the range of a batted ball</p>
#####<p align="center">Chun lin</p>
#####<p align="center">Student ID: 2012301020134, Major: Physics Base Class</p>


**Abstract:**
The spin of a thrown or pitched ball can have a tremendous influence on its flying path. In this paper, modeling the effect of backspin on a batted ball is done, and it turns out that with a backspin, the batted ball can fly a distance longer than non-spin case.

<br /> 
**Introduction:**
<br>
&emsp;&emsp;For the purpose of getting insight into the problem of a thrown or pitched ball, two main distinct effects should be placed in the center of the discussion.The focus of this paper is the effect of the spin, which turns out to dominate the motion of a curve ball. In addition to spin effect, there is actually another aspect that influences the trajectory of a flying ball seriously, that is the difference in the drag coefficients for rough and smooth balls. In figure 7.1, the variation of the drag coefficients with different smoothness is shown, and we can these complicated behaviors are badly dependent on the surface smoothness of the ball.

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-2/A7_Drag_coefficient.png)<p align="center">Figure 7.1, Variation of the drag coefficient</p>

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-2/A7_force_spin.png)<p align="center">Figure 7.2, Forces acting on a spinning ball</p>

&emsp;&emsp;Let's get back to the point of spin effect, the origin of the force that makes a spinning ball curve can be appreciated when recalling the drag force form of ![](http://latex.codecogs.com/gif.latex?$$F_{drag}\\sim v^2 $$), where *v* is the speed of the object relative to the air. For a ball spinning about an axis perpendicular to the direction of travel, this speed will be various on opposite sides of the ball, as illustrated in Figure 7.2. In Figure 7.2, the bottom of the spinning ball will have a larger velocity relative to the air than will the top due to the spin, which results in a larger drag force at the bottom edge of the ball than at the top edge. The bottom force will have a component directing towards the -*z* direction on account of the curved face of the ball, vice versus. This gives rise to a component of the net force in -*z* direction, the so called Magnus force, which is perpendicular to the (center of mass) velocity. Still, we expect this force to be proportional to ![](http://latex.codecogs.com/gif.latex?$$B_2 $$): 

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$F_{drag}=-B_2v^{2}\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\ (7.1)$$)

For the sake of hard of estimating this coefficient, here will simply argue for the general functional form of this force and then resort to experiments to determine the overall magnitude. From the discussion above, the upward and downward components of the drag force on the bottom and upper part of the ball are proportional to the square of the velocity of this surface relative to the air, respectively, that is ![](http://latex.codecogs.com/gif.latex?$$(v+r\\omega)^2 $$) and ![](http://latex.codecogs.com/gif.latex?$$(v-r\\omega)^2 $$). The Magnus force is equal to the difference between there two terms:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$F_{M}\\propto (v+r\\omega)^2-(v-r\\omega)^2\\sim vr\\omega \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\quad(7.2)$$)

Therefore the net spin dependent force have the general form:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&nbsp;![](http://latex.codecogs.com/gif.latex?$$F_{M}=S_0\\omega v_x\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\ \\ (7.3)$$)

The coefficient will be determined via experiments and as illustrated in Figure 7.1 it will depend on *v*, yet for simplicity, a constant ![](http://latex.codecogs.com/gif.latex?$$S_o $$) will be assumed throughout this paper. 

&emsp;&emsp;In general, to calculate the trajectory of a curve ball needs to consider there-dimension motion. This paper focuses on the effect of backspin, reducing the problem into two-dimension motion.

<br /> 
**Method and Results:**
<br>
&emsp;&emsp;Let *x* and *y* be the axises of flying distance and height of the ball respectively. Again, splitting the motion differential equations into two first-order differential equations respectively and then using standard Euler method to solve each equation, that is writing each derivative in finite difference form, which leads to :

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&nbsp;![](http://latex.codecogs.com/gif.latex?$$x_{i+1}=x_i+v_{x,i}\\Delta t\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\quad\\ \\ \\ (7.4a)$$)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$y_{i+1}=y_i+v_{y,i}\\Delta t\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad (7.4b)$$)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;![](http://latex.codecogs.com/gif.latex?$$v_{x,i+1}=v_{x,i}-\\frac{B_2v_iv_{x,i}}{m}\\Delta t \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\quad(7.4c)$$)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;![](http://latex.codecogs.com/gif.latex?$$v_{y,i+1}=v_{y,i}-(g-\\frac{S_0\\omega v_{x,i}}{m})\\Delta t \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\ \\ (7.4d)$$)



Over the velocity range that is usually of interest to a pitcher, an estimation from the experimental data gives that ![](http://latex.codecogs.com/gif.latex?$$S_0/m\\approx 4.1\\times 10^{-4} $$), where *m* = 149 g is the mass of the ball. These equations of motion include the effects of atmospheric drag on the largest x component of the velocity, with a velocity dependent coefficient, but not for y component of velocity, since the fores are much smaller in this case. Note that the initial height of ball is not zero in this case, for simplicity, here assumes its value of 1 m. The terminal signal of the program is given by the sign of y coordinate, i.e., as ![](http://latex.codecogs.com/gif.latex?$$y_{i+1} $$) becomes negative, which means the ball struck the ground somewhere during the *i* th ![](http://latex.codecogs.com/gif.latex?$$\\Delta t $$) time step, and that means we should stop this loop. By interpolating between the last two calculated positions, ![](http://latex.codecogs.com/gif.latex?$$y_i,y_{i+1}$$), to estimate where the ball hits the ground. Take ![](http://latex.codecogs.com/gif.latex?$$r=-y_i/y_{i+1} $$) then a linear interpolation gives the hitting point of the ball (*l*):

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&nbsp;&nbsp;&nbsp;![](http://latex.codecogs.com/gif.latex?$$x_l=\\frac{x_i+rx_{i+1}}{r+1} \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\quad (7.5)$$)

&emsp;&emsp;The pseudocode for the effect of backspin on the range of a batted ball using Euler method is described as follows:

* Declare and initialize necessary variables, store position as (![](http://latex.codecogs.com/gif.latex?$$x_i,y_i $$)) and velocity as(![](http://latex.codecogs.com/gif.latex?$$v_{x,i},v_{y,i} $$)).
* For each time step *i*, calculate positions, the accelerations due to air drag forces or spin-dependent force and velocities at step *i*+1:

&emsp;![](http://latex.codecogs.com/gif.latex?$$\\bigtriangledown$$) The positions:

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\rhd\\quad x_{i+1}=x_i+v_{x,i}\\Delta t$$)
      
&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\rhd\\quad y_{i+1}=y_i+v_{y,i}\\Delta t$$)

&emsp;![](http://latex.codecogs.com/gif.latex?$$\\bigtriangledown$$) The accelerations due to air drag forces and spin-dependent force:

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\rhd\\quad \\frac{F_{drag,x}}{m}=-B_2vv_xe^{-y/y_0}/m$$)

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\rhd\\quad \\frac{F_{M}}{m}=S_0\\omega v_{x}/m$$)

&emsp;![](http://latex.codecogs.com/gif.latex?$$\\bigtriangledown$$) The velocities:

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\rhd\\quad v_{x,i+1}=v_{x,i}+\\frac{F_{drag,x}}{m}\\Delta t $$)

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\rhd\\quad v_{y,i+1}=v_{y,i}+(-g+\\frac{F_{M}}{m})\\Delta t$$)

&emsp;![](http://latex.codecogs.com/gif.latex?$$\\bigtriangledown$$) Stop when ![](http://latex.codecogs.com/gif.latex?$$y_{i+1}\\leq 0 $$).

* Estimate landing point using equation (7.5).

------
The core code for calculation is shown below, here, *theta* is the initial hitting angle which in this example is zero degree.

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

&emsp;&emsp;The result is that when the initial speed, angle and angular velocity are 30 m/s, ![](http://latex.codecogs.com/gif.latex?$$0^{\\circ} $$) and 2000rpm respectively, the hitting point of backspin ball considering spin-dependent force is 15.77 m, while the case ignoring spin effect is only 13.56 m, which differ about 14 %. In addition to that, as illustrated in Figure 7.3, spin-dependent force in this case is much larger than the *y* coordinate component of air drag force, which is negligible therefore.



&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-2/A7.jpg)<p align="center">Figure 7.3, The effect of backspin on the range of a batted ball</p>

<br /> 
**Conclusion:**
<br>
&emsp;&emsp;The batted ball with a backspin can fly a distance longer than non-spin case and the difference is as large as 14 % when the initial speed, angle and angular velocity are 30 m/s, ![](http://latex.codecogs.com/gif.latex?$$0^{\\circ} $$) and 2000rpm respectively.


<br /> 
**Reference:**
<br>
Giordano, N. J., & Nakanishi, H. (2006). Computational physics. Pearson Education India.

<br />


