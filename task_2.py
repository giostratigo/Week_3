# Display the starting message.
print("Calculating the sum of the first 100 numbers...")

# Set the starting number and total.
number = 1
total = 0

# Add each number from 1 to 100 to the total.
while number <= 100:
    total += number
    number += 1

# Display the final answer.
print(f"...Done! The answer is {total}.")