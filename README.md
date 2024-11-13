# Simulated Gate Control System with TkCircuit

This project demonstrates a simulated gate control system, which is designed to operate using an ultrasonic sensor and camera for distance measurement and motion detection. However, in this simulation, a random number generator is used to mimic the distance sensor.

---

## Features
- **Simulated Hardware**: Includes LEDs, Servo Motor, and Distance Sensor using TkCircuit.
- **State Machine**: Implements a comprehensive state machine to manage gate operations.
- **Randomized Distance Simulation**: Simulates distance measurement using a random number generator.
- **Gate Control**: Automatically opens or closes the gate based on distance.

---

## Components Used
This simulation uses the following components via `TkCircuit`:
1. **Distance Sensor**: Simulates an ultrasonic sensor using random numbers.
2. **Servo Motor**: Controls the gate's movement.
3. **LEDs**:
   - Gate Closed LED (Pin 19)
   - Gate Open LED (Pin 20)

---

## Circuit Configuration
The TkCircuit configuration is as follows:
```python
configuration = {
    "width": 1000,
    "height": 500,
    "sensors": [{"x": 250, "y": 300, "name": "DistanceSensor", "trigger_pin": 23, "echo_pin": 24}],
    "servos": [{"x": 150, "y": 200, "name": "DoorServo", "pin": 17, "min_angle": 0, "max_angle": 180, "initial_angle": 0}],
    "leds": [{"x": 50, "y": 50, "name": "GateClosedLed", "pin": 19}, {"x": 150, "y": 50, "name": "GateOpenLed", "pin": 20}],
}
