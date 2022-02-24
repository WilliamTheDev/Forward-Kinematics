import math

#Link Lengths
L1 = #length 1
L2 = #Length 2
L3 = #Length 3
#Angles
a1 = #Angle 1
a2 = #Angle 2
a3 = #Angle 3

#The Y position of {4}
def Y_axis_End(a1, a2, a3):
    y = L1 * math.cos(a1) + L2 * math.cos(a1 + a2) + L3 * math.cos(a1 + a2 + a3)
    return y

#The X postion of {4}
def X_axis_End(a1, a2, a3):
    x = L1 * math.sin(a1) + L2 * math.sin(a1 + a2) + L3 * math.sin(a1 + a2 + a3)
    return x

#The X postion of {2}
def X_axis_J1(a1):
    J1_axis_X = L1 * math.sin(a1)
    return J1_axis_X

#The Y postion of {2}
def Y_axis_J1(a1):
    J1_axis_Y = L1 * math.cos(a1)
    return J1_axis_Y

#The Y postion of {3}
def Y_axis_J2(a1, a2):
    J2_axis_Y = L1 * math.cos(a1) + L2 * math.cos(a1 + a2)
    return J2_axis_Y

#The X postion of {3}
def X_axis_J2(a1, a2):
    J2_axis_X = L1 * math.sin(a1) + L2 * math.sin(a1 + a2)
    return J2_axis_X

print("--- 3-axis Robotic Arm ---")
print("X - J1: ", X_axis_J1(a1))
print("Y - J1: ", Y_axis_J1(a1))
print("X - J2: ", X_axis_J2(a1, a2))
print("Y - J2: ", Y_axis_J2(a1, a2))
print("X - EP: ", X_axis_End(a1, a2, a3))
print("Y - EP: ", Y_axis_End(a1, a2, a3))
print("--------------------------")

