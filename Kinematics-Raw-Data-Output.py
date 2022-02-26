import math

#3-Axis Robotic Arm | Foward-Kinematics

#Modelling the motion of a 3-axis robotic arm. To use this program 
#you will need to know the initial conditions of the robotic arm. 
#These conditions are the following:

#Link Lengths
L1 = 0
L2 = 0
L3 = 0

#Angles | Degress to radians
Theta1 = 0 * math.pi/180 #joint Angle 1 
Theta2 = 0 * math.pi/180 #joint Angle 2
Theta3 = 0 * math.pi/180 #joint Angle 3 
Theta4 = 0 * math.pi/180 #Z Angle 4

# - W!lliam - 2022 | WilliamTheDev On Github

def Joint_2(): #Joint One Position (X, Y)
    J2 = [ L1 * math.cos(Theta1), L1 * math.sin(Theta1)]
    return J2

def Joint_3(): #Joint Two Position (X, Y)
    J3 = [L1 * math.cos(Theta1) + L2 * math.cos(Theta1 + Theta2),
          L2 * math.sin(Theta1) + L2 * math.cos(Theta1 + Theta2)]
    return J3

def End_Frame(): #Joint Three Position (X, Y)
    End = [L1 * math.cos(Theta1) + L2 * math.cos(Theta1 + Theta2) + L3 * math.cos(Theta1 + Theta2 + Theta3), 
           L1 * math.sin(Theta1) + L2 * math.sin(Theta1 + Theta2) + L3 * math.sin(Theta1 + Theta2 + Theta3)]
    return End

def Z_Joint_1(): #Experimental (Z, X) | I have not fully tested this formula for Z
    End = End_Frame()
    Z= [End[0] * math.cos(Theta4), End[1] * math.sin(Theta4)]
    return Z

print("--- Foward Kinematics ---")
print("Joint 2 | X, Y: ")
print(Joint_2())
print("Joint 3 | X, Y : ")
print(Joint_3())
print("End Position | X, Y: ")
print(End_Frame()) 
print("Z_Joint_1 | Z, X: ")
print(Z_Joint_1())
print("Tool Head: ")
print((Theta1 * 180/math.pi) + (Theta2 * 180/math.pi) + (Theta3 * 180/math.pi))
print("-------------------------")
