import threading

from imports.imports import *
from imports.kivy_imports import *
from FunkyNect import *

camera = FunkyNect()
camera.start()
SCREEN_MANAGER = ScreenManager()
TYPE_SCREEN_NAME = 'type'


class MazeGUI(App):
    def build(self):
        return SCREEN_MANAGER


Window.clearcolor = (0, 0, 0, 1)  # black


class TypeScreen(Screen):
    a1 = ObjectProperty(None)
    b1 = ObjectProperty(None)
    c1 = ObjectProperty(None)
    d1 = ObjectProperty(None)
    e1 = ObjectProperty(None)
    f1 = ObjectProperty(None)
    g1 = ObjectProperty(None)
    h1 = ObjectProperty(None)
    i1 = ObjectProperty(None)
    j1 = ObjectProperty(None)
    k1 = ObjectProperty(None)
    l1 = ObjectProperty(None)
    m1 = ObjectProperty(None)
    n1 = ObjectProperty(None)
    o1 = ObjectProperty(None)
    p1 = ObjectProperty(None)
    q1 = ObjectProperty(None)
    r1 = ObjectProperty(None)
    s1 = ObjectProperty(None)
    t1 = ObjectProperty(None)
    u1 = ObjectProperty(None)
    v1 = ObjectProperty(None)
    w1 = ObjectProperty(None)
    x1 = ObjectProperty(None)
    y1 = ObjectProperty(None)
    z1 = ObjectProperty(None)
    space = ObjectProperty(None)
    star = ObjectProperty(None)
    dash = ObjectProperty(None)
    delete = ObjectProperty(None)
    enterKey = ObjectProperty(None)
    nickname = ObjectProperty(None)
    bar = ObjectProperty(None)
    cursor = ObjectProperty(None)

    cursor_y_top_row = 0.54
    cursor_y_middle_row = 0.39
    cursor_y_bottom_row = 0.24
    cursor_size_hint = 0.05*1.3, 0.06

    top_row_pos_hint = {"x": .015, "y": .54}
    middle_row_pos_hint = {"x": .015, "y": .39}
    bottom_row_pos_hint = {"x": .015, "y": .24}

    bar_size_hint = 0.944, .06

    enter_key_pos_hint = {"x": .087, "y": .09}
    enter_size_hint = 0.09, .06

    # KeyboardObjectList = [q1, w1, e1, r1, t1, y1, u1, i1, o1, p1, a1, s1, d1, f1, g1, h1, j1, k1, l1,
    #                       space, z1, x1, c1, v1, b1, n1, m1, star, dash,
    #                       delete, enterKey]

    def enter(self):
        self.set_keyboard_keys()
        Thread(target=self.keyboard_movement, daemon=True).start()

        # self.cursor.pos_hint['y'] = self.t1.pos_hint['y'] - 0.01  # accurate per key, doesnt work in thread?
