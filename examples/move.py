"""
Product Link:
- Servo Motor: https://diyables.io/products/servo-motor-sg90-180-degree
- Sensor Kit: https://diyables.io/products/sensor-kit
"""

from DIYables_MicroPython_Servo import Servo
import utime

# Create a Servo object on GPIO28
servo = Servo(28)

# Move servo to different angles
servo.move_to_angle(0)
utime.sleep(2)
servo.move_to_angle(90)
utime.sleep(2)
servo.move_to_angle(180)
utime.sleep(2)

# Clean up
servo.deinit()
