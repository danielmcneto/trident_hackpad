import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.combos import Combos, Chord

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()

keyboard.direct_pins = (board.D10, board.D9, board.D8)
encoder_handler.pins = (board.D0, board.D1, board.D2)

keyboard.keymap = [
    [
        KC.LCTRL(KC.C),
        KC.LCTRL(KC.V),
        KC.LCTRL(KC.S)
    ]
]

encoder_handler.map = [
    ((KC.VOLD,  KC.VOLU, KC.MUTE),) 
]

keyboard.modules.append(encoder_handler)

keyboard.go()