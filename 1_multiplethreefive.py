# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Maximum number range = 1000
# Find numbers where n % 3 = 0
#                 or n % 5 = 0
# Add the numbers with these properties to the list
# Sum the list

total = 0

for num in range(1, 1000):  # numbers below 1000

    if ((num % 3) == 0) or ((num % 5) == 0):
        print("Num is: ",num)
        print("Total is: ",total)
        total += num

print("\n\nFinal Total:", total)