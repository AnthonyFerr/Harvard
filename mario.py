import os
height = 0
def getHeight():
    global height
    try:
        height = int(input("How high do you want the pyramid to be?\n"))
    except:
        print("Are you sure that this is the equivilant of an integer?")
        getHeight()
    else:
        if height < 0:
            print("Height cannot be negative!")
            getHeight()
        elif height > 23:
            print("Height cannot be greater than 23")
            getHeight()
getHeight()
os.system('clear')

"""
space = height
for i in range(height):
    print(space*" ", "#"*(i+1))
    space -= 1
"""

space = height
for i in range(height):
    print(space*" " + "#"*(i+1) + "#"*(i+1))
    space -= 1
