__author__ = 'srkiyengar'

import pygame
import screen_print as sp
import reflex
import time



METHOD = 1


# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

SCAN_RATE = 20                    #1 (one) second divided by scan rate is the loop checking if the main program should stop



class gripper():

    def __init__(self):

        pygame.init()
        # Set the width and height of the screen [width,height]
        size = [500, 700]
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Reflex_SF JoyStick Movements")

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        # for print in Pygame screen object
        textPrint = sp.TextPrint()

        my_key_controller = reflex.key_reflex_controller()

        calibrate = False


        key_ring={}
        key_ring['301']= 0  # 301 is Caps lock. This will be displayed in the screen  Caps lock = 1 + keys are the command set
        key_pressed = 0     # key press and release will happen one after another
        key_released = 0

        file_ring={}        # to make sure we close any file created only if it is not closed

        method = METHOD

        # Calibration
        while calibrate is False:
            screen.fill(WHITE)
            textPrint.reset()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    key_pressed = event.key
                    print("Key Ascii Value {} Pressed".format(key_pressed))
                    key_ring[str(key_pressed)] = 1
                    if key_ring['301'] == 1:    # Caps lock is 1
                        if my_key_controller.set_key_press(key_pressed) == 1:
                            calibrate = True
                elif event.type == pygame.KEYUP:
                    key_released = event.key
                    print("Key Ascii Value {} Released".format(key_released))
                    key_ring[str(key_released)] = 0
                else:
                    pass # ignoring other non-logitech joystick event types

            textPrint.Screenprint(screen, "Caps Lock should be 1 to accept any of the keys")
            textPrint.Yspace()
            textPrint.Yspace()
            textPrint.Screenprint(screen,"Caps Lock Key set to {}".format(key_ring['301']))
            textPrint.Yspace()
            textPrint.Screenprint(screen, "Finger 1 - Press 'q' to move up")
            textPrint.Yspace()
            textPrint.Screenprint(screen, "Finger 1 - Press 'a' to move down")
            textPrint.Yspace()
            textPrint.Screenprint(screen, "Finger 2 - Press 'w' to move up")
            textPrint.Yspace()
            textPrint.Screenprint(screen, "Finger 2 - Press 's' to move down")
            textPrint.Yspace()
            textPrint.Screenprint(screen, "Finger 3 - Press 'e' to move up")
            textPrint.Yspace()
            textPrint.Screenprint(screen, "Finger 3 - Press 'd' to move down")
            textPrint.Yspace()
            textPrint.Screenprint(screen, "Pre Shape - Press 'r' to move closer")
            textPrint.Yspace()
            textPrint.Screenprint(screen, "Pre Shape - Press 'f' to move away")
            textPrint.Yspace()

            textPrint.Screenprint(screen, "Press 'c' when calibration is complete")

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # Limit to 20 frames per second OR 50 ms scan rate - 1000/20 = 50 ms Both display and checking of Joystick;
            clock.tick(SCAN_RATE)

        # Calibration completed
        my_list=[]
        taxonomy = False
        while taxonomy is False:
            screen.fill(WHITE)
            textPrint.reset()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    key_pressed = event.key
                    print("Key Ascii Value {} Pressed".format(key_pressed))
                    my_list.append(chr(key_pressed))
                    if key_pressed == 13:           # Enter Key to get out
                        taxonomy = True
                else:
                    pass


            textPrint.Screenprint(screen, "Taxonomy = {}".format("".join(my_list)))
            textPrint.Yspace()
            textPrint.Yspace()
            textPrint.Screenprint(screen,"Caps Lock Key set to {}".format(key_ring['301']))
            textPrint.Yspace()
            textPrint.Screenprint(screen, "Finger 1 - Press 'q' to move up")
            textPrint.Yspace()
            textPrint.Screenprint(screen, "Finger 1 - Press 'a' to move down")
            textPrint.Yspace()
            textPrint.Screenprint(screen, "Finger 2 - Press 'w' to move up")
            textPrint.Yspace()
            textPrint.Screenprint(screen, "Finger 2 - Press 's' to move down")
            textPrint.Yspace()
            textPrint.Screenprint(screen, "Finger 3 - Press 'e' to move up")
            textPrint.Yspace()
            textPrint.Screenprint(screen, "Finger 3 - Press 'd' to move down")
            textPrint.Yspace()
            textPrint.Screenprint(screen, "Pre Shape - Press 'r' to move closer")
            textPrint.Yspace()
            textPrint.Screenprint(screen, "Pre Shape - Press 'f' to move away")
            textPrint.Yspace()

            textPrint.Screenprint(screen, "Press 'c' when calibration is complete")

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # Limit to 20 frames per second OR 50 ms scan rate - 1000/20 = 50 ms Both display and checking of Joystick;
            clock.tick(SCAN_RATE)

        # The main loop that examines for other UI actions including Joy button/HatLoop until the user clicks the close button.
        done = False
        while done is False:
            screen.fill(WHITE)
            textPrint.reset()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    time.sleep(0.5)
                elif event.type == pygame.KEYDOWN:
                    key_pressed = event.key
                    print("Key Ascii Value {} Pressed".format(key_pressed))
                    key_ring[str(key_pressed)] = 1
                    if key_ring['301'] == 1:    # Caps lock is 1
                        time.sleep(0.5)
                        my_key_controller.set_key_press(key_pressed)
                        time.sleep(0.2)
                elif event.type == pygame.KEYUP:
                    key_released = event.key
                    print("Key Ascii Value {} Released".format(key_released))
                    key_ring[str(key_released)] = 0

                else:
                    pass # ignoring other non-logitech joystick event types

            textPrint.Screenprint(screen, "When ready to Quit, close the screen")
            textPrint.Yspace()
            textPrint.Screenprint(screen,"Caps Lock Key Pressed {}".format(key_ring['301']))
            textPrint.Yspace()
            textPrint.Screenprint(screen,"Taxonomy = {}".format(''.join(my_list)))
            textPrint.Yspace()
            pygame.display.flip()

            # Limit to 20 frames per second OR 50 ms scan rate - 1000/20 = 50 ms Both display and checking of Joystick;
            clock.tick(SCAN_RATE)

        return



if __name__ == "__main__":

    a = gripper()
    b =5