numbers = [1, 4, 5, 7, 9, 10]
for number in numbers:
    if number % 3 == 0:
        print(f"First multiple of 3 found: {number}")
        break # Exit the loop
    print(f"{number} is not a multiple of 3")

##########################################################

languages = ['Swift', 'Python', 'Go']

# start of the loop
for lang in languages:
    print(lang)
    print('-----')
# end of the for loop
print('Last statement')

##########################################################

# Prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

###########################################################
#Factorial of a number using while loop
num = 5
fact = 1
i = 1

while i <= num:
    fact *= i
    i += 1

print("Factorial =", fact)

#####################################################
# count even or odd numbers in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even = 0
odd = 0

for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)