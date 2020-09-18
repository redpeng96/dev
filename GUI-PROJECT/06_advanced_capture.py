import time
from PIL import ImageGrab
import keyboard


def screen_shot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("img{}.png".format(curr_time))
    print(f"Screen has been captured and saved...")

keyboard.add_hotkey("F9", screen_shot)

keyboard.wait("esc")
