import utime
import picowireless # type: ignore
import _thread

picowireless.init()
sleeptimems = 5

def thread():
    while True:
        for r in range(0,255):
            picowireless.set_led(r,0,0)
            utime.sleep_ms(sleeptimems)
        for r in range(255,0,-1):
            picowireless.set_led(r,0,0)
            utime.sleep_ms(sleeptimems)

_thread.start_new_thread(thread, ())
print("Done")
