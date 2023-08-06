# time module use to get the time

import time

timestamp = time.strftime("%H")

if (int(timestamp) < 12):
    print("good morning")

elif (int(timestamp) == 12):
    print("good day sir")

else:
    print("good night sir")
