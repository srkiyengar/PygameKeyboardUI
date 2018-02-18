__author__ = 'srkiyengar'

import logging
import time
from datetime import datetime





MOVE_TICKS = 130
MOVE_TICKS_SERVO4 = 70
POS_ERROR = 20


ndi_measurement = False         # meaning we are not running polaris when False
log_data_to_file = False        # To collect servo data without ndi measurements, this is set to True
control_method = 2              #1 means joystick displacement moves goal position by constant*MOVE_TICKS value.
                                #2 means joystick displacement moves goal position to a fixed value.

servo_move_with_joy = True      # means joystick or thumstick will move servo

CALIBRATION_TICKS = 50


# With lower limit set by eye during cabliration, upper limit is set by the two MAX values
MAX_FINGER_MOVEMENT = 2100      # Fingers  1,2,3 upper limit offset from lower limit (+ or - depends on rotation).
MAX_PRESHAPE_MOVEMENT = 800    # space between 1 and 2

MAX_SPEED = 600 # A max speed of 1023 is allowed

# This logger is setup in the main python script
my_logger = logging.getLogger("My_Logger")
LOG_LEVEL = logging.DEBUG



# Since Fingers start from 1 to 4, list and tuples will have index 0 left unused.

class reflex_sf():
    '''The class manages the calibration and movement of the fingers for pinch and grasp
    '''
    def __init__(self):
        self.palm = 1



class key_reflex_controller:

    def __init__(self):
        self.keys = {'113':0,'97':0,'119':0,'115':0,'101':0,'100':0,'114':0,'102':0,'99':0,'122':0,'108':0,'109':0,
                     '110':0, '112':0, '120':0, '111':0}
        # Letter-Integers q-113,a-97,w-119,s-115,e-101,d-100,r-114,f-102, c-99, z-122, l-108, m-109, n-110, p-112
        # x-120, o(111)
        # q(113), a(97) - up or down servo 1 which is finger 1
        # w(119), s(115) - up or down servo 2 which is finger 2
        # e(101), d(100) - up or down servo 3 which is finger 3
        # r(114), f(102) - away or closer between fingers 1 and 2
        # c(99) - Calibration complete. The current positions of the servo will be the new lowest position
        # z(122) - To measure drift from lowest position- Take the fingers to lowest and then use the command
        # l(108) - To Toggle Gripper with or without creating servo position file - Default - without
        # n(110) To Toggle Ndi labview measurements - Default - No NDI measurement
        # m(109) for toggling velocity method to drive gripper position to fixed displacement gripper position
        # p(112) for sending fingers to rest position
        # x(120) will toggle if joystick will drive the servo or not
        # o(111) will read a file and move to the location

        # When key value is captured it can be turned into string for the dict.
        # Keys are set to 0 and become 1 if key is pressed and back go to 0 when released

    def set_key_press(self, key):
        self.keys[str(key)] = 1
        return self.process_key_actions()

    def set_key_release(self,key):
        self.keys[str(key)] = 0

    def reset_key_press(self,key):
        self.keys[str(key)] = 0

    def process_key_actions(self):  # Act based on Buttons
        k = 0       # returns 1 when processing letter c otherwise k is unchanged.

        if self.keys['99'] == 1:  # letter c
            self.reset_key_press(99)
            k = 1
        return k




