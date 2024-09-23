import random

#count
count = 0

# Loop
while True:
    # Ask: roll the dice
    choice = input("Roll the dice? (y/n): ").lower()

    # If user enters y
    if choice == 'y':
        # Generate two random numbers
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        # Print them
        print(f'({die1}, {die2})')

        # increment the trial count
        count += 1

    # If user enters n
    elif choice == "n":
        #   Print thank you message
        print("Thank you for playing")
        print(f"you have rolled the dice {count} times during this session")
        #   Terminate
        break

    # Else
    else:
        #   Print invalid choice
        print("Invalid Choice")
