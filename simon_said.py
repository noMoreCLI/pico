import picoexplorer as display
import utime

def circle(point,rad,col,filled):
  x,y = point
  r,g,b = col
  display.set_pen(r,g,b)
  display.circle(x,y,rad)
  if not filled:
    display.set_pen(0,0,0)
    display.circle(x,y, rad - 2)

def play_tone(freq,duration=0.4):
    display.set_tone(freq)
    #utime.sleep(duration)
    #display.set_tone(-1)

#some definitions
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

#
# Initialization
#

buf = bytearray(display.get_width() * display.get_height() * 2)
display.init(buf)

display.set_audio_pin(0)

print("Height: {0}".format(display.get_height()))
print("Width : {0}".format(display.get_width()))

display.set_pen(0,0,0)
display.clear()
display.set_pen(255,255,255)
display.text("Simon said", 25, 20, 240,3)

circle(btn_a, 20, col_a, False)
circle(btn_x, 20, col_x, False)
circle(btn_b, 20, col_b, False)
circle(btn_y, 20, col_y, False)


display.update()

while True:
    display.update()
    if display.is_pressed(display.BUTTON_A):
        circle(btn_a, 20, col_a, True)
        display.update()
        play_tone(freq_a,0.3)
    else:
        circle(btn_a, 20, col_a, False)     
    if display.is_pressed(display.BUTTON_B):
        circle(btn_b, 20, col_b, True)
        display.update()
        play_tone(freq_b,0.3)
    else:
        circle(btn_b, 20, col_b, False)
    if display.is_pressed(display.BUTTON_X):
        circle(btn_x, 20, col_x, True)
        display.update()
        play_tone(freq_x,0.3)
    else:
        circle(btn_x, 20, col_x, False)
    if display.is_pressed(display.BUTTON_Y):
        circle(btn_y, 20, col_y, True)
        display.update()
        play_tone(freq_y,0.3)
    else:
        circle(btn_y, 20, col_y, False)

    utime.sleep(0.1)
    display.set_tone(-1)
