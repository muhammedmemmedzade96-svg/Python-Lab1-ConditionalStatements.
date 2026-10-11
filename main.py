def main_menu():
    print("Welcome to the Lab 1 Application!")
    # I want to ask for the name first to greet the user personally
    user_name = input("Please enter your name: ").strip()
    
    while True:
        # Custom message using the user's name so it feels unique for eveyrone :) 
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
            run_bgg(user_name)   # still developing  :(  
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
        print(f"{name}, your BMI is: {bmi:.2f}")
        
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
if __name__ == "__main__":
    main_menu()
