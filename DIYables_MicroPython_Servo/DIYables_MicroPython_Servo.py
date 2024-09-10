"""
This MicroPython library is designed for any hardware plaform that supports MicroPython such as Raspberry Pi Pico, ESP32, Micro:bit... to make it easy to use with servo motor

It is created by DIYables to work with DIYables products, but also work with products from other brands. Please consider purchasing products from [DIYables Store on Amazon](https://amazon.com/diyables) from to support our work.

Product Link:
- Servo Motor: https://diyables.io/products/servo-motor-sg90-180-degree
- Sensor Kit: https://diyables.io/products/sensor-kit


Copyright (c) 2024, DIYables.io. All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

- Redistributions of source code must retain the above copyright
  notice, this list of conditions and the following disclaimer.

- Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.

- Neither the name of the DIYables.io nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY DIYABLES.IO "AS IS" AND ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL DIYABLES.IO BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""


from machine import Pin, PWM
import utime

class Servo:
    def __init__(self, pin_number, min_pulse=600, max_pulse=2450, frequency=50):
        """ Initialize a servo object on a specified pin with customizable pulse widths and frequency. """
        self.servo_pin = PWM(Pin(pin_number))  # Set up PWM on the pin
        self.servo_pin.freq(frequency)         # Set frequency, default is 50Hz
        self.min_pulse = min_pulse
        self.max_pulse = max_pulse
        self.cycle = 1 / frequency * 1000000     # PWM cycle in us

    def move_to_angle(self, angle):
        """ Move the servo to a specific angle. """
        # Calculate the pulse width corresponding to the angle
        pulse_width = self.min_pulse + (self.max_pulse - self.min_pulse) * angle / 180
        
        # Set the PWM duty cycle
        self.servo_pin.duty_u16(int(pulse_width * 65536 / self.cycle))  # Convert to duty for Pico's 16-bit resolution

    def deinit(self):
        """ Disable the PWM signal. """
        self.servo_pin.deinit()

    def __del__(self):
        """ Clean up the servo object when it's being destroyed. """
        self.deinit()

