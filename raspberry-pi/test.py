#type: ignore
import adafruit_mpu6050 as imu
import board
import time
import busio

sda_pin = board.GP2
scl_pin = board.GP3
i2c = busio.I2C(scl_pin, sda_pin)
mpu = imu.MPU6050(i2c, address = 0x68)

while True:

    print(f"X acceleration: {mpu.acceleration[0]} m/s2") #print XYZ vals
    print(f"Y acceleration: {mpu.acceleration[1]} m/s2")
    print(f"Z acceleration: {mpu.acceleration[2]} m/s2")
    print("")
    time.sleep(.1)
    
    if mpu.acceleration[0] >= 1: 
        print("Tilting Right")

    if mpu.acceleration[0] <= -1: 
        print("Tilting Left")
    
    if mpu.acceleration[1] <= -1: 
        print("Tilting Back")

    if mpu.acceleration[1] >= 1: 
        print("Tilting Forward")
    
    else:
        print("Level")

