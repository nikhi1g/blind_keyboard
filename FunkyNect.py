from threading import Thread
from imports import *
from pynput import keyboard


class FunkyNect():
    def __init__(self):
        self.key_left = False
        self.key_right = False
        self.row_top = False
        self.row_middle = False
        self.row_bottom = False
        self.row_enter = False
        self.clicked = False
        self.delete = False
        self.start_monitor()

    def start_monitor(self):
        Thread(target=self.start_monitor_thread, daemon=True).start()

    def start_monitor_thread(self):
        while True:
            pass
        # while True:
            # print("\r", "left",self.key_left, "right", self.key_right,"enter", self.row_enter,"top selector", self.row_top, "middle selector",self.row_middle,"bottom selector", self.row_bottom,"clicked", self.clicked, end="")

    # def on_press(self, key):
    #     try:
    #         # print('alphanumeric key {0} pressed'.format(key.char))
    #         pass
    #     except AttributeError:
    #         # print('special key {0} pressed'.format(key))
    #         pass

    def on_press(self, key):
        # print('{0} released'.format(
        #     key))
        if key == keyboard.Key.right:
            self.key_right = True
        if key == keyboard.Key.left:
            self.key_left = True
        if key == keyboard.Key.up:
            self.row_top = True
        if key == keyboard.Key.down:
            self.row_bottom = True
        try:
            if str(format(key.char)) == "m": # true for all non-special characters
                self.row_middle = True
            if str(format(key.char)) == "c": # true for all non-special characters
                self.clicked = True
        except AttributeError:
            pass
        if key == keyboard.Key.enter:
            self.row_enter = True
        if key == keyboard.Key.backspace:
            self.delete = True
        if key == keyboard.Key.esc:
            return False

    def start(self):
        Thread(target=self.start_thread, daemon=True).start()

    def start_thread(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()


if __name__ == '__main__':
    camera = FunkyNect()
    camera.start()
