#  ques1
print("Hello, World!")

# Ques2 
name = "Aakriti"
age = 22
hobby = "singing"
# Print the variables
print(f"name : {name}")
print(f"age : {age}")
print(f"hobby : {hobby}")

# Ques3
print("Hello, World!")  # it prints Hello,World! 
name = "Aakriti"     #assigning string to a variable(name)
age = 22             #assigning integer
hobby = "singing"    #assigning string 

# Ques4
# Taking an integer input from the user
number = int(input("Enter an integer: "))
# Checking if the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Ques5
# Prompting the user to enter a year
year = int(input("Enter a year: "))
# Determine if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Ques6
# Print the first 10 natural numbers
for number in range(1, 11):
    print(number)

# Ques7
number = int(input("Enter an integer: "))
i = 1        # initializing 
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

# Ques8
for num in range(1,11):
    if num % 3 == 0:
        continue
    print(num)

# Ques9
for num in range(1, 11):
    if num > 5:
        break
    print(num)

# Ques10
def greet(name):
    print(f"Hello, {name}!")

greet("Aakriti")  #call the function and assigning name Aakriti

# Ques11
def add(x,y):
    return x + y
result = add(8,9) 
print(result)












