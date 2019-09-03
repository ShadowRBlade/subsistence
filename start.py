from time import sleep
from sys import platform
import perks


platform = platform[:2]
if (platform == 'li'):
    print("Running on Linux")
elif(platform == 'wi'):
    print("Running on Windows")

perks.setPerks()
