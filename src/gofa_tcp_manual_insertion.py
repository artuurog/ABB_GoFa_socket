# -*- coding: utf-8 -*-
"""
Establish a connection between the robot controller and this python node through TCP/IP socket.
The user is asked to give a position and gripper opening. The robot will then move to that pose.

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
        
    
        
#%% User inserts values

pose = []

while True:
    x = input('x = ')
    y = input('y = ')
    z = input('z = ')
    q1 = input('q1 = ')
    q2 = input('q2 = ')
    q3 = input('q3 = ')
    gripper_open = input('Open gripper [0,1] = ')
    
    # Fill in pose values
    pose = [x,y,z,q1,q2,q3]
    
    # Convert to string before sending
    pose_str = ",".join([str(x) for x in pose])
    
    # Send position
    s.send(bytes(pose_str, 'utf-8'))
    
    # Receive OK message from RAPID server
    data= s.recv(4096)
    if data:
        print("RAPID: ", data.decode())
    
    # Send gripper signal
    s.send(bytes(str(gripper_open), 'utf-8'))
    
    # Receive OK message from RAPID server
    data= s.recv(4096)
    if data:
        print("RAPID: ", data.decode())

 
        
#%% Close connection
s.close()