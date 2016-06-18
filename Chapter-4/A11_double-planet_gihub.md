**EXERCISE: 4.7** 

[Source Code: A11.py](https://github.com/ZQTXLC/computationalphysics_N2012301020134/blob/master/Chapter-4/A11.py)

###<p align="center">A hypothetical celestial system consisting of two planets</p>
#####<p align="center">Chun lin</p>
#####<p align="center">Student ID: 2012301020134, Major: Physics Base Class</p>


**Abstract:**
The movement of a celestial system consisting of two planets with close masses is not as simple as the solar system, where the mass of sun is far above other planets within. This paper will show the motion of two planets with approximate masses.

<br /> 
**Introduction:**
<br>
&emsp;&emsp;If we want to study the essential consequences of the fundamental physical principles, it thus seems best to consider a system ii which frictional fores are as small as possible. The solar system is just such a laboratory. Let's consider a hypothetical solar system, consisting of a planet, say the earth and a sun with a sufficiently large mass only, so that the motion of the sun can be neglected. Constructing a polar coordinates system where the sun is located in the center. On accordance with the Newton's law of gravitation between the sun and the earth and the Newton's second law of motion, it not so difficult to write out the equations of motion of the earth. Following the usual approach of Euler method, we have:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\frac{dv_x}{dt}=-\\frac{GM_sx}{r^3} \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad(11.1)$$)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\frac{dx}{dt}=v_x $$)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\frac{dv_y}{dt}=-\\frac{GM_sy}{r^3} $$)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\frac{dy}{dt}=v_y $$)

For convenience, we will use astronomical units, AU, throughout this paper. the pseudocode for this problem, that is to calculate the trajectory of earth, in AU is describe as following: (based on Euler-Cromer method)

* For each time step *i* calculate the velocities and positions at time step *i+1*.

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$>v_{x,i+1}=v_{x,i}-\\frac{4\\pi^2x_i}{r_i^3}\\Delta t $$)

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$>x_{i+1}=x_i+ v_{x,i+1}\\Delta t$$)

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$>v_{y,i+1}=v_{y,i}-\\frac{4\\pi^2y_i}{r_i^3}\\Delta t $$)

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$>y_{i+1}=y_i+ v_{y,i+1}\\Delta t$$)

&emsp;&emsp;For a system consisting of two planets with approximate masses, we need to consider the motion of two planets both. Since we can not neglect the movement of any planet, they will respond to the mutual acting force and move together. It's the main task in this paper that to obtain this different picture.

<br /> 
**Method and results:**
<br>
&emsp;&emsp;The main code for calculating the solar system is illustrated as below:

    def calculate(totaltime):
        global x, y, vx, vy, r, t
        for i in range(totaltime-1):
            vx['m1'].append(vx['m1'][i] - 4*pi**2*x['m1'][i]/r['m1'][i]**3*dt)
            vy['m1'].append(vy['m1'][i] - 4*pi**2*y['m1'][i]/r['m1'][i]**3*dt)
            x['m1'].append(x['m1'][i] + vx['m1'][i+1]*dt)
            y['m1'].append(y['m1'][i] + vy['m1'][i+1]*dt)
            t.append(t[i] + dt)
            r['m1'].append(sqrt(x['m1'][i]**2+y['m1'][i]**2))

where the program stores the results in dictionaries, due to the convenience of storing the results of two planets. The direct result is shown in Figure 11.1. Because the motion of sun can be neglected, the earth moves around the sun with a nicely circular orbit. Definitely, the initial conditions have been chosen properly. To be more intuitional, the animation in Figure 11.2 has revealed the time dependence of the motion of the earth within one year.

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-4/A11_xy.jpg)<p align="center">Figure 11.1, The circular orbit of Earth</p>

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-4/A11_earth.gif)<p align="center">Figure 11.2, An animation of the Earth orbiting around the sun</p>

------
&emsp;&emsp;For a celestial system consisting of two planets with close masses, it's a little bit complicated. Assuming the two planets have mass of ![](http://latex.codecogs.com/gif.latex?$$m_1$$) and ![](http://latex.codecogs.com/gif.latex?$$m_2$$) and the distance between them is ![](http://latex.codecogs.com/gif.latex?$$r_0$$). Thus the gravitational force between them is:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$F=\\frac{Gm_1m_2}{r_0^2} \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\ (11.2)$$)

For this system, the two planets will move around orbiting the center of the total mass, it's not so tough to obtain the movement radiuses:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$r_1=\\frac{m_2r_0}{m_1+m_2} \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad(11.3)$$)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$r_2=\\frac{m_1r_0}{m_1+m_2}$$)

Taking the initial conditions that the total linear momentum is zero:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$m_1v_1=m_2v_2 \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\ \\ (11.4)$$)

where the *v* is the speed of the corresponding planet. Moreover, the gravitational force is equal to the centripetal force:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$F=\\frac{m_1v_1^2}{r_1} \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad (11.5)$$)

Combining the equations above yields the speeds of the two planets:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$v_1=\\sqrt{\\frac{Gm_2^2}{(m_1+m_2)r_0}} \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\quad \\ (11.6)$$)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$v_2=\\sqrt{\\frac{Gm_1^2}{(m_1+m_2)r_0}}$$)

Therefore, given the masses and distance of the two planets, they will move around orbiting the center of the total masses with speeds of ![](http://latex.codecogs.com/gif.latex?$$v_1$$) and ![](http://latex.codecogs.com/gif.latex?$$v_2$$) respectively. In addition to that, because of the mutual force, which is always through the center of the total masses, the angular velocities of the two planets are equal. Given the math above, it's not very difficult to revise the code above to suit for two moving planet, actually, if we take the mass of one planet far more than the another and this planet will be approximately stationary, that is the case in solar system where the mass of the sun is far larger than other planets. The animation below gives a result of two planets with the conditions that the mass of the black one is twice the mass of the white one. If the masses of the two are equal, they will move around the same orbit but stay at the opposite position.

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-4/A11_xy_m1m2.gif)<p align="center">Figure 11.3, An animation of the movement of two planets with different masses</p>

<br /> 
**Conclusion:**
<br>
&emsp;&emsp;For a celestial system consisting of two planets with close masses, the two planets will move around orbiting the center of the total mass with same angular velocity.

<br />
**Reference:**
<br>
Giordano, N. J., & Nakanishi, H. (2006). Computational physics. Pearson Education India.

<br />




