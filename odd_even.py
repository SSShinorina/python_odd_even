number=input("Enter the maximum number")
number1=input("Enter the minimum number")
print(number)
print(number1)
array=list(range((int (number1)),(int (number))))
print (array)
for i in array:
    if (array.index(i)%2) == 0:
        print ("This is even position")
    else:
        print ("This is odd position")