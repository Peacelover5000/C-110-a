import time

def countdown_timer(seconds):

        while seconds > 0:

            min = int(seconds / 60)
            sec = int(seconds % 60)

            timer = f'{min}:{sec}'

            print(timer)

            seconds -= 1

        print('Time Up!')

seconds = input("Enter the time in number of seconds: ")

countdown_timer(int(seconds))
