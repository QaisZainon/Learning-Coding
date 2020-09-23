#! python3
# PrettifiedStopwatch.py - A variant of the stopwatch program.
import time, pyperclip
# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit')
input()  # press Enter to begin
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1
recordlist = []
# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = str(round(time.time() - lastTime, 2))
        totalTime = str(round(time.time() - startTime, 2))
        result = 'Lap #' + str(lapNum).rjust(2) + ':' + totalTime.rjust(7) + ' (' + lapTime.rjust(4) + ')'
        print(result, end = '')
        recordlist.append(result)
        lapNum += 1
        lastTime = time.time()  # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone, copied to clipboard.')
    # copies to your clipboard
    pyperclip.copy('\n'.join(recordlist))