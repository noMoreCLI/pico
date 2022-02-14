from machine import Timer
import picowireless # type: ignore
import utime

toggleFlag = False
count = 0
picowireless.init()

def toggle(self):
    global toggleFlag
    if toggleFlag:
        toggleFlag = False
        picowireless.set_led(255,0,0)
    else:
        toggleFlag = True
        picowireless.set_led(0,255,0)
    global count
    count += 1

print("Init timer")
tim = Timer()
Timer()
tim.init(mode=machine.Timer.PERIODIC, period=1, tick_hz=16, callback=toggle) # type: ignore
print("Starting main loop")
while True:
    utime.sleep(1)
    #toggle()
    print(f"Count: {count}")
        