import uiautomator2 as u2
import time

if __name__ == '__main__':
    d = u2.connect()
    d.screen_off()
    time.sleep(5)
    d.screen_on()
