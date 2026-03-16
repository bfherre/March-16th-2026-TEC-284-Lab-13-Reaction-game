from gpiozero import LED, Button
from time import sleep
import random
led = LED(4)

right_button = Button(15, bounce_time=0.1)
left_button = Button(14, bounce_time=0.1)

playerOneScore = 0
playerTwoScore = 0

    
left_User = input("Enter username for Player 1: ")
right_User = input ("Enter username for player 2: ")


def pressed(button):
    global playerOneScore, playerTwoScore
    if button.pin.number == 14:
        print(left_User + ' pressed first')
        playerOneScore += 1
        print("Player 1 has " + str(playerOneScore))
        
        
    elif button.pin.number == 15:
        print(right_User + ' pressed first')
        playerTwoScore += 1
        print("Player 2 has " + str(playerTwoScore))
        
        led.off()
        if playerOneScore == 5:
            print(left_User + " wins!")
            exit()
        elif playerTwoScore == 5:
            print(right_User + " wins!")
            exit()
            
right_button.when_pressed = pressed
left_button.when_pressed =  pressed

while True:
            print("Get Ready...")
            sleep(random.randint(2,6))
            led.on()
            sleep(2)
            led.off()







    



    

    