#Task1 Sample Solution
#Given two sides of right angled triangle
#Calculate the third side.Get two sides from user

ab = input("Please enter ab")
bc = input("please enter bc")
ac = (int(ab)**2 + int(bc)**2)**(1/2)
print("ac is:"+str(ac))


numbers = [2, 56, 12, 67, 1000, 32, 89, 29, 44, 39, 200, 11, 21]
Y = max(numbers)
L = min(numbers)
print(Y)
print(L)
