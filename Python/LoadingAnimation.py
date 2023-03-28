import time, sys
indent = 0
indentIncreasing = True 

try:
    while True: # главный цикл программы
        print(' ' * indent, end = '')
        print('******** ' )
        time.sleep(0.1)
        if indentIncreasing:
            indent = indent + 1
            if indent == 20:
                indentIncreasing = False
        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()