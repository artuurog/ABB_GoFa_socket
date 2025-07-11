# -*- coding: utf-8 -*-
"""
Establish a connection between the robot controller and this python node through TCP/IP socket.
Use the keyboard of your PC to jog the GoFa.

Run this python node AFTER the RAPID module established the TCP server successfully


Robotstudio simulation (virtual controller) + python node on the same PC:
    IP address 127.0.0.1
    port 5000

Real robot controller + python node:
    IP address: 192.168.125.1
    port 1025

@author: arturo.giacobbe@polimi.it

"""

import socket  
from pynput import keyboard
    
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 1025 # real controller
# port = 5000  # sim controller
 
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
    pose = data.decode()
    pose = [float(x.strip()) for x in pose.split(',')]
    x,y,z = pose
    print("Robot position:", pose)
 
data = s.recv(4096)
if data:
    gripper_open = int(data.decode())
    print("Gripper open:", gripper_open)       
    
        
#%% Keyboard input

delta = 20

def on_press(key):
    
    global x, y, z, gripper_open
    
    if key == keyboard.Key.left:
        print('Increase Y...')
        y += delta
                                            
    if key == keyboard.Key.right:
        print('Decrease Y...')
        y -= delta
        
    if key == keyboard.Key.up:
        print('Increase X...')
        x += delta
        
    if key == keyboard.Key.down:
        print('Decrease X...')
        x -= delta
        
    if key == keyboard.Key.shift_r:
        print('Move UP...')
        z += delta
        
    if key == keyboard.Key.ctrl_r:
        print('Move DOWN...')
        z -= delta
        
    if key == keyboard.Key.tab:
        print('Gripper...')
        if gripper_open == 1:
            gripper_open = 0
        else:
            gripper_open = 1
         
    # Stop listener
    if key == keyboard.Key.esc:
        s.close()
        return False 
    
    return False


while True:
    
    #pose = []
    # data = s.recv(4096)
    # if data:
    #     pose = data.decode()
    #     pose = [float(x.strip()) for x in pose.split(',')]
    #     x,y,z = pose
    #     print("Robot position:", pose)
     
    # data = s.recv(4096)
    # if data:
    #     gripper_open = int(data.decode())
    #     print("Gripper open:", gripper_open)
    
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
        
        
    # Convert to string before sending
    # pose_str = ",".join([str(x) for x in pose])
    pose_str = f"{x},{y},{z},0,0,0"
    
    output = f"{pose_str}, {gripper_open}"
    
    s.send(bytes(output, 'utf-8'))
    
    # Send position
    # s.send(bytes(pose_str, 'utf-8'))
    
    # Receive OK message from RAPID server
    # data= s.recv(4096)
    # if data:
    #     print("RAPID: ", data.decode())
    
    # # Send gripper signal
    # s.send(bytes(str(gripper_open), 'utf-8'))
    
    # # Receive OK message from RAPID server
    # data= s.recv(4096)
    # if data:
    #     print("RAPID: ", data.decode())

    # Receive OK message from RAPID server
    # data= s.recv(4096)
    # if data:
    #     print("RAPID: ", data.decode())
       
#%% Close connection
s.close()