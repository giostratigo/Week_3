# Ask the user about how many apples wants to display.
print("How many mountains should I display?")
mountains = int(input())

print("\nDisplaying...\n")

# Display one mountain for each repetition.
for count in range(mountains):
    print("           __")
    print("          /  \\_")
    print("         /^    \\")
    print("        /  ^    \\_")
    print("      _/ ^ ^     ^\\")
    print("     /  ^     ^    \\")

# Confirm that all mountains have been displayed.
print("\nDone!")