#Let the user input a number. Check if the number is
#even or odd
#is divisible by 5
#is divisble by 5 and odd

num = int(input("Give me a number: "))

if num % 2 != 0 and num % 5 == 0:
    print("Your number is odd and divisble with 5")
elif num % 2 !=0:
    print("your number is odd")
else:
    print("Your number is even")