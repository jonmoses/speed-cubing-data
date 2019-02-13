import time
import curses
import pyfiglet


done = False


def pbar(window):
    window.addstr(1, 0, pyfiglet.figlet_format("Timer!"))
    while not done:
        window.addstr(7, 0, pyfiglet.figlet_format(str(time.localtime(time.time())[5])))
        time.sleep(1)
        window.clrtoeol()
        window.refresh()



curses.wrapper(pbar)
