from vpython import *
import math

#3-Axis Robotic Arm | Foward-Kinematics

#Modelling the motion of a 3-axis robotic arm on a Two dimensional plane (X, Y, -X, -Y).
#To use this program you will need to enter the initial conditions of the robotic arm. 
#L1, L2, L3, Theta1, Theta2 & Theta3:

L1 = 0 #Link 1 length 
L2 = 0 #Link 2 length
L3 = 0 #Link 3 length

Theta1 = 0 * pi/180#joint Angle 1 
Theta2 = 0 * pi/180#Joint Angle 2
Theta3 = 0 * pi/180#Joint Angle 3

Origin = [0,0,0] #Origin Point {0}
Base = [12, 12, 12] #Box 
OffSet = [0, 0, 7] #Pivot Offset
OffSet2 = [0, -12, 0] #Fixed Base Offset

# - W!lliam - 2022 | WilliamTheDev On Github 

scene.title = "3-Axis Robotic Arm"
scene.width = scene.height = 800
scene.range = 300

#The X postion of {2}
def X_J1():
    x1 = L1 * math.cos(Theta1)
    return x1
#The Y postion of {2}
def Y_J1():
    y1 = L1 * math.sin(Theta1)
    return y1

#The X postion of {3}
def X_J2():
    x2 = L1 * math.cos(Theta1) + L2 * math.cos(Theta1 + Theta2)
    return x2
#The Y postion of {3}
def Y_J2():
    y2 = L1 * math.sin(Theta1) + L2 * math.sin(Theta1 + Theta2)
    return y2

#The X postion of {4}
def X_End_Effector():
    x = L1 * math.cos(Theta1) + L2 * math.cos(Theta1 + Theta2) + L3 * math.cos(Theta1 + Theta2 + Theta3)
    return x
#The Y position of {4}
def Y_End_Effector():
    y = L1 * math.sin(Theta1) + L2 * math.sin(Theta1 + Theta2) + L3 * math.sin(Theta1 + Theta2 + Theta3)
    return y

#---------------------------------------------#
# - Objects                                   #
#---------------------------------------------#

#Base - Z-axis | Not enabled in V0.20 
base = box(pos=vec(Origin[0],Origin[1],Origin[2]), size=vec(Base[0],Base[1],Base[2]), color=vec(0.4,0.4,0.5))
#Base2 - Fixed
base2 = box(pos=vec(OffSet2[0], OffSet2[1], OffSet2[2]), size=vec(Base[0], Base[1], Base[2]), color=vec(0.4,0.4,0.5))
#Origin 
Origin = box(pos=vec(Origin[0], Origin[1], OffSet[2]), size=vec(3,3,3), color=color.white)
#Joint 1
pivot1 = box(pos=vec(X_J1(), Y_J1(), OffSet[2]), size=vec(3,3,3), color=color.purple)
#Joint 2
pivot2 = box(pos=vec(X_J2(), Y_J2(), OffSet[2]), size=vec(3,3,3), color=color.yellow)
#Joint 3
pivot3 = box(pos=vec(X_End_Effector(), Y_End_Effector(), OffSet[2]), size=vec(3,3,3), color=color.green)
#Link 1 
Link1 = box(pos=vec(0,L1/2,OffSet[2]), size=vec(5,L1,2), color=color.blue)
#Link 2
Link2 = box(pos=vec(pivot1.pos.x, pivot1.pos.y+L2/2, OffSet[2]), size=vec(5,L2,2), color=color.red)
#Link 3
Link3 = box(pos=vec(pivot2.pos.x, pivot2.pos.y+L3/2, OffSet[2]), size=vec(5,L3,2), color=color.white)

#---------------------------------------------#
# - Rotate                                    #
#---------------------------------------------#

#Angle set-up
Link1_Angle = 1.5708 - Theta1 
Link2_Angle = 1.5708 - (Theta1 + Theta2)
Link3_Angle = 1.5708 - (Theta1 + Theta2 + Theta3)

#Link1, Link2 and Link3 rotation
Link1.rotate(angle=Link1_Angle, axis=vec(0,0,-1), origin=vec(0,0, Link1.pos.z))
Link2.rotate(angle=Link2_Angle, axis=vec(0,0,-1), origin=vec(pivot1.pos.x, pivot1.pos.y, 0))
Link3.rotate(angle=Link3_Angle, axis=vec(0,0,-1), origin=vec(pivot2.pos.x, pivot2.pos.y, 0))
