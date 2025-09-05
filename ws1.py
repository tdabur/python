#ans 1
print("""Twinkle, twinkle, little star,
      How I wonder what you are! 
      Up above the world so high,
      Like a diamond in the sky.
Twinkle, twinkle, little star,
      How I wonder what you are!""")

#ans 2
first = input("Enter your first name: ")
last = input("Enter your last name: ")
print(last + " " + first)

#ans 3
import math
radius = float(input("Enter radius of circle: "))
area = math.pi * radius ** 2
print("Area of circle =", area)

#ans 4
color_list = ["Red", "Green", "White", "Black"]
print("First color:", color_list[0])
print("Last color:", color_list[-1])

#ans 5
n = int(input("Enter an integer: "))
result = n + int(str(n)*2) + int(str(n)*3)
print("Result =", result)

#ans 6
nums = input("Enter numbers separated by commas: ")
num_list = nums.split(",")
num_tuple = tuple(num_list)

print("List:", num_list)
print("Tuple:", num_tuple)

#ans 7
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

#ans 8
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a   # swapping

print("After swapping: a =", a, ", b =", b)

#ans 9
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#ans 10
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

#ans 11
import math
x1, y1 = map(float, input("Enter first point (x1 y1): ").split())
x2, y2 = map(float, input("Enter second point (x2 y2): ").split())

distance = math.sqrt((x2 - x1)*2 + (y2 - y1)*2)
print("Euclidean distance =", distance)

#ans 12
a = float(input("Enter first angle: "))
b = float(input("Enter second angle: "))
c = float(input("Enter third angle: "))

if a + b + c == 180:
    print("It is a triangle")
else:
    print("Not a triangle")

#ans 13
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): "))

ci = p * (pow((1 + r / 100), t)) - p
print("Compound Interest =", ci)

#ans 14
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime Number")
else:
    print("Not Prime")

#ans 15
n = int(input("Enter a positive integer: "))
sum_sq = sum(i**2 for i in range(1, n+1))
print("Sum of squares =", sum_sq)