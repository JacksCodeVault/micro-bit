from microbit import *
import radio

# Set up the radio group
radio.on()
radio.config(group=1)

# Send a message when button A is pressed
def on_button_pressed_a():
    radio.send("Micro Chat!")
button_a.was_pressed = on_button_pressed_a

# Main loop to listen for incoming messages
while True:
    incoming = radio.receive()
    if incoming:
        display.scroll(incoming)
