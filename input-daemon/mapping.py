from evdev.ecodes import *

cec_mapping = {
    # core navigation
    KEY_OK  : [KEY_ENTER],
    KEY_EXIT: [KEY_ESC],

    # directions
    KEY_UP   : [KEY_UP],
    KEY_DOWN : [KEY_DOWN],
    KEY_LEFT : [KEY_LEFT],
    KEY_RIGHT: [KEY_RIGHT],

    # color buttons
    KEY_RED   : [KEY_LEFTCTRL, KEY_1], # navigation menu
    KEY_GREEN : [KEY_LEFTCTRL, KEY_2], # quick menu
    KEY_YELLOW: [KEY_LEFTCTRL, KEY_0], # properties
    KEY_BLUE  : [KEY_LEFTCTRL, KEY_8], # fullscreen

    # media controls
    KEY_PLAYCD : [KEY_SPACE],
    KEY_PAUSECD: [KEY_SPACE],
    KEY_REWIND : [KEY_LEFTALT, KEY_F4], # exit game

    # numerical buttons
    KEY_NUMERIC_0: [KEY_0],
    KEY_NUMERIC_1: [KEY_1],
    KEY_NUMERIC_2: [KEY_2],
    KEY_NUMERIC_3: [KEY_3],
    KEY_NUMERIC_4: [KEY_4],
    KEY_NUMERIC_5: [KEY_5],
    KEY_NUMERIC_6: [KEY_6],
    KEY_NUMERIC_7: [KEY_7],
    KEY_NUMERIC_8: [KEY_8],
    KEY_NUMERIC_9: [KEY_9],
}