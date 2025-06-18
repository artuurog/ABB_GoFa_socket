# -*- coding: utf-8 -*-
"""
Establish a connection between the robot controller and this python node through TCP/IP socket.
A custom trajectory is streamed the robot controller. The robot will follow the trajectory.

Run this python node AFTER the RAPID module established the TCP server successfully


Robotstudio simulation (virtual controller) + python node on the same PC:
    IP address 127.0.0.1
    port 5000

Real robot controller + python node:
    IP address: 192.168.125.1
    port 1025

@author: arturo.giacobbe@polimi.it

"""

# Import socket module 
import socket                
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 1025
# port = 5000 
 
# connect to the server on local computer 
# s.connect(('127.0.0.1', port))
# print("Connecting...")

# Connect to real robot controller
try:
    s.connect(('192.168.125.1', port)) 
except:
    while True:
        if (s.connect(('192.168.125.1', port)) != True ):
            break
        print("trying to connect")
        
  
# Receive data from the server
data = s.recv(4096)
if data:
    print(data.decode())

data = s.recv(4096)
if data:
    print("Robot position:", data.decode())
        
    
#%% Send coordinates to robot controller - Single point

# Coordinates
pose = [-250, 0, 500, 0, 0, 0] # XYZ + 3 rotations


# Convert to string
pose_str = ",".join([str(x) for x in pose])

# Send
s.send(bytes(pose_str, 'utf-8'))

# Receive OK message from RAPID server
data= s.recv(4096)
if data:
    print("RAPID: ", data.decode())

s.close()    

#%% Trajectory (3 points)
    
pose = [[-250, 50, 500, 0, 0, 0],
        [-250, 250, 500, 0, 0, 0],
        [-250, 200, 700, 0, 0, 0]
        ]

for i in range(len(pose)):
    pose_str = ",".join([str(x) for x in pose[i]])
    
    # Send
    s.send(bytes(pose_str, 'utf-8'))
    
    # Receive OK message from RAPID server
    data= s.recv(4096)
    if data:
        print("RAPID: ", data.decode())
        
s.close()