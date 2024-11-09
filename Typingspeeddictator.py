import curses
from curses import wrapper
import time


def welcome_text(stdscr):
    stdscr.clear()
    stdscr.addstr("You are welcome to this typing speed detector!!!", curses.color_pair(3))
    stdscr.refresh()
    stdscr.getkey()


def next_text(stdscr):
    stdscr.clear()
    stdscr.addstr("Enter any key to continue!!! Your time starts ticking as soon as you press the key.", curses.color_pair(3))
    stdscr.refresh()
    stdscr.getkey()



def engine(stdscr):

    text = "How are you doing today"
    current_text = []
    
    while True:
        stdscr.clear()
        stdscr.addstr(text)

        for i, char in enumerate(current_text):
            if char != text[i]:
                stdscr.addstr(0, i, char, curses.color_pair(1))
            else:
                stdscr.addstr(0, i, char, curses.color_pair(2))

        stdscr.refresh()
        key = stdscr.getkey()
        if ord(key) == 27:
            break

        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        else:
            if len(current_text) < len(text):
                current_text.append(key)

        if ''.join(current_text) == text:
            break
    return current_text

    
    

def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    welcome_text(stdscr)
    next_text(stdscr)
    start_time = time.time()
    list_of_text = engine(stdscr)
    end_time = time.time()
    time_elapsed = end_time - start_time
    wpm = round((len(list_of_text) / (time_elapsed / 60))/5, 1)
    print(f"WPM: {wpm}")
    

wrapper(main)
