# ABB GoFa socket

Establish a connection between a real ABB robot (or RobotStudio simulation) and a custom (python) node through socket communication.

A RAPID module is used to create a server, while the user node (e.g. Python script) acts as a client.
The client-server communication is setup through IP address and port number.

- Robotstudio simulation (virtual controller) + python node on the same PC:

    IP address 127.0.0.1\
    port 5000

- Real robot controller + python node:
  
    IP address: 192.168.125.1\
    port 1025

  The IP address and port number must match in both Python node and RAPID module in RobotStudio.

## Structure

- The `src` folder contains a RAPID module (.txt file) and a Python script
- The `envs` folder contains a RobotStudio environment for simulating a GoFa arm with a virtual controller

## Disclaimer
The current configuration has been tested on:
- Robot: ABB 15000-5-95 GoFa 5kg
- Omnicore controller
- RobotWare version 7.12.0
- Python script executed in Spyder v6
- RobotStudio 2025

## Usage

Setup all the necessary modules.
1. If needed, download and unpack the RobotStudio environment from `envs`

In RobotStudio:
1. Go to `Controller` tab
1. Expand `RAPID` from the dropdown menu on the left 
1. Create a new Program Module and paste the RAPID script (.txt file) from `src`
1. Click `RAPID` and `Apply`

Setup Python node:
1. Copy and paste the Python script and be ready to run it
2. Make sure you have installed the ```socket``` python library

In RobotStudio (or FlexPendant for the real controller):
1. Set Program Pointer to `main` ruotine:
    1. Go to `Controller/RAPID` tab
    1. Expand `TCP_socket` module
    2. Right-click `main` routine and `Set Program Pointer to Routine`
1. If running a simulation (virtual controller)
    1. Go to `Simulation` tab and press `Play`
    2. The robot will move to a predefined home position and start the socket server
1. If running on real robot
    1. Connect to robot controller via MGMT port 
    1. Go to the `Code` app on the FlexPendant
    1. Make sure Program Pointer is set to  `TCP_socket`
    1. Press play button
    1. The robot will move to a predefined home position and start the socket server

Once the RAPID module is running, start the Python node to establish connection.

## Error troubleshooting

  ### `Socket Error` 
  - Make sure that the IP address and port number match both in the python node and RAPID module
  - RobotStudio returns a socket error even if the socket connection is closed by the client node
  - To reset the error, set the Program Pointer back to the routine in RobotStudio

  ### `Robot Error`
  Make sure that the trajectory is feasible to follow for the robot:
  - There are no parallel consecutive joints
  - The robot does not pass through a singular configuration

  ### `Firewall settings in RobotStudio`
  Make sure that Rapid sockets are not blocked by the Firewall Manager in RobotStudio. To enable Rapid socket:
  1. Go to `Controller` > click `Configuration` > `Communication`
  2. Select `Firewall Manager`
  3. Double click on `RapidSockets` and set all the values to `Yes`
  4. Restart the controller


## Contacts

For questions, suggestions or contributions, feel free to contact:

- **Arturo Giacobbe** – [arturo.giacobbe@polimi.it](mailto:arturo.giacobbe@polimi.it)


## Citation
If you found this repo useful, please consider mentioning it in your work

<pre><code>
@misc{ABB_Gofa_socket_2025,
  author       = {Arturo Giacobbe},
  title        = {ABB GoFa socket},
  year         = 2025,
  url          = {https://github.com/artuurog/ABB_GoFa_socket},
}
</code></pre>

