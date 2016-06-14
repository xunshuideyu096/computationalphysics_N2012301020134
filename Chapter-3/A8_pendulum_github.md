**EXERCISE: 3.7** 

[Source Code: A8_3.7.py](https://github.com/ZQTXLC/computationalphysics_N2012301020134/blob/master/Chapter-3/A8_3.7.py)

[Source Code: A8_3.8.py](https://github.com/ZQTXLC/computationalphysics_N2012301020134/blob/master/Chapter-3/A8_nonlinear_3.8.py)

###<p align="center">Numerically investigate the linear forced damped pendulum and nonlinear ideal pendulum</p>
#####<p align="center">Chun lin</p>
#####<p align="center">Student ID: 2012301020134, Major: Physics Base Class</p>


**Abstract:**
Oscillatory motion is one of the most important phenomena in physics, this paper will investigate the linear forced pendulum. The numerical results has confirmed the existence of the resonance and the dependence of the resonant amplitude on the driving angular frequency ![](http://latex.codecogs.com/gif.latex?$$\\Omega_D $$) and on the friction  parameter *q*. Moreover, the Euler-Cromer method has been employed to investigate the relationship between the amplitude and period numerically in an nonlinear pendulum.

<br /> 
**Introduction:**
<br>
&emsp;&emsp;Examples of oscillatory phenomena can be found in many areas of physics, including the motion of electrons in atoms, the behavior of currents and voltages in electronic circuits and planetary orbits. The simplest mechanical system that exhibits such motion is, in a sense, a pendulum, consisting of a mass that is connected by a string to some sort of support so that it is able to swing freely in response to the force of gravity. In the idealized case, ignoring friction and assuming the angle the string makes with the vertical is small, such a pendulum undergoes what is known as simple harmonic motion, as illustrated in Figure 8.1. Figure 8.1 describes one example of a simple pendulum, i.e., a particle of mass *m* connected by a massless string to a rigid support, where ![](http://latex.codecogs.com/gif.latex?$$\\theta $$) is the angle that the taut string makes with the vertical. This simple model assumes that there are only two forces acting on the particle, gravity and the tension of the string. From the basic mechanics we know that the force perpendicular th the string is given by:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;;&emsp;;&emsp;![](http://latex.codecogs.com/gif.latex?$$F_{\\theta}=-mgsin\\theta \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\quad(8.1)$$)

where the minus sign reminds us that the force is always opposite to the displacement from the equilibrium position where ![](http://latex.codecogs.com/gif.latex?$$\\theta =0 $$),this is also a basic property of simple harmonic motion. Assuming ![](http://latex.codecogs.com/gif.latex?$$\\theta $$) is always small so that ![](http://latex.codecogs.com/gif.latex?$$sin\\theta \\approx \\theta$$), it's not so difficult to obtain the equation of motion:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\frac{d^2\\theta}{dt^2}=-\\frac{g}{l}\\theta \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\ (8.2)$$)

This is the central equation of simple harmonic motion, which has a general solution in the form of:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\theta=\\theta_0sin(\\Omega t+\\phi) \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\  (8.3)$$)

where ![](http://latex.codecogs.com/gif.latex?$$\\Omega =\\sqrt{(g/l)} $$) is the angular frequency whichi is independent of mass and the amplitude of the motion, and ![](http://latex.codecogs.com/gif.latex?$$\\theta_0 $$) and ![](http://latex.codecogs.com/gif.latex?$$\\phi $$) are constants that depend on on the initial displacement and velocity of the pendulum. The oscillations are sinusoidal with time and continue forever without decaying since there is no friction in the model. 

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A8_pendulum.png)<p align="center">Figure 8.1, A simple pendulum</p>

&emsp;&emsp;Now considering a numerical approach using Euler method to this problem. Equation (8.2) is second-order differential equations as opposed to the first-order equations. Splitting the differential equation into two first-order differential equations and then using standard Euler method to solve each equation, that is writing each derivative in finite difference form, which leads to:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\omega_{i+1}=\\omega_i-\\frac{g}{l}\\theta_i\\Delta t\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad(8.4a)$$)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;![](http://latex.codecogs.com/gif.latex?$$\\theta_{i+1}=\\theta_i+\\omega_i\\Delta t\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\ \\ (8.4b)$$)

The equations above can be employed to calculate the numerical solution using Euler method, the pseudocode 
for calculation is illustrated as follows:

* For each time step *i* calculate ![](http://latex.codecogs.com/gif.latex?$$\\omega $$) and ![](http://latex.codecogs.com/gif.latex?$$\\theta $$) at time step *i+1*.

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$>\\omega_{i+1}=\\omega_i-\\frac{g}{l}\\theta_i\\Delta t$$)

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$>\\theta_{i+1}=\\theta_i+\\omega_i\\Delta t$$)

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$>t_{i+1}=t_i+\\Delta t$$)


However, as illustrated in Figure 8.2 below, the behavior there is totally unusual, in short, the amplitude of the oscillations grows with time while the motion is basically oscillatory. This is not only at odds with our intuition, but beyond physics. It turns out the difficulty lies with our use of Euler method. Moreover, the energy of the pendulum will increase with time for any nonzero value of ![](http://latex.codecogs.com/gif.latex?$$\\Delta t $$).

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A8_energy_increasing.png)<p align="center">Figure 8.2, Euler method for a simple pendulum</p>

&emsp;&emsp;In effect, the problem encountering here is the inherent unstability of Euler method. Let's get insight into the total energy *E* to how this instability comes about:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$E=\\frac{1}{2}ml^2\\omega ^2+mgl(1-cos\\theta) \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\quad (8.5)$$)

In the limit of small ![](http://latex.codecogs.com/gif.latex?$$\\theta $$) the energy reduces to:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$E=\\frac{1}{2}ml^2(\\omega ^2+\\frac{g}{l}\\theta^2) \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\quad (8.6)$$)

Substituting ![](http://latex.codecogs.com/gif.latex?$$\\omega_{i+1} $$) and ![](http://latex.codecogs.com/gif.latex?$$\\theta_{i+1} $$) from equations (8.4) into equation (8.6) yields:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&ensp;&ensp;![](http://latex.codecogs.com/gif.latex?$$E_{i+1}=E_i+ \\frac{1}{2}mgl(\\omega_i ^2+\\frac{g}{l}\\theta_i^2)(\\Delta t)^2 \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\ (8.7)$$)

From equation (8.7) we can see the reason, the second term on the right is always positive unless ![](http://latex.codecogs.com/gif.latex?$$\\Delta t=0 $$), the total energy given by Euler method always increases with time.

&emsp;&emsp;For problems involving oscillatory motion, a numerical method must conserve energy over the long haul. Obviously, the Euler method is not a good choice for these types of problems. Indeed, there are several other different numerical approaches which work well in dealing with the oscillatory problems, including Runge-Kutta and Verlet methods. It turns out that a simple modification of the Euler method yields an algorithm that is also quite suitable, that is Euler-Cromer method. To appreciate this method, given below is a modified version of the calculation pseudocode:

* For each time step *i* calculate ![](http://latex.codecogs.com/gif.latex?$$\\omega $$) and ![](http://latex.codecogs.com/gif.latex?$$\\theta $$) at time step *i+1*.

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$>\\omega_{i+1}=\\omega_i-\\frac{g}{l}\\theta_i\\Delta t$$)

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$>\\theta_{i+1}=\\theta_i+\\omega_{i+1}\\Delta t$$)
(Note that ![](http://latex.codecogs.com/gif.latex?$$\\omega_{i+1} $$) is used to calculate ![](http://latex.codecogs.com/gif.latex?$$\\theta_{i+1} $$))

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$>t_{i+1}=t_i+\\Delta t$$)

For many other problems, such a minor change, i.e., substituting ![](http://latex.codecogs.com/gif.latex?$$\\omega_{i} $$) with ![](http://latex.codecogs.com/gif.latex?$$\\omega_{i+1} $$) makes no significant difference, however, for oscillatory motion the Euler_Cromer method conserves energy over each complete period of the motion, thus avoids the the difficulties encountering in Figure 8.2.

-----
&emsp;&emsp;For a *real* pendulum, adding some damping to equation (8.2), which is frictionless, the equation of motion has the form:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\frac{d^2\\theta}{dt^2}=-\\frac{g}{l}\\theta-q\\frac{d\\theta}{dt} \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\quad(8.8)$$)

where we assumed the damping force, which originates from the effective bearing where the string of the pendulum connects to the support, air resistance, etc., is proportional to the angular velocity and thus has the form of ![](http://latex.codecogs.com/gif.latex?$$-q(d\\theta /dt) $$). Therefore, *q* is a parameter that measures the strength of the damping.

&emsp;&emsp;While damped pendulum is more realistic, it's only a part of the whole story. No one would like to use a slowly dead pendulum, the tip is to drive it to move forever. Therefore, we should consider the addition of a driving force to the problem. The form of this force depends on how the force is applied, a convenient choice is to assume that the driving force is sinusoidal with time, with amplitude ![](http://latex.codecogs.com/gif.latex?$$F_D $$) and ![](http://latex.codecogs.com/gif.latex?$$\\Omega_D $$), which leads to the equation of motion:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\frac{d^2\\theta}{dt^2}=-\\frac{g}{l}\\theta-q\\frac{d\\theta}{dt}+F_Dsin(\\Omega_Dt) \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\quad(8.9)$$)

This driving force will pump energy into or out of the system, and the externally imposed frequency, will "complete" with the nature frequency of the pendulum, which yields much richer behaviors. It turns out that equation (8.9) can also be solved analytically, the steady state solution is:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\theta(t)=\\theta_0sin(\\Omega_Dt+\\phi) \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\ \\ \\ (8.10)$$)

where the amplitude is given by:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\theta_0=\\frac{F_D}{\\sqrt((\\Omega^2-\\Omega_D^2)^2)+(q\\Omega_D)^2}\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\quad(8.11)$$)

&emsp;&emsp;The driven, damped pendulum thus undergoes a simple harmonic oscillation with the angular frequency of the driving force so in some sense its behavior is even simpler than the non-driven case. There is a interesting situation, when the driving frequency ![](http://latex.codecogs.com/gif.latex?$$\\Omega_D $$) matches the natural angular frequency of the pendulum ![](http://latex.codecogs.com/gif.latex?$$\\Omega $$). In this case of *resonance*, the amplitude ![](http://latex.codecogs.com/gif.latex?$$\\theta_0 $$) can become large, especially if the friction is small.

&emsp;&emsp;So far, the discussion above is based on the assumption that the amplitude of the oscillation is small, which allows us to take ![](http://latex.codecogs.com/gif.latex?$$sin\\theta $$) as ![](http://latex.codecogs.com/gif.latex?$$\\theta $$). Now consider the situations in which the mass swings to large angles or even all the way around the pivot point of the pendulum, that is to consider the equation of motion:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$\\frac{d^2\\theta}{dt^2}=-\\frac{g}{l}sin\\theta \\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\qquad\\ \\ (8.12)$$)

where we ignore the friction and driving forces i.e., a ideal nonlinear pendulum. Obviously, the total mechanical energy is conserved and the pendulum executes a periodic motion. Its period is, however, no longer independent of amplitude. 

&emsp;&emsp;In this paper, the linear forced, damped pendulum with friction of equation (8.9) will be numerically investigated. We will confirm the existence of the resonance and the dependence of the resonant amplitude on the driving angular frequency ![](http://latex.codecogs.com/gif.latex?$$\\Omega_D $$) and on the friction  parameter *q*. At the same time, the Euler-Cromer method will be employed to investigate the relationship between the amplitude and period numerically in the nonlinear pendulum of (8.12).

<br /> 
**Method and results:**
<br>
&emsp;&emsp;The pseudocode for calculation of a linear forced and damped pendulum on accord with equation (8.9) is illustrated as follows:

* For each time step *i* calculate ![](http://latex.codecogs.com/gif.latex?$$\\omega $$) and ![](http://latex.codecogs.com/gif.latex?$$\\theta $$) at time step *i+1*.

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$>\\omega_{i+1}=\\omega_i+(F_Dsin(\\Omega_Dt_i)-\\frac{g}{l}\\theta_i-q\\omega_i)\\Delta t$$)

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$>\\theta_{i+1}=\\theta_i+\\omega_{i+1}\\Delta t$$)
(Note that ![](http://latex.codecogs.com/gif.latex?$$\\omega_{i+1} $$) is used to calculate ![](http://latex.codecogs.com/gif.latex?$$\\theta_{i+1} $$))

&emsp;&emsp;![](http://latex.codecogs.com/gif.latex?$$>t_{i+1}=t_i+\\Delta t$$)

where ![](http://latex.codecogs.com/gif.latex?$$\\omega_{i+1}=\\omega_i-\\frac{g}{l}sin\\theta_i\\Delta t$$) when considering a nonlinear ideal pendulum.

&emsp;&emsp;The core program for calculation for a linear forced and damped pendulum is illustrated as below:

	def calculate(totaltime):
		global i, theta, omega, t, a, b, T, amp
		i = 0
		for i in range(totaltime):
			omega.append(omega[i] + (F_D*sin(Omega_D*t[i]) - (g/l)*theta[i] - q*omega[i])*dt)
			theta.append(theta[i] + omega[i+1]*dt)
			t.append(t[i] + dt)
		for n in range(1,totaltime+1):  
			if theta[n-1]*theta[n]<= 0:
				a.append(n-1)
		for n in a:
			b.append((t[n+1]+t[n])/2)
		for n in range(len(b)-1):
			T.append((b[n+1]-b[n])*2)
			if b[n] > 15:
				amp.append(max(theta[int(n/dt):]))
				break

where *T* and *amp* represents the period and amplitude of steady state. 

&emsp;&emsp;For a simple pendulum, that is the driving force and damp is negligible, the result of the program above is shown in Figure 8.3. Note that the Euler_Cromer method is employed here to avoid unwilling increasing of amplitude or energy. A period of 2.006 s with a time step of 0.001 s is very close to the theoretical result of 2 s, plus the steady equal amplitude demonstrates that the Euler_Cromer method is reliable.

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A8_simple_EC.jpg)<p align="center">Figure 8.3, A simple pendulum based on the Euler_Cromer method</p>

&emsp;&emsp;Take the driving force and damping effects into account, the program yields a interesting result, which is presented in Figure 8.4. Figure 8.4 shows a typical result of a linear forced pendulum with friction of equation (8.9), that is, the driving angular frequency is distinct with the nature frequency. The steady period *T* is approximately equal to 3.14 s, which is determined by driving frequency, ![](http://latex.codecogs.com/gif.latex?$$T=\\frac{2\\pi}{\\Omega_D} $$), as illustrated in equation (8.10). The amplitude is given by equation (8.11). In short, the driven, damped pendulum undergoes a simple harmonic oscillation with the angular frequency of the frequency of driving force. However, when the driving angular frequency matches the nature frequency of the pendulum, a phenomena called *Resonance* occurs(see Figure 8.5), in which the amplitude can become much larger, as the friction or the damp is typically small in particular, as illustrated in Figure 8.6. In Figure 8.5, the friction parameter *q* is 1, so that the resonance is not very strong. As *q* becomes smaller, the amplitude of resonance will increase rapidly, as an example, Figure 8.6 shows a friction parameter of 0.2, no doubt that in this case, the steady resonance amplitude becomes a few times larger than its original amplitude and this ratio can be more than hundreds when *q* becomes much smaller. There always be some damp for a real pendulum so that the steady state of resonance phenomena can be reach at some time later on. An interesting case is that for an ideal pendulum, that is there is no damp, the rapidly increasing of amplitude in resonance state will never stop, some of the results are shown in Figure 8.7 (based on Euler method).

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A8_simple_EC.jpg)<p align="center">Figure 8.4, A linear forced and damped pendulum</p>

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A8_damp_force_resonance_nonzero_q.jpg)<p align="center">Figure 8.5, Resonance phenomena of a moderately damped pendulum</p>

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A8_damp_force_resonance_small_q.jpg)<p align="center">Figure 8.6, Resonance phenomena of an underdamped pendulum</p>

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A8_damp_force_resonance.jpg)<p align="center">Figure 8.7, Resonance phenomena of an undamped ideal pendulum</p>

&emsp;&emsp;The resonance phenomena is common in daily lives, it's a double-edged sword which means that it can bring harms to you or you can take advantage of it as well, it depends on your knowledge and usage on it

&emsp;&emsp;Figure 8.8 gives out the driving angular frequency dependence of resonant amplitude quantitatively. It's worth noting that the driving frequency is always equal to the nature frequency so that the resonance can happen. So the variation of ![](http://latex.codecogs.com/gif.latex?$$\\Omega_D $$) means the change of nature frequency ![](http://latex.codecogs.com/gif.latex?$$\\Omega $$). As equation (8.11) predicts, the amplitude decreases with an increasing ![](http://latex.codecogs.com/gif.latex?$$\\Omega_D $$).

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A8_damp_force_resonance_frequency_dependence.jpg)<p align="center">Figure 8.8, Driving angular frequency dependence of resonant amplitude</p>

&emsp;&emsp;Figure 8.9 demonstrates the friction parameter dependence of resonant amplitude, likewise, as *q* rises, the amplitude reduces, just in the way of equation (8.11).

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A8_damp_force_resonance_frequency_dependence.jpg)<p align="center">Figure 8.9, Friction parameter dependence of resonant amplitude</p>

--------

&emsp;&emsp;In the case of nonlinear pendulum, employing the Euler_Cromer method to investigate the relation between the amplitude and the period. The program of calculation is illustrated as below:

	def calculate(totaltime):
		global i, theta, omega, t, T, a, b
		i = 0
		for i in range(totaltime):
			omega.append(omega[i] - (g/l)*sin(theta[i])*dt)
			theta.append(theta[i] + omega[i+1]*dt)
			t.append(t[i] + dt)
		for n in range(1,totaltime+1):  
			if theta[n-1]*theta[n]<= 0:
				a.append(n-1)
		for n in a:
			b.append((t[n+1]+t[n])/2)
		for n in range(len(b)-1):
			T.append((b[n+1]-b[n])*2)

	theta0 = []
	T0 = []
	for n in range(1,int(50*pi)):
		theta_0 = n/100.0
		theta0.append(theta_0)
		initialize(0.001,theta_0)
		calculate(10000)
		T0.append(T[0])

where *theta0* and *T0* are the amplitude (initial amplitude) and the period. The result in Figure 8.10 indicates a larger amplitude with a longer period. This is obvious, since the object needs to travel longer time to get to the initial position for a larger amplitude. In a typical mechanical book, an angular requirement for a simple harmonic pendulum is usually set to 5 degree, which is represented in Figure 8.10 as well. From this numerical calculation, the deviation from a typical harmonic motion which means the period of motion is 2 s and holds at any time, is less than 0.5 % when the amplitude is less than ![](http://latex.codecogs.com/gif.latex?$$5^{\\circ} $$). So ![](http://latex.codecogs.com/gif.latex?$$5^{\\circ} $$) is a decent approximation for a harmonic pendulum.

&emsp;&emsp;&emsp;&emsp;&emsp;![](https://github.com/ZQTXLC/computationalphysics_N2012301020134/raw/master/Chapter-3/A8_nonlinear.jpg)<p align="center">Figure 8.10, The relationship between the amplitude and the period</p>

<br /> 
**Conclusion:**
<br>
&emsp;&emsp;The numerical results of a linear forced damped pendulum has confirmed the existence of the resonance and the monotonic decreasing dependence of the resonant amplitude on the driving angular frequency ![](http://latex.codecogs.com/gif.latex?$$\\Omega_D $$) and on the friction  parameter *q*. Moreover, the period becomes longer as the amplitude increases in an nonlinear pendulum.

<br /> 

**Reference:**
<br>
Giordano, N. J., & Nakanishi, H. (2006). Computational physics. Pearson Education India.

<br />




