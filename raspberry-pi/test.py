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

FREQ = 1000

motor1_f = pwmio.PWMOut(board.GP18, frequency=FREQ)
motor2_f = pwmio.PWMOut(board.GP19, frequency=FREQ)

while True:

    First = f"Angular Velocities`:"
    Second = f"x velocty: {round(mpu.acceleration[0], 1)}"  # round decimals to the 3rd decimal place
    Third = f"y velocity: {round(mpu.acceleration[1], 1)}"
    Fourth = f"z velocity: {round(mpu.acceleration[2], 1)}"

    print(f"X acceleration: {mpu.acceleration[0]} m/s2") #print XYZ vals
    print(f"Y acceleration: {mpu.acceleration[1]} m/s2")
    print(f"Z acceleration: {mpu.acceleration[2]} m/s2")
    print("")
    time.sleep(.1)
    
    if mpu.acceleration[0] <= .3: 
        print("Level")
    
    if mpu.acceleration[0] >= 1: 
        print("Tilting Right")

    if mpu.acceleration[0] >= -1 <= 0: 
        print("Tilting Left")
    
    if mpu.acceleration[1] <= -1: 
        print("Tilting Back")

    if mpu.acceleration[1] >= 1: 
        print("Tilting Forward")