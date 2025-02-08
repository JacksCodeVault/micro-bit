from microbit import *
import radio

# Set up the radio group
radio.on()
radio.config(group=1)  # Default group is 1

# Send specific messages based on button presses
def on_button_pressed_a():
    radio.send("Hello from A!")
    display.scroll("A Sent!")

def on_button_pressed_b():
    radio.send("Hello from B!")
    display.scroll("B Sent!")

def on_button_pressed_ab():
    radio.config(group=5)  # Switch to a secret group
    radio.send("Secret Message!")
    display.scroll("Secret Sent!")

# Main loop to listen for incoming messages
while True:
    if button_a.was_pressed():
        on_button_pressed_a()
    if button_b.was_pressed():
        on_button_pressed_b()
    if button_a.is_pressed() and button_b.is_pressed():
        on_button_pressed_ab()
        
    # Listen for incoming messages
    incoming = radio.receive()
    if incoming:
        display.scroll(incoming)
