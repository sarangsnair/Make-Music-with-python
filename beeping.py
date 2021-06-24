import winsound
from random import randrange
frequency = randrange(5000)
duration = randrange(2000)
winsound.Beep(frequency, duration)
