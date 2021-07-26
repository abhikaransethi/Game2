import curses
import copy
import time
import random
t = curses.initscr()


curses.curs_set(0)
curses.start_color()
h, w =t.getmaxyx()
screen=curses.newwin(h, w, 0,0)
screen.keypad(True)
curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_RED)
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_GREEN)
snake=[[0,1],[0,0]]
screen.timeout(50)
key=curses.KEY_RIGHT
ud=[curses.KEY_UP, curses.KEY_DOWN]
lr=[curses.KEY_RIGHT,curses.KEY_LEFT]
food=[h//2, w//2]
count=0
while True and snake[0] not in snake[1:] and snake[0][0]>=0 and snake[0][0]<h and snake[0][1]>=0 and snake[0][1]<=w:
    screen.attron(curses.color_pair(1))
    screen.addch(snake[0][0], snake[0][1], curses.ACS_PI)
    screen.attroff(curses.color_pair(1))
    screen.attron(curses.color_pair(2))
    screen.addch(food[0], food[1], curses.ACS_PI)
    screen.attroff(curses.color_pair(2))
    screen.refresh()
    if key in ud:
        screen.timeout(100)
    if key in lr:
        screen.timeout(50)
    keyentered=screen.getch()
    
    if keyentered in ud and key in ud:
        key=key

    elif keyentered in lr and key in lr:
        key=key

    elif keyentered==-1:
        key=key
    else:
        key=keyentered
    newhead=copy.copy(snake[0])


    if key==curses.KEY_RIGHT:
        newhead[1]+=1
    elif key==curses.KEY_LEFT:
        newhead[1]-=1
    elif key==curses.KEY_UP:
        newhead[0]-=1
    elif key==curses.KEY_DOWN:
        newhead[0]+=1
    else:
        screen.keypad(False)
        curses.curs_set(1)
        curses.endwin()
        break
    snake.insert(0, newhead)
    if snake[0]==food:
        count+=1
        food=None
        while food is None:
            food = [random.randint(0,h-1), random.randint(0,w-1)] if food not in snake else None
    else:
        tail=snake.pop()
        screen.addch(tail[0],tail[1], ' ')
        screen.refresh()





print("You got {} points".format(count))
