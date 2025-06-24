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
#port = 1025 # real controller
port = 5000  # sim controller
 
# connect to the server on local computer 
s.connect(('127.0.0.1', port))
print("Connecting...")

# Connect to real robot controller
# try:
#     s.connect(('192.168.125.1', port)) 
# except:
#     while True:
#         if (s.connect(('192.168.125.1', port)) != True ):
#             break
#         print("trying to connect")
        
  
# Receive data from the server
data = s.recv(4096)
if data:
    print(data.decode())

data = s.recv(4096)
if data:
    print("Robot position:", data.decode())
        
    

#%% Trajectory (N points)
    
pose = [[-400, 60, 400, 0, 0, 0],
        [-400, 250, 400, 0, 0, 0],
        [-400, 200, 700, 0, 0, 0],
        [-400, 60, 700, 0, 0, 0],
        [-400, 60, 400, 0, 0, 0]
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
