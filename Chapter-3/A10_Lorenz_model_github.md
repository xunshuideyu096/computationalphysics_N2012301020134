**EXERCISE: 3.26** 

[Source Code: A10.py](https://github.com/ZQTXLC/computationalphysics_N2012301020134/blob/master/Chapter-3/A10.py)

###<p align="center">Phase-space plots for the Lorenz model with different values of *r*</p>
#####<p align="center">Chun lin</p>
#####<p align="center">Student ID: 2012301020134, Major: Physics Base Class</p>


**Abstract:**
The Lorenz model, consisting of three simple equations, is essential for making headway on the weather problem. This paper will introduce this model simply and construct the Poincare section phase-space plots in different *r* parameter regimes.

<br /> 
**Introduction:**
<br>
&emsp;&emsp;When we think of chaotic or unpredictable behavior, and example that naturally comes to mind is the weather. Because of the economic importance of having accurate wehather predictions, a good deal of effort has been devoted to this problem. It's work of this kind by the atmospheric scientist E. N. Lorenz that provided a major contribution to the moder filed of chaos. The specific situation Lorenz considered when studying the basic equations of fluid mechanics, which are knows as the Navier-Stokes equations, was the Rayleigh-Benard problem that concerns a fluid in a container whose top and bottom surfaces are held at different temperatures. He considered a greatly simplified version of the Navier-Stokes equations as applied to this particular problem, and he reduced it to only three equations:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\frac{dx}{dt}=\\sigma(y-x) \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad(10.1)$$)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\frac{dy}{dt}=-xz+rx-y$$)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\frac{dz}{dt}=xy-bz$$)

here the Lorenz variables *x*, *y*, and *z* are derived from the temperature, density, and velocities in the original Navier-Stokes equations, and the parameters in equations (10.1) are measures of the temperature difference across the fluid and other fluid parameters. There are known as Lorenz equations or Lorenz model. Any behavior we find in the Lorenz model will certainly be found in the weather problem. Moreover it makes strategic sense to attack the Lorenz model first, since we would have no hope of making headway on the weather problem if we can not solve this simple model first. The suitability of an algorithm depends on the problems. Fortunately, the  Euler method can actually be used to treat Lorenz problem even it fails when facing simple pendulum problem. 

&emsp;&emsp;The behavior of Lorenz model depends on the parameters. We will follow custom and use ![](http://latex.codecogs.com/gif.latex?$$\\sigma = 10 $$) and ![](http://latex.codecogs.com/gif.latex?$$b =8/3 $$). The parameter __*r*__ is a measure of the temperature difference between the top and bottom surfaces of the fluid. For small *r*, the effective force on the fluid is small in the sense that there is very litter heat carried by the fluid and as *r* increases this force increases, which means that *r* plays a role analogous to the driving force in the pendulum problem. For a small *r*, the behavior corresponds to steday convective motion in the original fluid, whichi is the analog of regular nonchaotic motion of pendulum. However, for some specific values of *r*, there will appear an irregular, unpredictable, chaotic time dependence.The transition from steady convection to chaotic behavior takes place at *r* = 470/19 ≈ 24.47. 

&emsp;&emsp; Now we consider how to construct a phase-space plot for the Lorenz model. Perhaps the simplest way is to imagine that *x*, *y*, and *z* are coordinates in some abstract space and recognize that we are dealing with a trajectory in this space. We can then obtain a projection of this trajectory by simply plotting *z* as a function of *x*, which gives a projection onto the *x-z* plane. 

&emsp;&emsp;The Poincare sections can reveal underlying regularities that are not obvious from the time dependence alone, also, it can revel the attractors in a particularly clear way in the chaotic regime. Lorenz variables *x*, *y* and *z* can be viewed as specifying the trajectory of a particle moving in three dimensions. It then natural to consider two-dimension slices through this trajectory. That is to plot the trajectory projected onto certain coordinate plane, namely intersects with that plane. It turns out that there is a very high degree of regularity in the Poincare sections, that is we can predict with certainty that the system will be found somewhere on the attractor surface in phase space. In this paper, a program will be used to reveal some properties of Lorenz model and construct the Poincare section phase-space plots in different *r* parameter regimes.

<br /> 
**Method and results:**
<br>
&emsp;&emsp;The pseudocode for calculation based on equations (10.1) is illustrated as below:

* For each time step *i* calculate ![](http://latex.codecogs.com/gif.latex?$$x, y, z, t $$) at time step *i+1*.

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$>x_{i+1}=x_i+ \\sigma(y_i-x_i)\\Delta t $$)

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$>y_{i+1}=y_i+ (-x_iz_i+rx_i-y_i)\\Delta t$$)

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$>z_{i+1}=z_i+ (x_iy_i-bz_i)\\Delta t$$)

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$>t_{i+1}=t_i+\\Delta t$$)

The main code for calculation using Euler method s shown as following:

    def calculate(totaltime,s2):
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

