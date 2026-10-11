def main_menu():
    print("Welcome to the Lab 1 Application!")
    # I want to ask for the name first to greet the user personally
    user_name = input("Please enter your name: ").strip()
    
    while True:
        # Custom message using the user's name so it feels unique
        print(f"\n--- Hello {user_name}, Please Select an Option ---")
        print("1. Body Mass Index (BMI) Calculator")
        print("2. Chinese Zodiac Calculator")
        print("3. Birthday Guessing Game")
        print("4. Exit")
        
        choice = input("Your choice (1-4): ").strip()
        
        # Checking choices and routing to the correct function
        if choice == '1':
            run_bmi(user_name) 
        elif choice == '2':
            run_czc(user_name) 
        elif choice == '3':
            run_bgg(user_name) # It is finally finished...
        elif choice == '4':
            # This is the unique exit message I picked
            print(f"\nGoodbye {user_name}! Exiting the app. Code executed successfully!")
            break # Stops the menu and shuts down the app
        else:
            print("\nError: Invalid choice! Please type 1, 2, 3, or 4.")

# ----------------- TASK 1: BMI CALCULATOR -----------------
def run_bmi(name):
    while True:
        print(f"\n--- BMI Calculator (Active User: {name}) ---")
        try:
            # Using float because height and weight can have decimals
            weight = float(input("Enter weight (kg): "))
            height = float(input("Enter height (m): "))
            
            # Making sure the numbers are realistic and positive
            if weight <= 0 or height <= 0:
                print("Error: Numbers must be greater than 0!")
                continue
        except ValueError:
            # Prevents crashes if someone accidentally types letters
            print("Error: Please type numbers only!")
            continue
            
        # Standard formula from the sheet: weight divided by height squared
        bmi = weight / (height * height)
        print(f"{name}, your BMI is: {bmi:.2f}") #.2f for the 2 decimals
        
        # Matching the BMI number to the official table ranges
        if bmi < 18.5:
            category = "Underweight [⚠️ Need to gain weight]"
        elif 18.5 <= bmi < 25.0:
            category = "Normal Weight [✅ Great job!]"
        elif 25.0 <= bmi < 30.0:
            category = "Overweight [⚠️ Watch your diet]"
        else:
            category = "Obese [🚨 Please consult a doctor]"
            
        print(f"Your Category: {category}")
        
        repeat = input(f"\n{name}, do you want to check another BMI? (yes/no): ").strip().lower()
        if repeat != 'yes':
            break

# ----------------- TASK 2: CHINESE ZODIAC -----------------
def run_czc(name):
    while True:
        print(f"\n--- Chinese Zodiac Calculator (Active User: {name}) ---")
        try:
            # Years must be whole numbers, so I used int()
            year = int(input("Enter your birth year (e.g., 2004): "))
            if year < 0:
                print("Error: Years cannot be negative numbers!")
                continue
        except ValueError:
            print("Error: Please enter a proper whole number for the year!")
            continue
            
        # The zodiac has a 12-year cycle, so % 12 gives the correct remainder
        remainder = year % 12
        
        # Matching the remainder to the animal names from the pdf
        if remainder == 0: zodiac = "Monkey 🐵"
        elif remainder == 1: zodiac = "Rooster 🐔"
        elif remainder == 2: zodiac = "Dog 🐶"
        elif remainder == 3: zodiac = "Pig 🐷"
        elif remainder == 4: zodiac = "Rat 🐭"
        elif remainder == 5: zodiac = "Ox 🐮"
        elif remainder == 6: zodiac = "Tiger 🐯"
        elif remainder == 7: zodiac = "Rabbit 🐰"
        elif remainder == 8: zodiac = "Dragon 🐲"
        elif remainder == 9: zodiac = "Snake 🐍"
        elif remainder == 10: zodiac = "Horse 🐴"
        elif remainder == 11: zodiac = "Sheep 🐑"
        
        print(f"{name}, your Chinese Zodiac sign is the {zodiac}")
        
        repeat = input(f"\n{name}, do you want to check another year? (yes/no): ").strip().lower()
        if repeat != 'yes':
            break

# ----------------- TASK 3: BIRTHDAY GAME -----------------
def run_bgg(name):
    while True:
        print(f"\n--- Birthday Guessing Game (Active User: {name}) ---")
        print("Look at the number groups below and answer honestly.")
        
        # These are the exact number tables copied from the assignment book
        set1 = " 1  3  5  7\n 9 11 13 15\n17 19 21 23\n25 27 29 31"
        set2 = " 2  3  6  7\n10 11 14 15\n18 19 22 23\n26 27 30 31"
        set3 = " 4  5  6  7\n12 13 14 15\n20 21 22 23\n28 29 30 31"
        set4 = " 8  9 10 11\n12 13 14 15\n24 25 26 27\n28 29 30 31"
        set5 = "16 17 18 19\n20 21 22 23\n24 25 26 27\n28 29 30 31"
        
        sets = [set1, set2, set3, set4, set5]
        # These are the base numbers (first numbers) used to calculate the date
        first_numbers = [1, 2, 4, 8, 16]
        birthday = 0
        
        # Loop 5 times to show all 5 tables one by one
        for i in range(5):
            print(f"\n[Group Set {i+1}]")
            print(sets[i])
            
            while True:
                # User must type 1 for Yes or 0 for No
                ans = input("Is your birthday in this group? (1 for Yes, 0 for No): ").strip()
                if ans == '1' or ans == '0':
                    if ans == '1':
                        # If yes, I add the first number of that group to the total sum
                        birthday += first_numbers[i]
                    break
                else:
                    print("Error: Please type only 1 or 0!")
        
        # A quick check to see if the final calculated date makes sense
        if birthday == 0 or birthday > 31:
            print(f"\nHey {name}, something went wrong. Your answers don't match any real day.")
        else:
            print(f"\n🎉 Magic! {name}, your birthday is on the day: {birthday}")
            
        repeat = input(f"\n{name}, do you want to play this game again? (yes/no): ").strip().lower()
        if repeat != 'yes':
            break # Back to the Main Menu

if __name__ == "__main__":
    # Starts the program automatically when the file is opened
    main_menu()