#0.0085
    def keyboard_movement(self):
        top_row_buttons = [self.q1, self.w1, self.e1, self.r1, self.t1, self.y1, self.u1, self.i1, self.o1, self.p1]
        # middle_row_buttons = [self.a1, self.s1, self.d1, self.f1, self.g1, self.h1, self.j1, self.k1, self.l1, self.space]
        # bottom_row_buttons = [self.z1, self.x1, self.c1, self.v1, self.b1, self.n1, self.m1, self.star, self.dash, self.delete]
        # rows = [top_row_buttons,middle_row_buttons,bottom_row_buttons]
        # self.cursor.pos_hint['x'] = self.y1.pos_hint["x"] - 0.0085
        KeyboardObjectList = [self.q1, self.w1, self.e1, self.r1, self.t1, self.y1, self.u1, self.i1, self.o1, self.p1,
                              self.a1, self.s1, self.d1, self.f1, self.g1, self.h1, self.j1, self.k1, self.l1, self.space,
                              self.z1, self.x1, self.c1, self.v1, self.b1, self.n1, self.m1, self.star, self.dash, self.delete]
        # while SCREEN_MANAGER.current == TYPE_SCREEN_NAME:
        index = 0
        sleeptime = 0.1
        while True:
            if not camera.row_enter:
                self.cursor.pos_hint = KeyboardObjectList[index].pos_hint
                try:
                    KeyboardObjectList[index].color = "white"
                    KeyboardObjectList[index + 1].color = "lightblue"
                    KeyboardObjectList[index - 1].color = "lightblue"
                    #AROUND orig color for either direction
                except IndexError: pass
                if camera.key_right and index < 29:
                    index += 1
                    camera.key_right = False
                if camera.key_left and index > 0:
                    index -= 1
                    camera.key_left = False
                if camera.delete:
                    self.Delete_Key_Update()
                    camera.delete = False
                if camera.row_top:
                    if index > 9:
                        index -= 1
                    self.bar.pos_hint = self.top_row_pos_hint
                    camera.row_middle = False
                    camera.row_bottom = False
                    sleep(sleeptime)
                if camera.row_middle:
                    if index < 10:
                        index += 1
                    if index > 19:
                        index -= 1
                    self.bar.pos_hint = self.middle_row_pos_hint
                    camera.row_top = False
                    camera.row_bottom = False
                    sleep(sleeptime)
                if camera.row_bottom:
                    if index < 20:
                        index += 1
                    self.bar.pos_hint = self.bottom_row_pos_hint
                    camera.row_top = False
                    camera.row_middle = False
                    sleep(sleeptime)
                if camera.clicked:
                    try:
                        for thing in KeyboardObjectList:
                            if self.cursor.collide_widget(thing):
                                thing.trigger_action(duration=0.1)
                                thing.color = (1, 1, 1, 0.89)
                                sleep(0.2)
                                thing.color = "lightblue"
                                camera.clicked = False
                    except Exception as e:
                        print(e, 'in click, not a button')
            elif camera.row_enter:
                self.Enter_Key_Update()

            sleep(0.1)

    def set_keyboard_keys(self):
        KeyboardObjectList = [self.q1, self.w1, self.e1, self.r1, self.t1, self.y1, self.u1, self.i1, self.o1, self.p1,
                              self.a1, self.s1, self.d1, self.f1, self.g1, self.h1, self.j1, self.k1, self.l1,
                              self.space,
                              self.z1, self.x1, self.c1, self.v1, self.b1, self.n1, self.m1, self.star, self.dash,
                              self.delete, self.enterKey]
        x_spacing = .1
        y_spacing = -.15
        x_offset = 0
        y_offset = 0
        button_count = 0
        for btn in KeyboardObjectList:

            btn.pos_hint = {"x": .02 + x_offset, "y": .55 + y_offset}
            button_count += 1
            x_offset += x_spacing
            btn.color = "lightblue"
            if button_count % 10 == 0:
                x_offset = 0
                y_offset += y_spacing

        self.enterKey.pos_hint = {"x": 0.1, "y": .1}
        self.enterKey.color = "black"
        self.enterKey.text = ""
        self.nickname.color = "lightblue"
        self.nickname.text = "Enter Your Name:"

        self.bar.pos_hint = self.top_row_pos_hint
        self.bar.size_hint = self.bar_size_hint

        # self.cursor.pos_hint = {"x": .0115, "y": .54}
        self.cursor.pos_hint = KeyboardObjectList[1].pos_hint
        self.cursor.size_hint = self.cursor_size_hint



    def Key_Update(self, button):
        if ":" in self.nickname.text or "!" in self.nickname.text:
            self.nickname.text = ""
        self.nickname.text += button.text

    def Delete_Key_Update(self):
        if len(self.nickname.text) > 0:
            self.nickname.text = self.nickname.text[:-1]

    def Enter_Key_Update(self):
        self.bar.pos_hint = self.enter_key_pos_hint
        self.bar.size_hint = self.enter_size_hint
        self.cursor.size_hint = self.enter_size_hint
        self.cursor.pos_hint = self.enter_key_pos_hint

        if len(self.nickname.text) >= 1 and ":" not in self.nickname.text:
            with open("leaderboard.txt", "a") as f:
                # f.write(score + " ")
                f.write(self.nickname.text + "\n")
            self.nickname.text = "Congratulations!"
            Clock.schedule_once(self.transition)
        else:
            self.nickname.text = "Not A Name!"
        camera.row_enter = False

    def transition(self, dt):
        # SCREEN_MANAGER.current = LEADERBOARD_SCREEN_NAME # undo when transfer
        pass


Builder.load_file('screens/TypeScreen.kv')
SCREEN_MANAGER.add_widget(TypeScreen(name=TYPE_SCREEN_NAME))

if __name__ == '__main__':
    MazeGUI().run()
