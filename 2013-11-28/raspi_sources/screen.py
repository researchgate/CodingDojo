#!/usr/bin/python
import time, curses, parser

scr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.curs_set(0)

try:
        while True:
                f = open('pattern')
                patterns = parser.parse(f.read())
                f.close()

                for delay, pattern in patterns:
                        for i in range(0,4):
                                scr.addstr(i + 10, 50, pattern[i*4:i*4+4])
                        scr.refresh()
                        time.sleep(delay)

except KeyboardInterrupt:
        pass
finally:
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        curses.curs_set(2)

