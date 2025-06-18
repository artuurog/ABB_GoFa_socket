# ABB_GoFa_socket

Establish a communication between a real ABB robot (or RobotStudio simulation) and a custom node through socket.

A RAPID script is used to create a server, while the user node (e.g. Python script) acts as a client.
The client-server communication is setup through IP address and port number.

- Robotstudio simulation (virtual controller) + python node on the same PC:

    IP address 127.0.0.1\
    port 5000

- Real robot controller + python node:
  
    IP address: 192.168.125.1\
    port 1025

## Structure

- The `src` folder contains a RAPID module (.txt file) and a Python script
- The `envs` folder contains a RobotStudio environment for simulating a GoFa arm

## Disclaimer
The current configuration has been tested on:
- Robot: ABB 15000-5-95 GoFa 5kg
- Omnicore controller
- RobotWare version 7.12.0
- Python script executed in Spyder v6
- RobotStudio 2025

## Usage

Setup all the necessary modules. \In RobotStudio:
1. If needed, download and unpack the RobotStudio environment from `envs`
2. Go to `Controller` tab
3. Select `RAPID`
4. Create a new Program Module and paste the RAPID script (.txt file) from `src`
1. Click `RAPID` and `Apply`

Setup Python node:
1. Copy and paste the Python script and be ready to run it
2. Make sure you have ```Import socket ``` installed

In RobotStudio (or FlexPendant on real robot):
1. Set program pointer to ruotine by:
    1. Under `Controller/RAPID` tab
    1. Expand on `TCP_socket` module
    2. Right-click `main` and `Set Program Pointer to Routine` 


## Error troubleshooting

  ### `Socket Error` 

  ### `Robot Error`

## Contacts

## Citation
If you found this repo useful, please consider mentioning it in your work

<pre><code>
@misc{ABB_Gofa_socket_2025,
  author       = {Arturo Giacobbe},
  title        = {ABB GoFa socket},
  year         = 2025,
  howpublished = {\url{https://github.com/artuurog/ABB_GoFa_socket}},
}
</code></pre>

