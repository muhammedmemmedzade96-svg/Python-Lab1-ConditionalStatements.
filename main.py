def main_menu():
    # This loop keeps the menu running so the app stays open for the user
    while True:
        print("\n--- Main Menu ---")
        print("1. Body Mass Index (BMI) Calculator")
        print("2. Chinese Zodiac Calculator")
        print("3. Birthday Guessing Game")
        print("4. Exit")
        
        # Get input and remove extra spaces from the sides
        choice = input("Please enter your choice (1-4): ").strip()
        
        # Check what the user typed and open the correct program
        if choice == '1':
            run_bmi()           # This opens the BMI Calculator
        elif choice == '2':
            print("\nThis feature is under development.") # Task 2 is not added yet
        elif choice == '3':
            print("\nThis feature is under development.") # Task 3 is not added yet
        elif choice == '4':
            # Show the requested exit message and close the app
            print("\nExiting the app. Code executed successfully!")
            break               # Stops the loop and exits
        else:
            # Handles wrong inputs like typing 5 or letters in the menu
            print("\nError: Invalid choice! Please enter 1, 2, 3, or 4.")

# ----------------- TASK 1: BMI CALCULATOR -----------------
def run_bmi():
    # Loop to let the user calculate BMI multiple times
    while True:
        print("\n--- Body Mass Index (BMI) Calculator ---")
        try:
            # Get numbers from user (float is used for decimal numbers)
            weight = float(input("Enter weight (kg): "))
            height = float(input("Enter height (m): "))
            
            # Check if inputs are positive numbers
            if weight <= 0 or height <= 0:
                print("Error: Weight and height must be greater than 0!")
                continue
        except ValueError:
            # Error Handling: Prevents the app from crashing if user types letters
            print("Error: Please enter a valid number!")
            continue
            
        # Standard formula: BMI = weight / (height * height)
        bmi = weight / (height * height)
        print(f"BMI = {bmi:.2f}") # Formats the number to show only 2 decimal places
        
        # Check the BMI ranges to find the correct weight category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25.0:
            category = "Normal Weight"
        elif 25.0 <= bmi < 30.0:
            category = "Overweight"
        else:
            category = "Obese"
            
        print(f"Category: {category}")
        
        # Option to try again or return to the main menu
        repeat = input("\nDo you want to calculate BMI again? (yes/no): ").strip().lower()
        if repeat != 'yes':
            break # Stops this task and goes back to the menu loop

if __name__ == "__main__":
    # Starts the program automatically when the file is opened
    main_menu()
