# 99 bottles.

import time
import sys
import bext

bext.fg('red')
print('99 Bottles')

print('(Press ctrl-c to Quit.)')

time.sleep(2)

bottles = 99
PAUSE = 1  # Change this to 0 to se the full song

try:
    while bottles > 1:  # Keep looping and display the lyrics.
        bext.fg('cyan')
        print(bottles, 'bottles of milk on the wall,')
        time.sleep(PAUSE)  # Pause for PAUSE number of seconds.
        print(bottles, 'bottles of milk,')
        time.sleep(PAUSE)
        print('Take one down, pass it around,')
        time.sleep(PAUSE)
        bottles = bottles - 1  # Decrease the number of bottles by one.
        print(bottles, 'bottles of milk on the wall!')
        time.sleep(PAUSE)
        print()  # Print a newline.

    # Display the last stanza:
    print('1 bottle of milk on the wall,')
    time.sleep(PAUSE)
    print('1 bottle of milk,')
    time.sleep(PAUSE)
    print('Take it down, pass it around,')
    time.sleep(PAUSE)
    print('No more bottles of milk on the wall!')
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.
