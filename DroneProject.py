from djitellopy import tello
# Imports the needed functions for the drone to maneuver
from time import sleep

# Names and connects the drone to the code
tello = tello.Tello()
tello.connect()

# Allows the drone to stream video as it flies around the room
tello.streamon()

# Begins the sequence to lift the drone up the initial 80 centimeters
tello.takeoff()

# Moves the drone up 100 centimeters to a safe height
tello.move_up(100)
sleep(.5)

# Moves the drone the first 850 centimeters lengthwise across the room
tello.move_forward(500)
tello.moveforward(350)
sleep(.5)

# Turns the drone 90 degrees to the left and moves it 400 centimeters width-wise across the room
tello.rotate_counter_clockwise(90)
sleep(.5)

tello.move_forward(400)
sleep(.5)

tello.rotate_counter_clockwise(90)
sleep(.5)

tello.moveforward(500)
tello.move_forward(350)
sleep(.5)

tello.rotate_counter_clockwise(90)
sleep(.5)

tello.move_forward(400)
sleep(.5)

# Initializes the landing sequence on the drone
tello.land()

# Ends the drone's live video feed
tello.streamoff()
