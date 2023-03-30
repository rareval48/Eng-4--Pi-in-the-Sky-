# Pi_in_the_Sky

# Table of Contents

* [Schedule](#Schedule)
* [Designing](#Designing)
* [Functionablility and Materials](#Functionablility_and_Materials)
* [Weekly Progress](#Weekly_Progress)

# Schedule
We must follow the schedule to a t for us to complete this by the end of the school year. WE first start working on our project just after Christmas break. 

From Janurary to End of Q2 - We finish initial CAD and code

From Q2 to March - We create a functional prototype

All through out March - We will do design refinement and final tweaks

All thorough out April - We make sure the drone launches and collects data

From May to when the drone is due - We analyze data that the drone collected and finish documentation of the drone

If needed after the due date we will have emergency project work time if we didnt finish


# Designing

## Initial Design
Our initial plan is to make a nuke shaped device that wil be launched and protect the ascent and decent of the raspberry pi. We also ended up making a onshape design so that we were able to compare it to all the components that we needed.
Initial design and reference picture:

<img src="https://user-images.githubusercontent.com/71342195/204313376-51ca5328-9db9-49df-b2a6-f57427667dd3.png" width="300px"><img src="https://user-images.githubusercontent.com/71342195/204315696-83aefc91-d7c2-400f-9384-0ba7efb19afa.png" width="200px"><img src="https://user-images.githubusercontent.com/71342195/204319456-e632d12b-2841-421b-b828-0732915cac08.png" width="400px">

## ReDesign
We ended up changing our design to a drone. As we are able to make our own circuitboard and we would be able to cut down on weight. It would also cut down on materials used as there was an excess use of ABP.
Here is our reference for a drone next to our initial design for our drone:

<img src="https://user-images.githubusercontent.com/71342195/204837447-9a0223bd-9544-4fe0-9009-91eb4449f9eb.png" width="400px"><img src="https://user-images.githubusercontent.com/71342195/206731486-579a0617-027c-4520-9d6a-464589515d7d.png" width="400px">

# Functionablility_and_Materials

## Functionability
Our plan to control this drone is to just let all of the motors go at full speed till we reach a certain height then turn them off. If we have time then we can change it so that mototrs rpm is slowly reduced till landing but first we have to make the drone work. 

Example of initial code: 

```python
# type: ignore
import adafruit_mpu6050 as imu
import busio
import board
import time
import pulseio
from pwmio import PWMOut
from digitalio import DigitalInOut, Direction, Pull
from adafruit_motor import motor as Motor

sdaPin = board.GP2  # defining the SDA & SCL pins to use
sclPin = board.GP3
i2c = busio.I2C(sdaPin, sclPin)
mpu = imu.MPU6050(i2c) 

reverse_ain1 = PWMOut(board.GP8, frequency=50)
reverse_ain2 = PWMOut(board.GP9, frequency=50)
reverse_bin1 = PWMOut(board.GP11, frequency=50)
reverse_bin2 = PWMOut(board.GP10, frequency=50)

forward_ain1 = PWMOut(board.GP12, frequency=50)
forward_ain2 = PWMOut(board.GP13, frequency=50)
forward_bin1 = PWMOut(board.GP14, frequency=50)
forward_bin2 = PWMOut(board.GP15, frequency=50)


motor_a = Motor.DCMotor(forward_ain1, forward_ain2)
motor_b = Motor.DCMotor(forward_bin1, forward_bin2)
motor_c = Motor.DCMotor(reverse_ain1, reverse_ain2)
motor_d = Motor.DCMotor(reverse_bin1, reverse_bin2)

def basic_operations():  # Drive forward at full throttle
    motor_a.throttle = 1.0
    motor_b.throttle = 1.0
    motor_c.throttle = 1.0
    motor_d.throttle = 1.0

while True:
    basic_operations() 

    accelerationVals = mpu.acceleration
    
    print(f"X acceleration: {accelerationVals[0]} m/s2")
    print(f"Y acceleration: {accelerationVals[1]} m/s2")
    print(f"Z acceleration: {accelerationVals[2]} m/s2")
    print("")
    time.sleep(.1)
```



## Risk Mitigation
There isnt much risk involving drones since there isnt any presssure, liquids, or harsh chemicals. The only thing that we would need to watch out for would be the drone blades as there isnt much stopping it from protecting the surroundings. To protect us from the blades we would need to make sure that we arent touching the drone when it takes off or if the blades are spinning at all.

## Materials
Some of the materials and supplies that we need are easy to ge as we have them here in the lab. The other supplies would need to be ordered. Here is a list of all of our supplies include: 4 dc coreless motors, circuitboard, accelerometer (MPU6050), battery pack, altimeter (MPL3115A2), GPS module, 2 H-bridges, a powerboost, and 3d printed/lasercut supplies. We would need to buy 4 dc motors and a GPS module. As those are the only things that we dont have in the lab.

# Weekly_Progress

## Week 1/9-1/13
This week we ended up redesigning our drone again. Picture provided below. Another big thing that we started working on is wiring the parts to see if the code will work. Most of the code that I have already was copy and pasted from my other working projects, its easier to do that then rewrite code, so you know for certain that it works.

<img src="https://user-images.githubusercontent.com/71342195/212105444-89988bfd-3ccd-4660-9d69-df616c82ad5c.png" width="400px">

## Week 1/17-1/20
A four day week really didnt help on our progress as we lost a day that we counld be working. But the days that we were here Spencer re laser cut parts of our drone that were susceptible to breaking from small drops. I've been trying to find information on how to store data on the Raspberry Pi Pico for most of the week. 

## Week 1/24-1/27
There hasnt been much progress finnding code for writing, storing, and finding data on the Pico. Stil looking for instructions on how to do that. But Spencer finally perfected the drones stability after multiple lasercuts and hopefully it wont break in the future. . 

## Week 1/30-2/3
We finished soldering all the connections to the board. We also made sure that all connectiuons that we did were in the right position so we didnt have to go back and redo them. The drone motors arrived. So we are waiting for the motor holders to finish printing so that we can finish connecting the motors.
At the end of the week we finished wiring and soldering wires and making sure the connections wouldnt break. We alos had to do some modifications to the feet of the drone. As they hold the motors and the holes are to big for the motors.

## Week 2/6-2/10
We finished soldering and realized that the code wouldnt work, so we found out that the the pins for the SDA and SCL were soldered switched on the board. We also had to reprint the drone to cut down on weight and the bottom broke, so it was essential that we fixed this before anything else.

<img src="https://user-images.githubusercontent.com/71342195/219695007-0a3584ba-20c4-4939-86a7-fe209d7ba3c0.png" width="400px">

## Week 2/13-2/17
For our project we are making a drone, as well as a couple of other groups. One of the groups is farther ahead and found out that the battery doesnt put out enough amps for the drone to take off. So we have to add some transisters for the drone to take off as the new battery would fry the h-bridges if we tried to use it.

Wiring diagram:

<img src="https://user-images.githubusercontent.com/71342195/219696356-3a3c486c-faac-4738-a780-41d5bb058faa.png" width="400px">

## Week 2/20-2/24
We finished our initial code and learned that we have to use a Tello battery so that all 4 motors. We also started redesigning our drone body as our current one was really heavy and 3d prining a redesign would help the drone lift off and the acceleration and deacceleration of the drone.

## Week 2/27-3/3
We didnt really do much besides keep redesigning our drone and making our code work together. One big thing we learned was for turning on our drone motors with an (if) statement we need a print("") statement to make sure that the loop keeps looping.

## Week 3/6-3/10
We finished designing our drone and are 3d printing it out. We have also had some problems with VSCode and the run button not working properly. We also ran into problems with the pico connecting to the computer.

<img src="https://user-images.githubusercontent.com/71342195/224726724-63f23845-b767-4141-8475-70b03d2afd4e.png" width="400px">

## Week 3/13-3/17
We learned that any other mosfet besides IRLB8721 cannot control the current the drone needs to fly. Fortunately we found some more and were able to make more power on the motors.

## Week 3/20-3/24 
SPENCER BROKE THE DRONE. We have to reprint with better structures for support to make sure taht the drone doesnt break again. We also edited the diameter for the motor holes. As there was to much room for the drone motors. We also have a basic code setup for the drone to use without transistors. 
Example Below:

```python
#type: ignore
import adafruit_mpu6050 as imu
import board
import time
import busio
import pwmio

sda_pin = board.GP4
scl_pin = board.GP5
i2c = busio.I2C(scl_pin, sda_pin)
mpu = imu.MPU6050(i2c, address = 0x68)

CraigJr = 100

motor1_r = pwmio.PWMOut(board.GP17, frequency=CraigJr)
motor2_f = pwmio.PWMOut(board.GP18, frequency=CraigJr)
motor3_r = pwmio.PWMOut(board.GP19, frequency=CraigJr)
motor4_f = pwmio.PWMOut(board.GP20, frequency=CraigJr)
while True:

    print(f"X: {mpu.acceleration[0]} m/s2") #print XYZ vals
    print(f"Y: {mpu.acceleration[1]} m/s2")
    print(f"Z: {mpu.acceleration[2]} m/s2")
    print("")
    time.sleep(.1)

    if mpu.acceleration[0] >= 1: 
        print("Tilting Back")
        motor1_r.duty_cycle = 65535 // 2
        motor2_f.duty_cycle = 65535
        motor3_r.duty_cycle = 65535 // 2
        motor4_f.duty_cycle = 65535

    else:
        print("Level")
        motor1_r.duty_cycle = 65535
        motor2_f.duty_cycle = 65535
        motor3_r.duty_cycle = 65535
        motor4_f.duty_cycle = 65535
    
    if mpu.acceleration[0] <= -1: 
        print("Tilting Forward")
        motor1_r.duty_cycle = 65535 
        motor2_f.duty_cycle = 65535 // 2 
        motor3_r.duty_cycle = 65535
        motor4_f.duty_cycle = 65535 // 2

    else:
        print("Level")
        motor1_r.duty_cycle = 65535
        motor2_f.duty_cycle = 65535
        motor3_r.duty_cycle = 65535
        motor4_f.duty_cycle = 65535

    if mpu.acceleration[1] <= -1: 
        print("Tilting left")
        motor1_r.duty_cycle = 65535 // 2
        motor2_f.duty_cycle = 65535 // 2
        motor3_r.duty_cycle = 65535
        motor4_f.duty_cycle = 65535

    else:
        print("Level")
        motor1_r.duty_cycle = 65535
        motor2_f.duty_cycle = 65535
        motor3_r.duty_cycle = 65535
        motor4_f.duty_cycle = 65535

    if mpu.acceleration[1] >= 1: 
        print("Tilting right")
        motor1_r.duty_cycle = 65535
        motor2_f.duty_cycle = 65535
        motor3_r.duty_cycle = 65535 // 2
        motor4_f.duty_cycle = 65535 // 2

    else:
        print("Level")
        motor1_r.duty_cycle = 65535
        motor2_f.duty_cycle = 65535
        motor3_r.duty_cycle = 65535
        motor4_f.duty_cycle = 65535
```

## Week 3/27-3/30
Our drone is coming together really well. Here is a progress photo. I did accidentally fry a board, while wiring the board I didnt cover the connections that connected the battery to the motors, so I think by not covering those connections they touched the board and added voltage to a component to something that didnt need voltage.

<img src="https://user-images.githubusercontent.com/71342195/228573203-8aea49ba-d59e-4102-983b-83c445132d9e.jpg" width="500px">
