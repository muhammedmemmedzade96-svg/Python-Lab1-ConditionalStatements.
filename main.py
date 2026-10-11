def main_menu():
    # This loop keeps the menu running until the user decides to exit
    while True:
        print("\n--- Main Menu ---")
        print("1. Body Mass Index (BMI) Calculator")
        print("2. Chinese Zodiac Calculator")
        print("3. Birthday Guessing Game")
        print("4. Exit")
        
        # Get the choice from the user and remove spaces
        choice = input("Please enter your choice (1-4): ").strip()
        
        # Check what the user selected and open the correct tool
        if choice == '1':
            run_bmi()           # Opens the Body Mass Index program
        elif choice == '2':
            run_czc()           # Opens the Chinese Zodiac Calculator program
        elif choice == '3':
            run_bgg()           # Opens the Birthday Guessing Game program
        elif choice == '4':
            # Updated exit message exactly as requested
            print("\nExiting the app. Code executed successfully!")
            break               # Stops the loop and closes the app
        else:
            # Message for wrong inputs (like typing 5 or letters)
            print("\nError: Invalid choice! Please enter 1, 2, 3, or 4.")

# ----------------- TASK 1: BMI CALCULATOR -----------------
def run_bmi():
    # Loop to allow user to calculate multiple times
    while True:
        print("\n--- Body Mass Index (BMI) Calculator ---")
        try:
            # Get numbers from user (float allows decimal numbers like 1.78)
            weight = float(input("Enter weight (kg): "))
            height = float(input("Enter height (m): "))
            
            # Check if numbers are positive
            if weight <= 0 or height <= 0:
                print("Error: Weight and height must be greater than 0!")
                continue
        except ValueError:
            # If the user enters text instead of numbers, catch the error so it does NOT crash!
            print("Error: Please enter a valid number!")
            continue
            
        # Official BMI formula: weight / height squared
        bmi = weight / (height * height)
        print(f"BMI = {bmi:.2f}") # Shows only 2 numbers after the decimal dot
        
        # Check the BMI table to find the weight category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25.0:
            category = "Normal Weight"
        elif 25.0 <= bmi < 30.0:
            category = "Overweight"
        else:
            category = "Obese"
            
        print(f"Category: {category}")
        
        # Ask the user if they want to try again
        repeat = input("\nDo you want to calculate BMI again? (yes/no): ").strip().lower()
        if repeat != 'yes':
            break # Exit this task and go back to the Main Menu

# ----------------- TASK 2: CHINESE ZODIAC -----------------
def run_czc():
    # Loop to allow user to check multiple years
    while True:
        print("\n--- Chinese Zodiac Calculator ---")
        try:
            # Get the birth year as a whole number (integer)
            year = int(input("Enter your birth year: "))
            if year < 0:
                print("Error: Year cannot be negative!")
                continue
        except ValueError:
            # Catch errors if the user types letters so it does NOT crash!
            print("Error: Please enter a valid integer for the year!")
            continue
            
        # Divide by 12 and find the remainder (year % 12)
        remainder = year % 12
        
        # Match the remainder to the correct animal name
        if remainder == 0: zodiac = "Monkey"
        elif remainder == 1: zodiac = "Rooster"
        elif remainder == 2: zodiac = "Dog"
        elif remainder == 3: zodiac = "Pig"
        elif remainder == 4: zodiac = "Rat"
        elif remainder == 5: zodiac = "Ox"
        elif remainder == 6: zodiac = "Tiger"
        elif remainder == 7: zodiac = "Rabbit"
        elif remainder == 8: zodiac = "Dragon"
        elif remainder == 9: zodiac = "Snake"
        elif remainder == 10: zodiac = "Horse"
        elif remainder == 11: zodiac = "Sheep"
        
        print(f"Your Chinese Zodiac sign is: {zodiac}")
        
        # Ask to repeat or go back
        repeat = input("\nDo you want to calculate Zodiac again? (yes/no): ").strip().lower()
        if repeat != 'yes':
            break # Go back to Main Menu

# ----------------- TASK 3: BIRTHDAY GAME -----------------
def run_bgg():
    # Loop for the game
    while True:
        print("\n--- Birthday Guessing Game ---")
        
        # Number tables given by the assignment
        set1 = " 1  3  5  7\n 9 11 13 15\n17 19 21 23\n25 27 29 31"
        set2 = " 2  3  6  7\n10 11 14 15\n18 19 22 23\n26 27 30 31"
        set3 = " 4  5  6  7\n12 13 14 15\n20 21 22 23\n28 29 30 31"
        set4 = " 8  9 10 11\n12 13 14 15\n24 25 26 27\n28 29 30 31"
        set5 = "16 17 18 19\n20 21 22 23\n24 25 26 27\n28 29 30 31"
        
        sets = [set1, set2, set3, set4, set5]
        # The first number of each set (values used to find the day)
        first_numbers = [1, 2, 4, 8, 16]
        birthday = 0
        
        # Show each set to the user one by one
        for i in range(5):
            print(f"\n[Set {i+1}]")
            print(sets[i])
            
            while True:
                # Ask if the birthday is in the table (1 = Yes, 0 = No)
                ans = input("Is your birthday included in this set? (1 for Yes, 0 for No): ").strip()
                if ans == '1' or ans == '0':
                    if ans == '1':
                        # If yes, add the first number of that set to the total
                        birthday += first_numbers[i]
                    break
                else:
                    print("Error: Please enter only 1 or 0!")
        
        # Check if the calculated date is correct for a calendar month
        if birthday == 0 or birthday > 31:
            print("\nError: Could not calculate a valid day based on your answers.")
        else:
            print(f"\nYour birthday is: {birthday}")
            
        # Ask to restart the game or go back
        repeat = input("\nDo you want to play the game again? (yes/no): ").strip().lower()
        if repeat != 'yes':
            break # Go back to Main Menu

# Starts the program when the file is opened
if __name__ == "__main__":
    main_menu()
