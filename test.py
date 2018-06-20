x = int (input ("Enter a number: "))
#x = int (x)
ans = 0
iterate = x
while (iterate != 0):
    ans = ans + x
    iterate -= 1
print("The square of" + " " + str(x) + " " + "is" + " " + str(ans))