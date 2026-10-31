phrase = input("What phrase do you want to see in reverse?\n")
print("Reversing...")

reversed_phrase = ""

# Start at the last character and move backwards to index 0.
for index in range(len(phrase) - 1, -1, -1):
    reversed_phrase += phrase[index]

print("The phrase is:", reversed_phrase)
