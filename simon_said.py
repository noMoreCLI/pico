import picoexplorer as display # type: ignore
import utime
import random
import math


class SensoElement:
    
    #br, bg, bb = (0,0,0)  <--- these should be instance variables
    #r,g,b = (255,255,255) <--- these should be instance variables
    #x,y,rad = (100,100,20)<--- these should be instance variables
    #freq = 1200           <--- these should be instance variables 
    duration = 0.5

    def __init__(self, point: tuple[int, int], radius: int, colorRBG: tuple[int, int, int], freq: int = 1200, duration: float = 0.5):
        self.set_location(point)
        self.set_radius(radius)
        self.set_color(colorRBG)
        self.set_bg_color((0,0,0))
        self.set_duration(duration)
        self.set_frequency(freq)

    def set_location(self, point):
        self.x, self.y = point

    def set_color(self, colorRBG):
        self.r, self.g, self.b = colorRBG

    def set_bg_color(self, colorRBG):
        self.br, self.bg, self.bb = colorRBG

    def set_radius(self, radius):
        self.rad = radius

    def set_frequency(self, f):
        self.freq = f

    @classmethod
    def set_duration(cls, d: float) -> None:
        cls.duration = d

    @classmethod
    def calc_duration(cls, factor: float):
        cls.duration = cls.duration * factor

    def play(self, display, duration: float = None):
        display.set_pen(self.r, self.g, self.b)
        display.circle(self.x, self.y, self.rad)  
        display.update()
        display.set_tone(self.freq)
        if duration is not None:
            utime.sleep(duration)
        else:
            utime.sleep(self.duration)
        display.set_pen(self.br, self.bg, self.bb)
        display.circle(self.x,self.y, self.rad - 2) 
        display.set_tone(-1)
        display.update()

    def init_display(self, display):
        display.set_pen(self.r, self.g, self.b)
        display.circle(self.x, self.y, self.rad) 
        display.set_pen(self.br, self.bg, self.bb)
        display.circle(self.x,self.y, self.rad - 2) 
        display.update()


def play_tone(freq: int,duration: float = 0.4):
    display.set_tone(freq)
    utime.sleep(duration)
    display.set_tone(-1)

def showRound(round: int):
    display.set_pen(0,255,0)
    display.rectangle(0,115,240,30)
    display.set_pen(0,0,0)
    display.text("Round: "+str(round), 35,120, 200,3)
    display.update()

def init_game() -> None:
    pass

def computer_turn():
    pass

def player_turn():
    pass

def loose():
    pass


def start_screen() -> None:
    display.set_pen(0,255,0)
    display.clear()
    display.set_pen(0,0,0)
    display.text("Get Ready to play", 5,20, 200,5)
    display.text("Press Button 'Y' to start", 5,140,200,4)
    display.update()
    while not display.is_pressed(display.BUTTON_Y):
        utime.sleep(.1)


#
# Initialization
#
btn_a = (60,70)
btn_b = (60,190)
btn_x = (180,70)
btn_y = (180,190)
col_a = (255,0,0)
col_b = (255,255,0)
col_x = (0,255,0)
col_y = (0,255,255)
freq_a = 220
freq_b = 440
freq_x = 880
freq_y = 1760
duration_break = 1
duration_play = 0.5
duration_factor = 0.9
buf = bytearray(display.get_width() * display.get_height() * 2)
display.init(buf)
sensoX = SensoElement(btn_x,20,col_x, freq=freq_x, duration=0.5)
sensoY = SensoElement(btn_y,20,col_y, freq=freq_y, duration=0.5)
sensoA = SensoElement(btn_a,20,col_a, freq=freq_a, duration=0.5)
sensoB = SensoElement(btn_b,20,col_b, freq=freq_b, duration=0.5)
sensoElements = [sensoA, sensoB, sensoX, sensoY]

start_screen()

while True:
    playlist = []
    round = 1

    display.set_audio_pin(0)
    display.set_pen(0,0,0)
    display.clear()
    display.set_pen(255,255,255)
    display.text("Simon said", 25, 20, 240,3)

    print("Height: {0}".format(display.get_height()))
    print("Width : {0}".format(display.get_width()))

    for e in sensoElements:
        e.init_display(display)

    inplay = True
    sensoElements[0].set_duration(0.5)

    while inplay:

        showRound(round)
        playlist.append(sensoElements[random.randint(0,3)])
        sensoElements[0].calc_duration(0.90)
        print(f"Duration: {sensoElements[0].duration}")

        # show the play sequence
        utime.sleep(0.7)
        
        for e in playlist:
            e.play(display)
            #e.calc_duration(duration_factor)
            utime.sleep(sensoElements[0].duration)
        print(f"Round: {round} done")
        
        # players turn

        display.update()
        keys = 0
        play = True

        while play:

            if display.is_pressed(display.BUTTON_A):
                print("Button A")
                if playlist[keys] == sensoA:
                    sensoA.play(display, 0.5)
                    keys = keys + 1
                else:
                    print("Lost")
                    inplay = False
                    play = False
            if display.is_pressed(display.BUTTON_B):
                print("Button B")
                if playlist[keys] == sensoB:
                    sensoB.play(display, 0.5)
                    keys = keys + 1
                else:
                    print("Lost")
                    inplay = False
                    play = False
            if display.is_pressed(display.BUTTON_X):
                print("Button X")
                if playlist[keys] == sensoX:
                    sensoX.play(display, 0.5)
                    keys = keys + 1
                else:
                    print("Lost")
                    inplay = False
                    play = False
            if display.is_pressed(display.BUTTON_Y):
                print("Button Y")
                if playlist[keys] == sensoY:
                    sensoY.play(display, 0.5)
                    keys = keys + 1
                else:
                    print("Lost")
                    inplay = False
                    play = False
            utime.sleep(.05)
            if keys == round:
                play = False
                round = round + 1
                print("Starting next round")

        utime.sleep(1)

    display.set_pen(255,0,0)
    display.clear()
    display.set_pen(0,0,0)
    display.text("LOST", 5,20, 200,5)
    display.text("Press Button 'Y' to start", 5,140,200,4)
    display.update()
    while not display.is_pressed(display.BUTTON_Y):
        utime.sleep(.1)
    display.set_pen(0,0,0)
    display.clear()
