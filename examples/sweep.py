"""
Product Link:
- Servo Motor: https://diyables.io/products/servo-motor-sg90-180-degree
- Sensor Kit: https://diyables.io/products/sensor-kit
"""

from DIYables_MicroPython_Servo import Servo
import utime

# Create a Servo object on GPIO28
servo = Servo(28)

# Attach the servo and prepare for sweeping
print("Servo attached and ready to sweep!")

# Main loop
while True:
    # Sweep from 0 degrees to 180 degrees
    for pos in range(0, 181):  # Goes from 0 degrees to 180 degrees
        servo.move_to_angle(pos)
        utime.sleep_ms(15)  # Wait 15 ms for the servo to reach the position

    # Sweep from 180 degrees back to 0 degrees
    for pos in range(180, -1, -1):  # Goes from 180 degrees to 0 degrees
        servo.move_to_angle(pos)
        utime.sleep_ms(15)  # Wait 15 ms for the servo to reach the position
