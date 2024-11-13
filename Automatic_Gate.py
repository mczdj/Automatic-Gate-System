#import cv2
#import numpy as np
#from imutils.viedo import VideoSteam
#from Imutils import resize
import time
import random
from tkgpio import TkCircuit
from gpiozero import AngularServo, LED, DistanceSensor
from enum import Enum

# Configuration of the circuit
configuration = {
    "width": 1000,
    "height": 500,
    "sensors": [{"x": 250, "y": 300, "name": "DistanceSensor", "trigger_pin": 23, "echo_pin": 24}],
    "servos": [{"x": 150, "y": 200, "name": "DoorServo", "pin": 17, "min_angle": 0, "max_angle": 180, "initial_angle": 0}],
    "leds": [{"x": 50, "y": 50, "name": "GateClosedLed", "pin": 19}, {"x": 150, "y": 50, "name": "GateOpenLed", "pin": 20}],
}

# Print the configuration for debugging
print("Configuration:", configuration)

# Initialize the TkCircuit
circuit = TkCircuit(configuration)

@circuit.run
def main():
    class DoorState(Enum):
        OnEntryClosed = 0
        OnStayClosed = 1
        OnEntryOpening= 2
        OnStayOpening =3
        OnEntryOpen =4
        OnStayOpen = 5
        OnStayClosing = 6
        OnEntryClosing = 7
    # video_stream = VideoStream(src=0).start()
    #diff_threshold = 10000
    #initial_frame = video_stream.read()

    # Initialize hardware components
    door_servo = AngularServo(17, min_angle=0, max_angle=180)
    gate_open_led = LED(20)
    gate_closed_led = LED(19)
    #sensor = DistanceSensor(echo=2, trigger=3)

    current_state = DoorState.OnEntryClosed

    def get_distance():
        # Simulate distance measurement with a random value between 0 and 5 meters
        return random.uniform(0, 5)

    while True:
        print(f"Current State: {current_state.name}")
        distance_value = get_distance()  # Use the simulated distance

        if current_state == DoorState.OnEntryClosed:
            print(f"Distance: {distance_value:.2f} meters")
            gate_closed_led.off()      # Turn on the closed LED
            gate_open_led.off()       # Turn off the open LED
            door_servo.angle = 0      # Door is closed
            current_state = DoorState.OnStayClosed

        elif current_state == DoorState.OnStayClosed:
            time.sleep(2)
            # new Frame = video_stream.read()
            # frame diff = cv2.absdiff(initial_frame, new frame)
            # diff_score =np.sum(diff)
            #if sensor.distance & diff_score > diff_threshold:
            if distance_value < 2:    # Condition to open Gate.
                print(f"Distance: {distance_value:.2f} meters")
                current_state = DoorState.OnEntryOpening
        elif current_state == DoorState.OnEntryOpening:
            gate_closed_led.off()
            gate_open_led.on()
            door_servo.angle = 90
            print(f"Distance: {distance_value:.2f} meters")
            current_state = DoorState.OnStayOpening
        elif current_state == DoorState.OnStayOpening:
            gate_closed_led.off()
            gate_open_led.on()
            time.sleep(3)
            print(f"Distance: {distance_value:.2f} meters")
            current_state = DoorState.OnEntryOpen
        elif current_state == DoorState.OnEntryOpen:
            gate_open_led.off()
            gate_closed_led.off()
            door_servo.angle = 180
            print(f"Distance: {distance_value:.2f} meters")
            current_state = DoorState.OnStayOpen
        elif current_state == DoorState.OnStayOpen:
            # new_Frame = video_stream.read()
            # frame_diff = cv2.absdiff(initial_frame, new frame)
            # diff_score = np.sum(frame_diff)
            # if sensor.distance & diff_score > diff_threshold:
            if distance_value > 2:
                print(f"Distance: {distance_value:.2f} meters")
                current_state = DoorState.OnStayOpen
            time.sleep(10)
            current_state = DoorState.OnEntryClosing
        elif current_state == DoorState.OnEntryClosing:
            gate_closed_led.on()
            gate_open_led.off()
            door_servo.angle = 90
            current_state = DoorState.OnStayClosing
        elif current_state == DoorState.OnStayClosing:
            gate_closed_led.on()
            gate_open_led.off()
            # new_Frame = video_stream.read()
            # frame_diff = cv2.absdiff(initial_frame, new frame)
            # diff_score = np.sum(frame_diff)
            # if sensor.distance & diff_score > diff_threshold:
            if distance_value > 2:
                print(f"Distance: {distance_value:.2f} meters")
                current_state = DoorState.OnStayOpen
            time.sleep(3)
            current_state = DoorState.OnEntryClosed

        time.sleep(0.1)  # Small delay for CPU relief