&emsp;&emsp;Some results with small values of *r* for *z* as a function of time are shown in Figure 10.1, where the time step is 0.0001 s and the initial conditions are *x* = 1, *y* = *z* = 0, these conditions are held throughout this paper. Notes that *x* and *y* exhibit qualitatively similar behavior. For *r* = 5 and 10, there existing an initial decaying transient, after which *z* becomes constant, the larger *r*, the longer time the transient takes to decay away. These two cases correspond to steady convective motion in the original fluid. In this process, the *warm* fluid produces at the bottom surface of the container rises and the cooler fluid returns from the the top, which represents a steady convection and is the analog of regular nonchaotic motion of the pendulum. The behavior is completely different at *r* = 25, where the initial transient is roughly periodic, yet it gives way to an irregular chaotic time dependence after *t* = 20 or so. 

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A10_zt.jpg)<p align="center">Figure 10.1, Variation of the Lorenz variable *z* as a function of time with some small values of *r*.</p>

&emsp;&emsp;To obtain the phase-space plot, Figure 10.2 plots *z* as a function of *x*, which gives a projection onto the *x-z* plane, with the case that *r* = 25. Obviously, the system undergoes approximately periodic oscillations (roughly circular orbits) on one side of the line *x* = 0, then moves to the opposite side and undergoes a new series of oscillations.

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A10_zx.jpg)<p align="center">Figure 10.2, Trajectory of the Lorenz model projected onto the *x-z* plane.</LI></p>

&emsp;&emsp;Consider two-dimension Poincare sections through the trajectory. Here, for instance, has plotted the trajectory intersects with x =0 plane, i.e., a plot of v versus y only when x = 0, as shown in Figure 10.3. It's a little bit surprising the complicated chaotic behavior with a strange phase-space plot could produce this kind of very high degree of regularity in the Poincare sections. 

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A10_yz_x=0_r=025.jpg)<p align="center">Figure 10.3, Poincare section of the Lorenz model projected onto the *x = 0* plane with r = 25.</LI></p>

------

&emsp;&emsp;Now, let's consider some other values of *r*. The program has performed values of *r* from 0 to 160, as shown in the following animation (Figure 10.4). To confirm the transition around *r* = 25 from steady convection to chaotic behavior, the program has also given out a detailed transition procedure with *r* from 23 to 25 with a step of 0.1, as illustrated in Figure 10.5. It turn out that the transition indeed occurs at some values of *r* between 24.0 and 25.0. An interesting result is that there is a seemly periodic behavior for *z* as a function of time with *r* = 23.9, as illustrated in Figure 10.6, which occurs at a much earlier time.

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A10_zt.gif)<p align="center">Figure 10.4, An animation for *z* as a function of time with the values of *r* from 0 to 160.</LI></p>

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A10_zt_23-25.gif)<p align="center">Figure 10.5, An animation for *z* as a function of time with the values of *r* from 23.0 to 25.0.</LI></p>

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A10_zt_r=23.9.jpg)<p align="center">Figure 10.6, A seemly periodic behavior for *z* as a function of time with *r* = 23.9.</LI></p>

&emsp;&emsp;At *r* = 160, as shown in Figure 10.7, the result gives a periodic oscillation. While the waveform of these oscillations is certainly not simple, they are stable and persist forever. This corresponds to period-1 behavior. When examining the behavior as *r* is made smaller, Figure 10.8 and 10.9 indicates the observation of period-doubling and four times period behavior respectively.

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A10_zt_r=160.jpg)<p align="center">Figure 10.7, A periodic behavior for *z* as a function of time with *r* = 160.</LI></p>

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A10_zt_r=152.jpg)<p align="center">Figure 10.8, Period-doubling behavior for *z* as a function of time with *r* equal to 152 or so.</LI></p>

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A10_zt_r=146.jpg)<p align="center">Figure 10.9, Four times period behavior for *z* as a function of time with *r* equal to 146 or so.</LI></p>

----------
&emsp;&emsp;To observe the Poincare sections for a variety of *r*, the animation below gives a sketch with the values of *r* from 0 to 160. For *r* from 0 to 23, there is no Poincare section, when *r* reaches the values from 24 to 78, the figure demonstrates a shape of something like a bending character 'v'. Starting from *r* equal to 79, the picture emerges some hint of double 'v' shape, while some irregular lines mixing at some particular values of *r*. At some specific values of *r*, the double 'v' shape figure is clear, as shown in Figure 10.11. The Poincare section with *r* = 160 is shown in Figure 10.12.

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A10_yz.gif)<p align="center">Figure 10.10, An animation for Poincare section of the Lorenz model projected onto the *x = 0* plane with the values of *r* from 0 to 160.</LI></p>

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A10_yz_x=0_r=122.jpg)<p align="center">Figure 10.11, The Poincare section with *r* = 122.</LI></p>

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A10_yz_x=0_r=160.jpg)<p align="center">Figure 10.12, The Poincare section with *r* = 160.</LI></p>

<br /> 
**Conclusion:**
<br>
&emsp;&emsp;This paper has introduced the Lorenz model simply, plotted the Lorenz variable *z* as a function of time and constructed the Poincare section phase-space plots, with *r* values from 0 to 160.

<br /> 
**Reference:**
<br>
Giordano, N. J., & Nakanishi, H. (2006). Computational physics. Pearson Education India.

<br />




