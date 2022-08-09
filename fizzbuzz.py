#for numbers 1-100, print fizz for multiples of 3 and buzz for multiples of 5
#for multiples of both, print fizz buzz
for i in range(1, 101):
    if i % 15 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
