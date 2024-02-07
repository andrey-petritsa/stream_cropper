import time

def run_normal():
    count = 3
    while(True):
        if(count == 0):
            break
        print('Hello World')
        time.sleep(1)
        count = count - 1


run_normal()