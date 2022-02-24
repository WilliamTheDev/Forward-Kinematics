# Foward-Kinematics 

Equations:<br>
x = L1 x cos θ1 + L2 x cos(θ1 + θ2) + L3 x cos(θ1 + θ2 + θ3)<br>
y = L1 x sin θ1 + L2 x sin(θ1 + θ2) + L3 x sin(θ1 + θ2 + θ3)<br>
φ = θ1 + θ2 + θ3

The equations above are the ones, I used to predict the motion of a 3-axis robotic arm on a cartesian plane (X, Y, -X, -Y). The robotic arm is make out of three different arm sections. L1, L2, L3, these lengths are linked together from the origin located {0} at the base joint. We also have to assume an end-effector frame {4} has been attached to the top of the thrid link. We get the end-effector frame {4} as a function of the joint angles (θ1, θ2, θ3).

![Capture](https://user-images.githubusercontent.com/69966592/155539065-f4da8fb6-702c-4d8e-bdb4-b76e76ad787c.PNG)
<br>
Note that Each joint also has a end-effector frame too {1}, {2}, {3}.
<br>
<br>
So if we wanted to predict the motion a 3-axis robotic arm, we will need to have define the origin point location {0} and the lengths of all three links. For example, the fixed origin point will be (x=0, y=0). And the lengths of the links will be 100, 80, 20 and joint angles will be 20°, 30°, -5°.

-----------------------
X - J1:  91.29452507276277
Y - J1:  40.808206181339195
-----------------------
X - J2:  70.30453677644846
Y - J2:  118.00548846070825
-----------------------
X - EP:  87.32260726713082
Y - EP:  128.51192823706285
-----------------------
