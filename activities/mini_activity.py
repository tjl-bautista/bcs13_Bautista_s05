'''
Create an if-else statement that determines if a number is divisible by 3, 5, or both. 
If the number is divisible by 3, print "The number is divisible by 3"
If the number is divisible by 5, print "The number is divisible by 5"
If the number is divisible by 3 and 5, print "The number is divisible by both 3 and 5"
If the number is not divisible by any, print "The number is not divisible by 3 nor 5"

Screenshot your code solution and result and paste it in our Lecture Discussion Link
'''

num = int(input("Enter a number: "))

if num % 5 == 0 and num % 3 == 0:
    print("The number is divisible by both 3 and 5")
elif num % 3 == 0:
    print("The number is divisible by 3")
elif num % 5 == 0:
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 3 nor 5") 