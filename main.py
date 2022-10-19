# You can also play a sound when timer was completed

import time # --> Importing time module
from playsound import playsound

# Defining countdown function
def countdown(t):

   while t:
      mins, secs = divmod(t, 60)
      timer = '{:02d}:{:02d}'.format(mins, secs)
      print(timer, end="\n\r")
      if t==1:
         print("Timer Completed!!")
         playsound("ringtone.wav")

      t -= 1
      time.sleep(1)


if __name__ == "__main__":
   t = int(input("Enter the time in seconds : "))
   
   countdown(t)
