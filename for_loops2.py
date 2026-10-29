user_input = int(input("What level of brightness is required?\n"))
print("\Adjusting brightness...\n")

for current_level in range (2, user_input+1, 2):
    aesterisks = "*" * current_level
    print(f"Brightness level: [aesterisks}")

    print("\nComplete!")