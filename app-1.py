import random

# How many times
times = input("How many times do you want to roll the dice? (number): ")
times = int(times)

# Loop
i = 1
while i <= times:
    # Ask: roll the dice
    choice = input("Roll the dice? (y/n): ").lower()

    # If user enters y
    if choice == 'y':
        # Generate two random numbers
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        # Print them
        print(f'({die1}, {die2})')
        i += 1

    # If user enters n
    elif choice == "n":
        #   Print thank you message
        print("Thank you for playing")
        #   Terminate
        break

    # Else
    elif choice != "n" or choice != "y":
        #   Print invalid choice
        print("Invalid Choice")


# if the trial times are over thank the user.
else:
    print('Your trial limits are over! thanks for playing')
