import math

#3-Axis Robotic Arm | Foward-Kinematics

#Modelling the motion of a 3-axis robotic arm. To use this program 
#you will need to know the initial conditions of the robotic arm. 
#These conditions are the following:

#Link Lengths
L1 = 0 #Link 1 Length
L2 = 0 #Link 2 Length
L3 = 0 #Link

#Angles | Degress to radians
Theta1 = 0 * math.pi/180#joint Angle 1 
Theta2 = 0 * math.pi/180#joint Angle 2
Theta3 = 0 * math.pi/180#joint Angle 3 
Theta4 = 0 * math.pi/180#Z Angle 4

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

End_Effector = End_Frame()
J2 = Joint_2()
J3 = Joint_3()

#Output Data
print("--- Foward Kinematics ---")
print("Joint 2 X: ")
print(J2[0])
print("Joint 2 Y: ")
print(J2[1])
print("Joint 3 X: ")
print(J3[0])
print("Joint 3 Y: ")
print(J3[1])
print("End Effector X: ")
print(End_Effector[0])
print("End Effector Y: ")
print(End_Effector[1])
print("Tool Head Orientation: ")
print((Theta1 * 180/math.pi) + (Theta2 * 180/math.pi) + (Theta3 * 180/math.pi))
print("-------------------------")
