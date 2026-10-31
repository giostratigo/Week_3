# Read the grid dimensions as whole numbers.
rows = int(input("How many rows should I have?\n"))
columns = int(input("How many columns should I have?\n"))

print("\nHere I go:\n")

# The outer loop starts a row. The inner loop fills it with smileys.
for row in range(rows):
    for column in range(columns):
        if column > 0:
            print(" ", end="")
        print(":-)", end="")
    print()  # Move to the next line after the row is complete.

print("\nDone!")