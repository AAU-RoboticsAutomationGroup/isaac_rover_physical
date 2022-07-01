from adafruit_pca9685 import PCA9685
from board import SCL, SDA
import busio
import time
import sys

'''
This script simply stops all the motors, in case they were left in a running state. 
'''
i2c_bus = busio.I2C(SCL, SDA)

pwm = PCA9685(i2c_bus)
# For most motors a pwm frequency of 50Hz is normal
pwm_frequency = 50.0  # Hz
pwm.frequency = pwm_frequency

for pin_number in range(16):
    pwm.channels[pin_number].duty_cycle = 0
