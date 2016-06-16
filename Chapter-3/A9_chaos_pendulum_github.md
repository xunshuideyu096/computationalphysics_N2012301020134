**EXERCISE: 3.12** 

[Source Code: A9.py](https://github.com/ZQTXLC/computationalphysics_N2012301020134/blob/master/Chapter-3/A9.py)

###<p align="center">Constructing the Poincare sections for different cases</p>
#####<p align="center">Chun lin</p>
#####<p align="center">Student ID: 2012301020134, Major: Physics Base Class</p>


**Abstract:**
An interesting result of a nonlinear forced, damped pendulum is the occurrence of _Chaos_.This paper will confirm the existence of chaotic regime and construct the Poincare sections for different cases, i.e., at times in phase with the drive force, corresponding to the maximum of the drive force and ![](http://latex.codecogs.com/gif.latex?$$\\pi $$)/4 out-of-phase with the force.
.

<br /> 
**Introduction:**
<br>
&emsp;&emsp;&emsp;&emsp;A nonlinear pendulum means that the amplitude of the oscillation is not so small that allows us to take ![](http://latex.codecogs.com/gif.latex?$$sin\\theta $$) as ![](http://latex.codecogs.com/gif.latex?$$\\theta $$). For a nonlinear pendulum, we need to consider the situations in which the mass swings to large angles or even all the way around the pivot point of the pendulum, that is to consider the equation of motion:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\frac{d^2\\theta}{dt^2}=-\\frac{g}{l}sin\\theta \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\ \\ (9.1)$$)

where we ignore the friction and driving forces i.e., an *ideal* nonlinear pendulum. Obviously, the total mechanical energy is conserved and the pendulum executes a periodic motion. Its period is, however, no longer independent of amplitude. 

&emsp;&emsp;Take on a slightly more complex and also more interesting situation, that is to add all *real* ingredients to the *ideal* pendulum. Specifically speaking, consider a nonlinear pendulum with a frictional damp and a sinusoidal driving force, the equation of motion is:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\frac{d^2\\theta}{dt^2}=-\\frac{g}{l}sin\\theta-q\\frac{d\\theta}{dt}+F_Dsin(\\Omega_Dt) \\qquad\\qquad\\qquad\\qquad\\qquad\\quad\\ \\ (9.2)$$)

this is a nonlinear, damped, driven pendulum, or *physical pendulum*， where there is no known exact solution to it. To examine the behavior of ![](http://latex.codecogs.com/gif.latex?$$\\theta $$) as a function of time for several typical cases, the pseudocode for calculation on accord with equation (9.2) is illustrated as follows:

* For each time step *i* calculate ![](http://latex.codecogs.com/gif.latex?$$\\omega $$) and ![](http://latex.codecogs.com/gif.latex?$$\\theta $$) at time step *i+1*.

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$>\\omega_{i+1}=\\omega_i+(F_Dsin(\\Omega_Dt_i)-\\frac{g}{l}sin\\theta_i-q\\omega_i)\\Delta t$$)

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$>\\theta_{i+1}=\\theta_i+\\omega_{i+1}\\Delta t$$)

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$>if\\  \\theta_{i+1}$$) is out of the range ![](http://latex.codecogs.com/gif.latex?$$[-\\pi,\\pi]$$), add or subtract ![](http://latex.codecogs.com/gif.latex?$$2\\pi$$) to keep it in this range.

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$>t_{i+1}=t_i+\\Delta t$$)

An interesting result of this *physical pendulum* is the occurrence of __Chaos__. The chaotic behavior in this case is that when the driven force reaches some values, the pendulum does not settle into any sort of repeating steady-state behavior and the motion is unpredictable, unlike a small driven force case which will transit into a steady, predictable oscillation motion in response to the driving force. It turns out that this system is both deterministic, for a small driving force, and unpredictable, for a larger value of driving force. To be more defined, by **chaotic**, means a system can obey certain deterministic laws of physics, but still exhibit behavior behavior that is unpredictable due to an extreme sensitivity to initial conditions.

&emsp;&emsp;It is true that ![](http://latex.codecogs.com/gif.latex?$$\\theta(t) $$) is unpredictable, however, it's possible to make certain accurate predictions concerning ![](http://latex.codecogs.com/gif.latex?$$\\theta $$), even in the chaotic regime. Instead of investigating ![](http://latex.codecogs.com/gif.latex?$$\\theta $$) as a function of time, consider the angular velocity ![](http://latex.codecogs.com/gif.latex?$$\\omega $$) as a function of ![](http://latex.codecogs.com/gif.latex?$$\\theta $$), which is sometimes referred to as a *phase-space* plot. The phase-space trajectory in chaotic regime exhibits many orbits that are nearly closed and that persist for only one or two cycles. Exhibiting a phase-space trajectory with significant structure is a common property of chaotic systems. More interesting, if we plot ![](http://latex.codecogs.com/gif.latex?$$\\omega $$) versus ![](http://latex.codecogs.com/gif.latex?$$\\theta $$) only at some particular times, which is known as a **Poincare section**, it would be very useful to analyze the behavior of dynamical system. In this paper, the nonlinear forced, damped pendulum will be numerically investigated. We will confirm the existence of chaotic regime and construct the Poincare sections for different cases.

<br /> 
**Method and results:**
<br>
&emsp;&emsp;The main code for this problem is shown below: the *calculation* function performs calculation, of which, the first parameter is the calculation total time, and the 2nd and 3rd parameters are two switches for whether to keep ![](http://latex.codecogs.com/gif.latex?$$-\\pi\\leq\\theta\\leq\\pi $$) and whether to output Poincare sections, the last parameter is the phase difference driving force and times, i.e., different cases for Poincare sections. Using this program, we can explore the behavior of Chaos.

    def calculate(totaltime,s1,s2,phase):
        global theta, omega, t
        for i in range(totaltime):
            omega.append(omega[i] + (F_D*sin(Omega_D*t[i]) - (g/l)*sin(theta[i]) - q*omega[i])*dt)
            theta.append(theta[i] + omega[i+1]*dt)
            t.append(t[i] + dt)
            if s1==1 and theta[i+1]>pi:
                theta[i+1] -= 2*pi
            if s1==1 and theta[i+1]<-pi:
                theta[i+1] += 2*pi
        if s2==1:  #Poincare section
            ti = []
            for n in range(int((totaltime+1)*dt*Omega_D/2/pi)):
                for i in range(len(t)):
                    if abs(t[i]-(2*n*pi+phase)/Omega_D)<=dt/2:
                        ti.append(i)
            thetai = []
            omegai = []
            for i in ti:
                thetai.append(theta[i])
                omegai.append(omega[i])
            theta = thetai
            omega = omegai

&emsp;&emsp;With a zero driving force, as shown in Figure 9.1, the motion is damped and the pendulum comes to rest after at most a few oscillations. These damped oscillations are a vestige of simple harmonic motion and its damped cousin.

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A9_F=0.jpg)<p align="center">Figure 9.1, Behavior of ![](http://latex.codecogs.com/gif.latex?$$\\theta $$) as a function of time with a driving force equal to 0</p>

&emsp;&emsp;With a driving force equal to 0.5, Figure 9.2 shows two regimes. The first few oscillations are affected by the decay of an initial transient as in the case of no driving force.The pendulum settles into a steady oscillation in response to the driving force when the transient is damped away.

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A9_F=0.5.jpg)<p align="center">Figure 9.2, Behavior of ![](http://latex.codecogs.com/gif.latex?$$\\theta $$) as a function of time with a driving force equal to 0.5</p>

&emsp;&emsp;The behavior changes radically when the driving force increases to 1.2, as illustrated in Figure 9.3. As stated above, the pendulum does not settle into any sort of repeating steady-state behavior even at a much longer time, and the motion is unpredictable. Figure 9.4 shows the results when keeping ![](http://latex.codecogs.com/gif.latex?$$-\\pi\\leq\\theta\\leq\\pi $$).

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A9_F=1.2.jpg)<p align="center">Figure 9.3, The chaotic behavior, with a driving force equal to 1.2</p>

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A9_F=1.2_pi.jpg)<p align="center">Figure 9.4, The chaotic behavior, with a driving force equal to 1.2 and keep ![](http://latex.codecogs.com/gif.latex?$$-\\pi\\leq\\theta\\leq\\pi $$)</p>

&emsp;&emsp;Figure 9.5 and 9.6 have shown the phase-space plot for different driving forces, that is to plot ![](http://latex.codecogs.com/gif.latex?$$\\omega $$) as a function of ![](http://latex.codecogs.com/gif.latex?$$\\theta $$). With a small driving force, after a short-time transient, the pendulum quickly settles into a regular orbit in phase space corresponding to the oscillatory motion. It can be shown that this final orbit is independent of the initial conditions. 

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A9_omega_vs_theta_F=0.5.jpg)<p align="center">Figure 9.5, The phase-space plot, with a driving force equal to 0.5</p>

&emsp;&emsp;The behavior in the chaotic regime, as shown in Figure 9.6, is a bit more surprising, which exhibits many orbits that are nearly closed and that persist for one or two cycles and is not completely random.

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A9_omega_vs_theta_F=1.2_pi.jpg)<p align="center">Figure 9.6, The phase-space plot, with a driving force equal to 1.2</p>

&emsp;&emsp;Figure 9.7, 9.8, 9.9 have shown the **Poincare sections** for different cases, i.e., at times are in phase with the drive force, corresponding to the maximum of the drive force and ![](http://latex.codecogs.com/gif.latex?$$\\pi $$)/4 out-of-phase with the force, respectively. We can see the strange attractors and the plot shapes are varied with different phase differences. Moreover, if we change a little for the parameters, like the driving force or driving frequency, the strange attractors will change their shapes and even disappear as the parameters have been altered a lot.

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A9_Poincare_phase=0.jpg)<p align="center">Figure 9.7, Poincare section for times that are *in phase* with the driving force</p>

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A9_Poincare_phase=pi_2.jpg)<p align="center">Figure 9.8, Poincare section for times corresponding to the *maximum* of the driving force</p>

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A9_Poincare_phase=pi_4.jpg)<p align="center">Figure 9.9, Poincare section for times ![](http://latex.codecogs.com/gif.latex?$$\\pi $$)/4 *out-of-phase* with the driving force</p>

<br /> 
**Conclusion:**
<br>
&emsp;&emsp;This paper has confirmed the existence of chaotic regime and construct the Poincare sections for different cases, i.e., at times in phase with the drive force, corresponding to the maximum of the drive force and ![](http://latex.codecogs.com/gif.latex?$$\\pi $$)/4 out-of-phase with the force and the shapes of Poincare section are varied with different phase differences.

<br />
**Reference:**
<br>
Giordano, N. J., & Nakanishi, H. (2006). Computational physics. Pearson Education India.

<br />




